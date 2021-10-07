from flask import Flask, render_template, request

from bokeh.plotting import figure, show
from bokeh.resources import INLINE
from bokeh.embed import components
from bokeh.layouts import gridplot

import cfusdlog

app = Flask(__name__,
        static_url_path='',
        static_folder='static')

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        f = request.files['file']
        decoded = cfusdlog.decode(f.read())
        logData = decoded['fixedFrequency']

        gyro = figure(title="Gryoscope", y_axis_label='Gyroscope [°/s]', x_axis_label='Timestamp [ms]')
        gyro.line(logData['timestamp'], logData['gyro.x'], legend_label="X", line_color="red")
        gyro.line(logData['timestamp'], logData['gyro.y'], legend_label="Y", line_color="green")
        gyro.line(logData['timestamp'], logData['gyro.z'], legend_label="Z", line_color="blue")

        accel = figure(title="Accelerometer", y_axis_label='Accelerometer [g]', x_axis_label='Timestamp [ms]')
        accel.line(logData['timestamp'], logData['acc.x'], legend_label="X", line_color="red")
        accel.line(logData['timestamp'], logData['acc.y'], legend_label="Y", line_color="green")
        accel.line(logData['timestamp'], logData['acc.z'], legend_label="Z", line_color="blue")
        
        baro = figure(title="Barometer", y_axis_label='Pressure [hPa]', x_axis_label='Timestamp [ms]')
        baro.line(logData['timestamp'], logData['baro.pressure'], line_color="red")
        
        asl = figure(title="Above Sea Level (Baro)", y_axis_label='Above Sea Level [m]', x_axis_label='Timestamp [ms]')
        asl.line(logData['timestamp'], logData['baro.asl'], line_color="blue")

        temp = figure(title="Temperature (Baro)", y_axis_label='Temperature [°C]', x_axis_label='Timestamp [ms]')
        temp.line(logData['timestamp'], logData['baro.temp'], line_color="Green")

        ctrl = figure(title="Manual Control Inputs", y_axis_label='Control', x_axis_label='Timestamp [ms]')
        ctrl.line(logData['timestamp'], logData['ctrltarget.roll'], legend_label="Roll (X)", line_color="red")
        ctrl.line(logData['timestamp'], logData['ctrltarget.pitch'], legend_label="Pitch (Y)", line_color="green")
        ctrl.line(logData['timestamp'], logData['ctrltarget.yaw'], legend_label="Yaw", line_color="blue")
        
        stab = figure(title="Stabiliser", y_axis_label='', x_axis_label='Timestamp [ms]')
        stab.line(logData['timestamp'], logData['stabilizer.roll'], legend_label="Roll", line_color="red")
        stab.line(logData['timestamp'], logData['stabilizer.pitch'], legend_label="Pitch", line_color="green")
        stab.line(logData['timestamp'], logData['stabilizer.yaw'], legend_label="Yaw", line_color="blue")
        stab.line(logData['timestamp'], logData['stabilizer.thrust'], legend_label="Thrust", line_color="grey")

        plots_script, plots_div = components(gridplot([gyro, accel, baro, temp, asl, ctrl, stab], ncols=2))

        return render_template('plot.html',
                plots_script=plots_script,
                plots_div=plots_div,
                js_resources=INLINE.render_js(),
                css_resources=INLINE.render_css(),
        )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
