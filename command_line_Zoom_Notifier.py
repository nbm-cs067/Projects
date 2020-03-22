import time
import os 
from win10toast import ToastNotifier

ZoomFile = 'Zoom_notifier_datetime.txt'
  
def check_zoom_meetings(): 
    fileName = open(ZoomFile, 'r') 
    meeting_datetime=fileName.read()
    list_of_meetings=[i.split(' ') for i in meeting_datetime.split('\n')]
    current_time=time.strftime('%H:%M')
    for individual_meeting in list_of_meetings:
        if(individual_meeting[0]!='#time'):
            #print(current_time,individual_meeting[0])
            if(current_time==individual_meeting[0]):
                #print(individual_meeting[0])
                n = ToastNotifier() 
                n.show_toast("Meeting with ",individual_meeting[1], duration = 5) 
            else:
                print("No Meetings Now")            
               
if __name__ == '__main__': 
    check_zoom_meetings() 