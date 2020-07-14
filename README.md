# Object-Detection-with-Flask-Docker-AWS-nginx

This repo is showing the steps for building obbject detection web application with:
Python, Flask, Docker compose.
The Objection detection Framwork used the YOLOv3.

### Deployement:
  - first option: AWS EC2 instance
  - Second option: Amazon Elastic Container Registry (ECR), Amazon Elastic Container Service (ECS) 


# Build the detection API and test it with Postman:

Note that the yolov3.weights file should be included in the Detection_API_Test/yolo_conf directory. I didn't put here because of it's size but it can be downloaded in the following link: https://pjreddie.com/darknet/yolo/

Run command:

$python api_test.py

Note that this part is run in local host.


## Test Result With Postman: 
![pic](https://user-images.githubusercontent.com/44145876/87327240-692b4180-c566-11ea-83f7-6c3824655667.png)


# Web Application

<!-- The architecture picture here nginx -->
### Overview of the architecture

![pic1](https://user-images.githubusercontent.com/44145876/87399587-2743df00-c5ea-11ea-9870-f60802141800.png)

#


The html and css files are respectively in /flask/templates and /flask/static directories.




comming soon...


