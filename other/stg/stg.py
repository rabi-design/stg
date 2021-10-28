import tkinter as tk
import random, pygame, sys, os
from PIL import Image, ImageTk
from math import sin, cos, pi
from time import time
from glob import glob
from pygame.locals import *


WINDOW_HEIGHT = 600  # ウィンドウの高さ
WINDOW_WIDTH = 800  # ウィンドウの幅
sys.setrecursionlimit(100000)
CANNON_Y = 400  # 自機のy座標
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(100, 100)
NUMBER_OF_ENEMY = 18  # 敵の数
ENEMY_SHOOT_INTERVAL = 200  # 敵がランダムに弾を打ってくる間隔

COLLISION_DETECTION = 300  # 当たり判定

BULLET_HEIGHT = 1  # 弾の縦幅
BULLET_WIDTH = 2  # 弾の横幅
BULLET_SPEED = 7  # 弾のスピード(10 ms)
pygame.init()
w = 50
h = 50

# noinspection PyAttributeOutsideInit,PyMethodMayBeStatic
class Cannon:  # 自機
    def __init__(self, x, y=CANNON_Y):
        self.x = x
        self.y = y
        self.draw()

    def draw(self):
        self.id = cv.create_image(
            self.x,
            self.y,
            image=cannon_tkimg,
            tag="cannon"
        )

    def bind(self):
        # cv.tag_bind(self.id, "<ButtonPress-3>", self.pressed)
        # cv.tag_bind(self.id, "<Button1-Motion>", self.dragged)
        #root.bind("<KeyPress>", self.key_event)
        self.key_event(pygame.key.get_pressed())
        root.after(50, self.bind)

    # def pressed(self, event):
    #     mybullet = MyBullet(event.x, self.y)
    #     mybullet.draw()
    #     mybullet.shoot()

    def key_event(self, event):
        mo = 10
        mo_s = 0
        mo_v = 0
        key = event
        if key[K_RSHIFT] == 1 or key[K_LSHIFT] == 1:
            mo = 5
        if key[K_RIGHT] == 1:
            mo_s = mo
            self.x += mo
        if key[K_LEFT] == 1:
            mo_s = -mo
            self.x -= mo
        if key[K_UP] == 1:
            mo_v = -mo
            self.y -= mo
        if key[K_DOWN] == 1:
            mo_v = mo
            self.y += mo
        cv.move(self.id, mo_s, mo_v)
        # try:
        #     dx = self.x + ex
        #     dy = self.y + ey
        #     self.x, self.y = cv.coords(self.id)
        #     cv.coords(self.id, dx, self.y)
        #     self.x = dx
        #     self.y = dy
        # except:
        #     pass

    def dragged(self, event):
        dx = event.x - self.x
        self.x, self.y = cv.coords(self.id)
        cv.coords(self.id, self.x + dx, self.y)
        self.x = event.x

    def destroy(self):
        cv.delete(self.id)


class enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.draw()

    # noinspection PyAttributeOutsideInit
    def draw(self):
        self.id = cv.create_image(self.x, self.y, image=ene_tkimg, tag="enemy")


# noinspection PyMethodMayBeStatic
class pre:
    def __init__(self):
        self.flg = True

    def ene_bu(self):
        hankei = 70
        nt = time()
        for s in range(1, 33):
            rad = pi * s / 16
            fx = ene_w + cos(rad) * hankei
            fy = ene_h + sin(rad) * hankei
            enemybullet = EnemyBullet(fx, fy, rad, self.flg, nt)

            enemybullet.draw()
            enemybullet.shoot()
        if self.flg:
            self.flg = False
        else:
            self.flg = True
        root.after(700, self.ene_bu)


# noinspection PyMethodMayBeStatic
class EnemyBullet:  # 敵の弾
    def __init__(self, x, y, radian, flg, nt):
        self.x = x
        self.y = y
        self.radian = radian
        self.nt = nt
        self.flg = flg

    # noinspection PyAttributeOutsideInit
    def draw(self):
        self.id = cv.create_image(self.x, self.y, image=shot_tkimg, tag="bullet")
        bullet1[self.id] = self.radian

    # noinspection PyUnresolvedReferences,PyUnboundLocalVariable
    def shoot(self):
        if -100 < self.y <= WINDOW_HEIGHT + 100 and -100 < self.x < WINDOW_WIDTH + 100:
            if time() - self.nt > 1:
                if self.flg:
                    self.radian = bullet1[self.id] + pi / 2
                else:
                    self.radian = bullet1[self.id] - pi / 2

            nx = BULLET_HEIGHT * cos(self.radian)
            ny = BULLET_HEIGHT * sin(self.radian)
            cv.move(self.id, nx, ny)
            self.y += BULLET_HEIGHT

            root.after(BULLET_SPEED, self.shoot)
        else:
            self.destroy()

    def destroy(self):
        bullet1.pop(self.id)
        cv.delete(self.id)


# noinspection PyMethodMayBeStatic
class music:
    def bgm(self):
        pygame.mixer.init(frequency=44100)  # 初期設定
        ms = glob("music/*.mp3")
        for m in ms:
            pygame.mixer.music.load(m)  # 音楽ファイルの読み込み
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(1)


if __name__ == '__main__':
    bullet1 = {}
    mu = music()
    mu.bgm()

    root = tk.Tk()
    root.title("invader")
    root.geometry("{0}x{1}+300+300".format(WINDOW_WIDTH, WINDOW_HEIGHT))
    cv = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
    cv.pack()
    menubar = tk.Menu(root)
    root.configure(menu=menubar)
    menubar.add_command(label="QUIT", underline=0, command=root.quit)

    shot_img = Image.open("images/gai.jpg")
    shot_tkimg = ImageTk.PhotoImage(shot_img)
    ene_img = Image.open("images/astro.jpg")
    ene_tkimg = ImageTk.PhotoImage(ene_img)
    cannon_img = Image.open("images/jiki.jpg")
    cannon_tkimg = ImageTk.PhotoImage(cannon_img)

    ene_w = WINDOW_WIDTH / 2
    ene_h = 200
    ene = enemy(ene_w, ene_h)
    ene.draw()
    prepare = pre()
    prepare.ene_bu()
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    # インスタンス生成
    cannon = Cannon(WINDOW_WIDTH // 2, CANNON_Y + 200)
    cannon.bind()
    root.mainloop()
