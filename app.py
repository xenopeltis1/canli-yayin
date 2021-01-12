import pyautogui
import io
from flask import Flask, render_template, Response


app = Flask(__name__)


def takeScreenShot():
    while True:
        myScreenshot = pyautogui.screenshot()
        buffer = io.BytesIO()
        myScreenshot.save(buffer, format="jpeg")
        img_data = buffer.getvalue()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img_data+ b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(takeScreenShot(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
