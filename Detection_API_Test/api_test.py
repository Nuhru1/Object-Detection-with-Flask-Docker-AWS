from flask import Flask
from flask import render_template, request, redirect, Response
import os

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







app = Flask(__name__)


# <==============load the required files for YOLO model ==================>

labelsPath="/yolo_conf/coco.names"
cfgpath="/yolo_conf/yolov3.cfg"
wpath="/yolo_conf/yolov3.weights"
Lables= yolo.get_labels(labelsPath)
CFG= yolo.get_config(cfgpath)
Weights= yolo.get_weights(wpath)
nets= yolo.load_model(CFG,Weights)
Colors= yolo.get_colors(Lables)



@app.route("/", methods=["GET", "POST"])
def upload_image():

	filename = None


	image = request.files["image"].read()

	img = Image.open(io.BytesIO(image))
	np_img = np.array(img)
	im = np_img.copy()
	im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

	# detect_names ,res=yolo.get_predection(im,nets,Lables,Colors)
	res=yolo.get_predection(im,nets,Lables,Colors)

	im=cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
	np_image=Image.fromarray(im)
	img_encoded =yolo.image_to_byte_array(np_image)

	return Response(response = img_encoded, status=200,mimetype="image/jpeg")







if __name__ == "__main__":
	app.run()




