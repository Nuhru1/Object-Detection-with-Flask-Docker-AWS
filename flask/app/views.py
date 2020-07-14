from app import app

# ==== import all required files of yolo and EV=====

from flask import render_template, request, redirect
import os
from werkzeug.utils import secure_filename

# our yolo API
import yolo

import io as StringIO
import base64
from io import BytesIO
import io
import json
from PIL import Image
import numpy as np
import pandas as pd
import time
import cv2

from ev import EV3_Config, EV
from Evaluator import Features_selection
import glob



# <========= Image format checking for object detection part =================>

# app.config["IMAGE_UPLOADS"] ="/Users/nouhourouteonsa/MyWebApp-Flask/flask/static/img/uploads"
app.config["IMAGE_UPLOADS"] ="static/img/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


#================= function to empty folder ======================

def empty_folder(path):

	files = glob.glob(path)
	for f in files:
		os.remove(f)








# <======================== the Home route =================================>
@app.route("/")
def index():
	return render_template("index.html")
	

# <===================== the about route ===================================>
@app.route("/about")
def about():
	return render_template("about.html")






# <==============load the required files for YOLO model ==================>

labelsPath="/yolo_conf/coco.names"
cfgpath="/yolo_conf/yolov3.cfg"
wpath="/yolo_conf/yolov3.weights"
Lables= yolo.get_labels(labelsPath)
CFG= yolo.get_config(cfgpath)
Weights= yolo.get_weights(wpath)
nets= yolo.load_model(CFG,Weights)
Colors= yolo.get_colors(Lables)


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
	message = None
	filename = None
	detect_names = []
	# global img_encoded 

	empty_folder(app.config["IMAGE_UPLOADS"] + '/*')

	if request.method == "POST":
		
		if request.files:

			# image = request.files["image"].read()
			image = request.files["image"]
			# image = imag.read()
			pic = True

			if image.filename == None:
				message = "No file selected"
				print(message)
				return redirect(request.url)

			if image and allowed_image(image.filename):

				filename = secure_filename(image.filename)
				image = image.read()

				img = Image.open(io.BytesIO(image))
				np_img = np.array(img)
				im = np_img.copy()
				im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

				detect_names ,res=yolo.get_predection(im,nets,Lables,Colors)
				im=cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
				np_image=Image.fromarray(im)
				img_encoded =yolo.image_to_byte_array(np_image)

				f = open(os.path.join(app.config["IMAGE_UPLOADS"], filename), 'w+b')	
				# f = open(os.path.join(app.config["IMAGE_UPLOADS"], 'output.jpg'), 'w+b')	
				f.write(img_encoded)

				message = "Succesfully Processed and saved!!"
				print(message)
				print(filename)
				
				# return redirect(request.url)
			else:
				message = "That file extension is not allowed"
				print(message)
				return redirect(request.url)



	
	print(message)
	return render_template("/upload_image.html", file_name = filename, output_image = filename, detct = detect_names )







# <=========== File format checking for feature selection app===================>



app.config["CSV_UPLOADS"] ="/Users/nouhourouteonsa/MyWebApp-Flask/flask/static/csv/uploads"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["CSV"]


def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False



@app.route("/features-select", methods=["GET", "POST"])
def features_select():
	message=""
	inputFileName = "my_params.cfg"
	

	if request.method == "POST":

		if request.files:

			file = request.files["file"]

			if file.filename == "":
				print("No file selected")
				return redirect(request.url)

			if allowed_file(file.filename):


				file = pd.read_csv(file)
				# print(file.head)


				Features_selection.dataset = file

				#Get EV3 config params
				cfg=EV3_Config(inputFileName)

				#print config params
				print(cfg)

				#run EV3
				EV(cfg)




				# filename = secure_filename(file.filename)
				# file.save(os.path.join(app.config["CSV_UPLOADS"], filename))
				# print("file saved")

				return redirect(request.url)

			else:
				print("That file extension is not allowed")
				return redirect(request.url)


	return render_template("/features-select.html")