#coding=utf8
from flask import Flask, render_template, Response
from utils import get_img_list

app = Flask(__name__)

def gen_img():
    while True:
        frame = get_img_list()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/img_circle')
def img_circle():
    return Response(gen_img(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()
