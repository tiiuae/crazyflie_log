from flask import Flask, render_template, request
from bokeh.embed import components
from bokeh.resources import INLINE

from vis import plot
from cfusdlog import decode

app = Flask(__name__,
        static_url_path='',
        static_folder='static')

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        f = request.files['file']
        decoded = decode(f.read())
        plots_script, plots_div = components(plot(decoded))

        return render_template('plot.html',
                plots_script=plots_script,
                plots_div=plots_div,
                js_resources=INLINE.render_js(),
                css_resources=INLINE.render_css(),
        )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
