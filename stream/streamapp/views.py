from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .camera import VideoCamera
# Create your views here.

def home(request):
	return render(request, 'streamapp/home.html')

def stream(request):
	return render(request, 'streamapp/stream.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')
