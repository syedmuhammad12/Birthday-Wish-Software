
# **************************** Importing Modules ********************

from tkinter import *
from pytube import YouTube
import pafy
import vlc 
from PIL import ImageTk,Image

# **************************** Main PRogram ************************

class Main(Tk):
    
    def __init__(self):
        
        # =================================== Creating Screen =========================
        
        super().__init__()
        super().geometry("700x500+330+100")
        super().state("zoomed")
        super().title("Happy Birthday Buddy")
        super().iconbitmap("birth.ico")
        
        # =================================== Background =================================
        
        self.background_pic = PhotoImage(file="happy birthday.png")
        self.background = Label(self,image=self.background_pic).pack()
        
        # =================================== Canvas for YT video ============================
        
        self.canva_wid = Canvas(self, width = 600, height= 300)
        self.canva_wid.place(x=50,y=370)
        self.canva_wid.create_rectangle(3,5,600,300)
        
        self.url = "https://www.youtube.com/watch?v=K2aJTT29ZdU"
        self.video = pafy.new(self.url)
        self.best = self.video.getbest()
        self.play = self.best.url

        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.player.set_hwnd(self.canva_wid.winfo_id()) #tkinter label or frame

        media = self.Instance.media_new(self.play)
        self.player.set_media(media)
        self.player.play()
        
        # ======================================== Adding Gif ================================
        
        self.birthday_gif = ImageTk.PhotoImage(Image.open("birthday.jpg"))
        self.f1 = Label(self,image=self.birthday_gif).place(x=50,y=50)

      
if __name__ == "__main__":
    window = Main()
    window.mainloop()
