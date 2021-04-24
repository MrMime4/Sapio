from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .camera import VideoCamera
import cv2
import datetime
import numpy as np
from .models import Records


def stream(request):
    return render(request, 'stream.html')


def gen(camera):
    data = camera.send_data()
    gray_inp_img = data[0]
    old_pts = data[1]
    backup = data[2]
    backup_img = data[3]
    outp = data[4]
    ytest_pos = data[5]

    while True:
        lst = camera.get_frame()
        frame = lst[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/img\r\n\r\n' + frame + b'\r\n\r\n')

        new_inp_img = lst[1]
        new_gray = lst[1]
        new_pts, status, err = cv2.calcOpticalFlowPyrLK(gray_inp_img,
                                                    new_gray, old_pts, None, maxLevel=1,
                                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                                                              15, 0.08))

    # boundries
        if new_pts.ravel()[0] >= 600:
            new_pts.ravel()[0] = 600
        if new_pts.ravel()[1] >= 350:
            new_pts.ravel()[1] = 350
        if new_pts.ravel()[0] <= 20:
            new_pts.ravel()[0] = 20
        if new_pts.ravel()[1] <= 150:
            new_pts.ravel()[1] = 150
        if new_pts.ravel()[2] >= 600:
            new_pts.ravel()[2] = 600
        if new_pts.ravel()[3] >= 350:
            new_pts.ravel()[3] = 350
        if new_pts.ravel()[2] <= 20:
            new_pts.ravel()[2] = 20
        if new_pts.ravel()[3] <= 150:
            new_pts.ravel()[3] = 150
    ###############

    # drawing line
        x, y = new_pts[0, :, :].ravel()
        a, b = new_pts[1, :, :].ravel()
        cv2.line(new_inp_img, (x, y), (a, b), (0, 0, 255), 15)

        if new_pts.ravel()[0] > 400 or new_pts.ravel()[2] > 400:
            if new_pts.ravel()[0] > 550 or new_pts.ravel()[2] > 550:
                new_pts = backup.copy()
                new_inp_img = backup_img.copy()
                ytest_pos += 40

            #####################################################
                date = datetime.datetime.now().strftime('%H:%M:%S')
                print("Out at ", date)
                record = Records(stamp = date, direction = "OUT")
                record.save()
            ######################################################

        elif new_pts.ravel()[0] < 200 or new_pts.ravel()[2] < 200:
            if new_pts.ravel()[0] < 50 or new_pts.ravel()[2] < 50:
                new_pts = backup.copy()
                new_inp_img = backup_img.copy()
                ytest_pos += 40

            ########################################################
                date = datetime.datetime.now().strftime('%H:%M:%S')
                print("In at ", date)
                record = Records(stamp = date, direction = "IN")
                record.save()
            ##########################################################

        gray_inp_img = new_gray.copy()
        old_pts = new_pts.reshape(-1, 1, 2)


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
