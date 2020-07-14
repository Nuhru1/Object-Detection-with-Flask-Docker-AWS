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

Note: download yolov3.weights from https://pjreddie.com/darknet/yolo/ and put it yolo_conf directory



run in local host with docker-compose:

$docker-compose build

$docker-compose up


app is running in the localhost:


![Screen Shot 2020-07-14 at 5 16 50 PM 1](https://user-images.githubusercontent.com/44145876/87408410-008ba580-c5f6-11ea-939f-8aee5686a25d.png)

#


## Running on AWS EC2

###- create a user with Programmatic access:
	. Programmatic access Enables an access key ID and secret access key for the AWS API, CLI, SDK, and other development tools. (save the access key ID and secret access key)
	. Add user to a group AdministratorAccess 

###- create and EC2 instance : for this project I used Amazon Linux 2 instance (t2.micro Free tier)

###- Configure Security Group:
A security group is a set of firewall rules that control the traffic for your instance. You can add rules to allow specific traffic to reach your instance. For example, if you want to set up a web server and allow Internet traffic to reach your instance, add rules that allow unrestricted access to the HTTP and HTTPS ports.


###- Connect to your EC2 instance with your Terminal:
	. Open your terminal in the directory containing your key pair file

	. change the permission to 400 : 
		. $chmod 400 key-pair-file-name (.pem file)

	. connect using :
		.$ssh ec2-user@IP -i key-pair file (IP: IPv4 Public IP of your EC2 instance)





coming soon...





