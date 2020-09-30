

from flask import Flask,render_template,Response
import cv2


app = Flask(__name__)

@app.route('/')
def camera():
    return render_template('camera.html')

def get_frame():
    camera_port = 0
    cam = cv2.VideoCapture(camera_port)

    while(True):

        ret,img=cam.read()
        imgencode=cv2.imencode('.jpg',img)[1]
        # img=cv2.imread('imgencode')
        # cv2.imshow("Original Image",imgencode)
        
        stringData = imgencode.tostring()

        yield (b'--frame\r\n'
        b'Content-Type: Text/plain\r\n\r\n' + stringData+b'\r\n')
    

@app.route('/video_stream')
def video_stream():
    return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
