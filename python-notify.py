#!/usr/bin/env python
# python pushbullet notification
# Does all of the notifying using pre made tools. checks which tools 
# are available on the system and to the user

#Variables
APP_NAME = "Aware Notifications"
Body = sys.argv[1]
Title = sys.argv[2]

#Backend Imports
try:
 from subprocess import call
 import sys 
 import os
except ImportError:
	print(ImportError)
	print("Fatal Error")
	exit()
	
try:
	import urllib2
except ImportError:
	#try system ping
	
# Notification Imports
try:
	from pushbullet import Pushbullet
	call('sudo pip install pushbullet')
except ImportError:
	Pushbullet = None

try:
	import notify2 as Notify
	call('sudo pip install notify2')
except ImportError:
    Notify = None

# Check Internet connectivity
def internet_on():
   try:
      response=urllib2.urlopen('http://74.125.228.100',timeout=1)
      return True
   except urllib2.URLError as err: pass
   return False

if Pushbullet && internet_on():
  api_key = raw_input("Plese input an API key for pushbullet \n leave blank for default")
  if !api_key:
  	api_key = "o.ru6eB9umOhBP0kgZliPj4mJUF4xVLR7Q"
	try:
	#read api from user, then hash and store data
	   pb = Pushbullet(api_key)
  excpt:
	api_key = raw_input("API did not work please enter a different API \n leave blank for default")
  # Compose Message

	# Push Message
	push = pb.push_note(Title, Body)

if Notify:

	Notify.init(APP_NAME)

	#Compose Message
	n = Notify.Notification(Title, Body,
         			 						"notification-message-im"   # Icon name
							     				)
  #Push Message   
	n.show()