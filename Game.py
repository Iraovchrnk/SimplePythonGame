from tkinter import *
import time
from PlatformSprite import *
from MovingPlatformSprite import *
from StickFigureSprite import *
from DoorSprite import *
import sys
import keyboard

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('Stickman\'s Escape')
        self.tk.resizable(0, 0)
        self.tk.wm_attributes('-topmost', 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_width = 500
        self.canvas_height = 500
        self.bg = PhotoImage(file='figures/background.gif')
        w = self.bg.width()
        h = self.bg.height()
        for i in range(5):
            for j in range(5):
                if (i + j) % 2 == 1:
                    self.canvas.create_image(i * w, j * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True
        self.text = self.canvas.create_text(240, 50, text="YOU ESCAPE!", font=("Helvetica", 20), state="hidden")

        door = DoorSprite(self, PhotoImage(file="figures/door1.gif"), 45, 30, 40, 35)
        platform1 = PlatformSprite(self, PhotoImage(file='figures/platform1.gif'), 0, 480, 100, 10)
        platform2 = MovingPlatformSprite(self, PhotoImage(file='figures/platform1.gif'), 150, 440, 100, 10)
        platform3 = PlatformSprite(self, PhotoImage(file='figures/platform1.gif'), 300, 400, 100, 10)
        platform4 = PlatformSprite(self, PhotoImage(file='figures/platform1.gif'), 300, 160, 100, 10)
        platform5 = PlatformSprite(self, PhotoImage(file='figures/platform2.gif'), 175, 350, 66, 10)
        platform6 = MovingPlatformSprite(self, PhotoImage(file='figures/platform2.gif'), 50, 300, 66, 10)
        platform7 = PlatformSprite(self, PhotoImage(file='figures/platform2.gif'), 170, 120, 66, 10)
        platform8 = PlatformSprite(self, PhotoImage(file='figures/platform2.gif'), 45, 60, 66, 10)
        platform9 = MovingPlatformSprite(self, PhotoImage(file='figures/platform3.gif'), 170, 250, 32, 10)
        platform10 = PlatformSprite(self, PhotoImage(file='figures/platform3.gif'), 230, 200, 32, 10)
        sf = StickFigureSprite(self)
        self.sprites.append(platform1)
        self.sprites.append(platform2)
        self.sprites.append(platform3)
        self.sprites.append(platform4)
        self.sprites.append(platform5)
        self.sprites.append(platform6)
        self.sprites.append(platform7)
        self.sprites.append(platform8)
        self.sprites.append(platform9)
        self.sprites.append(platform10)
        self.sprites.append(door)
        self.sprites.append(sf)

    def mainloop(self):

        while True:
            if self.running:
                for sprite in self.sprites:
                    sprite.move()
            else:
                self.canvas.itemconfig(self.text, state="normal")
                self.tk.update_idletasks()
                self.tk.update()
                while True:
                    if keyboard.is_pressed('ENTER') or keyboard.is_pressed('Esc'):
                        sys.exit(0)
                            #print("\nyou pressed Esc, so exiting...")
                            #sys.exit(0)
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)
