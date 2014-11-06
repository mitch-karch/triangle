import win32service
import win32serviceutil
import win32api
import win32con
import win32event
import win32evtlogutil
import os, sys, string, time
import dataParser

class aservice(win32serviceutil.ServiceFramework):

    _svc_name_ = "TriangleWallpaper"
    _svc_display_name_ = "Triangle Wallpaper"
    _svc_description_ = "An automatic wallpaper generator and setter"

    def __init__(self, args):
           win32serviceutil.ServiceFramework.__init__(self, args)
           self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
           self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
           win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
      import servicemanager
      servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,servicemanager.PYS_SERVICE_STARTED,(self._svc_name_, ''))

      self.timeout = 60000
      while 1:
         # Wait for service stop signal, if I timeout, loop again
         rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
         # Check to see if self.hWaitStop happened
         if rc == win32event.WAIT_OBJECT_0:
            # Stop signal encountered
            servicemanager.LogInfoMsg("TriWall - STOPPED!")  #For Event Log
            break
         else:
             try:
                servicemanager.LogInfoMsg("TriWall - Alls well in love and war!")  #For Event Log
                dataParser.main()
                #file_path =  r"c:\data\dev\lab\experiments\triangle\dataParser.py"
                #execfile(file_path)
             except:
                 pass

def ctrlHandler(ctrlType):
   return True

if __name__ == '__main__':
   win32api.SetConsoleCtrlHandler(ctrlHandler, True)
   win32serviceutil.HandleCommandLine(aservice)

