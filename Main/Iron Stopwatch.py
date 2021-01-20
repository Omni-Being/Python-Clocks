from tkinter import *
import time
from tkinter import messagebox

class StopWatch(Frame):  
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()               
        self.makeWidgets()

    def makeWidgets(self):                         
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr,font=('Arial',50),bg='gray')
        self._setTime(self._elapsedtime)
        l.grid(row=1,column=1,columnspan=4,pady=2,padx=2)                      
    
    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0

    def Dev(self):
        messagebox.showinfo(title="About Developer",message="Version  :\t\t1.0\nDeveloped By  :\tVikas Samal\nPowered By  :\tIron Boy\n\nCopyright \u00A9 2018")
        
    
    def Reset(self):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
        
        
def main():
    root = Tk()
    sw = StopWatch(root)
    sw.grid(row=0,column=0,columnspan=4)
    root.resizable(False,False)
    root.configure(bg='gray')
    root.title("Iron Stopwatch")
    Button(root, text='Start', command=sw.Start).grid(row=2,column=0,pady=10)
    Button(root, text='Stop', command=sw.Stop).grid(row=2,column=1,pady=10)
    Button(root, text='Reset', command=sw.Reset).grid(row=2,column=2,pady=10)
    Button(root, text='Quit', command=root.destroy).grid(row=2,column=3,pady=10)
    Button(root, text='About Developer',width=20,height=2,command=sw.Dev).grid(padx=20,pady=20,row=5,column=0,columnspan=4)
    
    
    root.mainloop()

if __name__ == '__main__':
    main()
