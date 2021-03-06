# Crazyflie Flight Review

![Screenshot of the plots](https://i.imgur.com/5Qt2D4d.png)

## 1. Description

This is a web application, that allows you to upload a log file from the
[Crazyflie], using the [Micro-SD card deck].

It is similar to [PX4 flight review], but supports the native logs generated by
the Micro-SD card deck.

Please use the `config.txt` provided with this project, so that plots are
generated correctly.

We use [Flask] for the web server and [Bokeh] for generating the
visualisations.

## 2. Prerequisites

You need to install the required packages before running.

```sh
pip3 install -r requirements.txt
```

## 3. Usage

First, run the web server:

```sh
python3 app.py
```

Then, you will be able to upload the log files on the web app by visiting the
page on your browser.

## 4. Copyright

The `cfusdlog.py` file is released GPL v3, a copy of the license is included in
the `cfusdlog.py.LICENSE` file.


[Flask]: https://flask.palletsprojects.com/en/2.0.x/
[Bokeh]: https://bokeh.org/

[Crazyflie]: https://www.bitcraze.io/products/crazyflie-2-1/
[Micro-SD card deck]: https://www.bitcraze.io/products/micro-sd-card-deck/
[PX4 flight review]: https://github.com/PX4/flight_review
