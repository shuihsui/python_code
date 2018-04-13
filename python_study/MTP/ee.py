#!/usr/bin/env python
# -*- coding:utf8
#Created email

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def make_mpa_msg():
	email = MIMEMultipart('alternative')
	text = MIMEText('Hello,email!\r\n','plain')
	email.attach(text)
	html = MIMEText(
		'<html><body><h4>Hello,email</h4>'
		'</body></html>','html')
	email.attach(html)
	return email

def make_img_msg(fn):
	f = open(fn,'r')
	data = f.read()
	f.close()
	email = MIMEImage(data,name=fn)
	email.add_header('Content-Disposition','attachment;filename="%s"' % fn)
	return email

def send_Msg(fr,to,msg):
	s = SMTP('smtp.163.com')
	s.set_debuglevel(1)
	errs = s.sendmail(fr,to,msg)
	s.quit()

if __name__ == '__main__':

	SENDER = 'xxxxxxxxx@163.com'
	RECIPS = 'xxxxxxxxxx'
	SOME_IMG_FILE = '/home/shuihsui/Pictures/1.png'
	print('Sending multipart alternative msg...')
	msg = make_mpa_msg()
	msg['From'] = SENDER
	msg['To'] = ','.join(RECIPS)
	msg['Subject'] = 'multipart alternative test'
	send_Msg(SENDER,RECIPS,msg.as_string())

	print('Sending image message...')
	msg = make_img_msg(SOME_IMG_FILE)
	msg['From'] = SENDER
	msg['To'] = ','.join(RECIPS)
	msg['Subject'] = 'image file test'
	send_Msg(SENDER,RECIPS,msg.as_string())
	
