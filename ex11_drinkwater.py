# Write a program to give a reminder to programmer to give notifcation to drink water every hour you can wither beep or send desktop notifcations
import os
import notify2
import time

#  Most basic implementation of the notification program 
def water_notifcation():
     
     for i in range(0,24):
    #   this program will sleep for 4 seconds
      time.sleep(4)
      notify2.init("Drink Water Notifier")
      notification = notify2.Notification(summary="pani piyo",message="Please Drink Water")
      notification.set_urgency(notify2.URGENCY_NORMAL)
      #displays the amount of time the notification will be shown
      notification.set_timeout(1000)
      notification.show()

water_notifcation()