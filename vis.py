from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

def plot(decoded):
        logData = decoded['fixedFrequency']

        gyro = figure(title="Gryoscope", y_axis_label='Gyroscope [°/s]', x_axis_label='Timestamp [ms]')
        gyro.line(logData['timestamp'], logData['gyro.x'], legend_label="X", line_color="red")
        gyro.line(logData['timestamp'], logData['gyro.y'], legend_label="Y", line_color="green")
        gyro.line(logData['timestamp'], logData['gyro.z'], legend_label="Z", line_color="blue")
        gyro.legend.click_policy = 'hide'

        accel = figure(title="Accelerometer", y_axis_label='Accelerometer [g]', x_axis_label='Timestamp [ms]')
        accel.line(logData['timestamp'], logData['acc.x'], legend_label="X", line_color="red")
        accel.line(logData['timestamp'], logData['acc.y'], legend_label="Y", line_color="green")
        accel.line(logData['timestamp'], logData['acc.z'], legend_label="Z", line_color="blue")
        accel.legend.click_policy = 'hide'
        
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
        ctrl.legend.click_policy = 'hide'
        
        stab = figure(title="Stabiliser", y_axis_label='', x_axis_label='Timestamp [ms]')
        stab.line(logData['timestamp'], logData['stabilizer.roll'], legend_label="Roll", line_color="red")
        stab.line(logData['timestamp'], logData['stabilizer.pitch'], legend_label="Pitch", line_color="green")
        stab.line(logData['timestamp'], logData['stabilizer.yaw'], legend_label="Yaw", line_color="blue")
        stab.line(logData['timestamp'], logData['stabilizer.thrust'], legend_label="Thrust", line_color="grey")
        stab.legend.click_policy = 'hide'

        return gridplot([gyro, accel, baro, temp, asl, ctrl, stab], ncols=2)

