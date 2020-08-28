from tkinter import *
from Sprite import *
from Coords import *
import time


class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        self.image_left = [
            PhotoImage(file='figures/figure_L1.gif'),
            PhotoImage(file='figures/figure_L2.gif'),
            PhotoImage(file='figures/figure_L3.gif')
        ]
        self.image_right = [
            PhotoImage(file='figures/figure_R1.gif'),
            PhotoImage(file='figures/figure_R2.gif'),
            PhotoImage(file='figures/figure_R3.gif')
        ]
        self.image = game.canvas.create_image(200, 470, image=self.image_left[0], anchor='nw')
        self.x = -2
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        self.game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.game.canvas.bind_all('<space>', self.jump)
        self.game.canvas.bind_all('<KeyPress-Up>', self.jump)

    def turn_left(self, event):
        #if self.y == 0:
            self.x = -2

    def turn_right(self, event):
        #if self.y == 0:
            self.x = 2

    def jump(self, event):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y == 0 and time.time() - self.last_time > 0.1:
            self.last_time = time.time()
            self.current_image += self.current_image_add
            if self.current_image >= 2:
                self.current_image_add = -1
            if self.current_image <= 0:
                self.current_image_add = 1
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.image_left[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.image_left[self.current_image])

        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.image_right[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.image_right[self.current_image])

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y1 = xy[1]
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates

    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
            self.jump_count -= 1

        co = self.coords()
        left = True
        right = True
        top = True
        bottom = True
        falling = True

        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False
        if self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False
        elif self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False

        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0 and collided_top(co, sprite_co):
                self.y = -self.y
                top = False
            if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and collided_bottom(1, co, sprite_co):
                falling = False
            if left and self.x < 0 and collided_left(co, sprite_co):
                self.x = 0
                left = False
                if sprite.endgame:
                    self.end(sprite)
            if right and self.x > 0 and collided_right(co, sprite_co):
                self.x = 0
                right = False
                if sprite.endgame:
                    self.end(sprite)

        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y = 4
        self.game.canvas.move(self.image, self.x, self.y)

    def end(self, sprite):
        self.game.running = False
        sprite.opendoor()
        time.sleep(1)
        self.game.canvas.itemconfig(self.image, state='hidden')
        sprite.closedoor()
