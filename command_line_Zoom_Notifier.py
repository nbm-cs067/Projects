import time
import os 
from win10toast import ToastNotifier
from SMWinservice import SMWinservice

ZoomFile = 'C:/Users/nbhatm/Downloads/Nayana Other stuffs/Python programs/Zoom_Notifier/Zoom_command_line_notifier_git/Zoom_notifier_datetime.txt'

class Zoom_Notifier(SMWinservice):
    _svc_name_ = "Zoom_Notifer_Python"
    _svc_display_name_ = "Zoom_Notifer_Python"
    _svc_description_ = "Notifies the user about meeting"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            fileName = open(ZoomFile, 'r') 
            meeting_datetime=fileName.read()
            list_of_meetings=[i.split(' ') for i in meeting_datetime.split('\n')]
            current_time=time.strftime('%H:%M')
            for individual_meeting in list_of_meetings:
                if(individual_meeting[0]!='#time'):
                    #print(current_time,individual_meeting[0])
                    if(current_time==individual_meeting[0]):
                        n = ToastNotifier() 
                        n.show_toast("Meeting with ",individual_meeting[1], duration = 5) 
                    
if __name__ == '__main__': 
    Zoom_Notifier.parse_command_line()

    