import os
import pywhatkit as pwt
import smtplib
import imghdr
from email.message import EmailMessage
import time 
from os import listdir
from os.path import isfile, join



def  whatsapp():
	number = "+919461647484"
	mess = "Hey, Gargi  how are you? \n "
	pwt.sendwhatmsg_instantly(number,mess,5)
	print("Whatsapp message Successfully Sended")
	print("byee")


def  mail():
	print("hello")
	Sender_Email = "testmodelml@gmail.com"	
	Reciever_Email = "testmodelml@gmail.com"
	Password = "test$1234"
	newMessage = EmailMessage()                         
	newMessage['Subject'] = "Alert Message." 
	newMessage['From'] = Sender_Email                   
	newMessage['To'] = Reciever_Email                   
	newMessage.set_content('Security Alert , Someone is trying to use your system please check the face..') 
	with open('./python/faces/user1/4.jpg', 'rb') as f:
		image_data = f.read()
		image_type = imghdr.what(f.name)
		image_name = f.name
	newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(Sender_Email, Password)              
		smtp.send_message(newMessage) 
		smtp.quit()
	print("Mail Successfully Sended ")
	print("byee")
	
    

def  ec2instance():
	print("hello")
	os.system("aws ec2 run-instances --image-id ami-0aeeebd8d2ab47354  --instance-type t2.micro  --count 1 --subnet-id subnet-0855ad39 --security-group-ids sg-0e12487e05a97fdba --key-name gargi2000  ")	
	print("Instance launch Successfully")
	print("byee")

    
def  ebsvolume():
	print("hello")
	os.system("aws ec2 create-volume --availability-zone us-east-1a --volume-type gp2 --size 5")
	print("Volume created Successfully")
	print("byee")

    