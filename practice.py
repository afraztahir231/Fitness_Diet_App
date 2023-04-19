''' how to get day from python
	import datetime
	now = datetime.datetime.now()
	day = now.strftime("%A")
	print(day)
'''
'''import smtplib

def send_email(subject, msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login('afraztahir123@gmail.com', 'afraztahirtah123')
		message = 'Subject: {}\n\n{}'.format(subject, msg)
		server.sendmail('afraztahir123@gmail.com', 'afraztahirtah123', message)
		server.quit()
		print('Email Sent')
	except:
		print('Email Sent')'''

'''import time
time.sleep(3) # Sleep for 3 seconds'''

'''import cx_Oracle

conn = cx_Oracle.connect('system/sys@localhost:1522/XE')
print(conn.version)'''

# importing vlc module
import vlc
  
# importing pafy module
import pafy
  
# url of the video
url = "https://www.youtube.com/watch?v = vG2PNdI8axo"
  
# creating pafy object of the video
video = pafy.new(url)
  
# getting best stream
best = video.getbest()
  
# creating vlc media player object
media = vlc.MediaPlayer(best.url)
  
# start playing video
media.play()