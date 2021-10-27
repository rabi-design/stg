import tkinter as tk
import random, pygame
from PIL import Image, ImageTk
from math import sin, cos, pi
from time import sleep, time
from glob import glob
WINDOW_HEIGHT = 600  # ウィンドウの高さ
WINDOW_WIDTH = 600  # ウィンドウの幅

CANNON_Y = 400  # 自機のy座標

NUMBER_OF_ENEMY = 18  # 敵の数
ENEMY_SHOOT_INTERVAL = 200  # 敵がランダムに弾を打ってくる間隔

COLLISION_DETECTION = 300  # 当たり判定

BULLET_HEIGHT = 1  # 弾の縦幅
BULLET_WIDTH = 2  # 弾の横幅
BULLET_SPEED = 10  # 弾のスピード(10 ms)


class enemy:
    def __init__(self):
        self.x = WINDOW_WIDTH / 2
        self.y = 200
        self.draw()

    # noinspection PyAttributeOutsideInit
    def draw(self):
        self.id = cv.create_image(self.x, self.y, image=ene_tkimg, tag="enemy")


class EnemyBullet:  # 敵の弾

    def __init__(self, x, y, radian):
        self.x = x
        self.y = y
        self.radian = radian

    # noinspection PyAttributeOutsideInit
    def draw(self):
        self.id = cv.create_image(self.x, self.y, image=shot_tkimg, tag="bullet")

    # noinspection PyUnresolvedReferences,PyUnboundLocalVariable
    def shoot(self):
        global count
        if self.y <= WINDOW_HEIGHT:
            print(time() - nt)
            if time() - nt > 1:
                try:
                    if count > 7:
                        print(count)
                    else:
                        self.radian = self.radian + pi / 2
                        count += 1

                except:
                    self.radian = self.radian + pi / 2
                    print("aaa")
                    count = 1

            nx = BULLET_HEIGHT * cos(self.radian)
            ny = BULLET_HEIGHT * sin(self.radian)
            cv.move(self.id, nx, ny)
            self.y += BULLET_HEIGHT

            root.after(BULLET_SPEED, self.shoot)
        else:
            self.destroy()

    def destroy(self):
        cv.delete(self.id)


# noinspection PyAttributeOutsideInit


if __name__ == '__main__':
    count = 0
    pygame.mixer.init(frequency=44100)  # 初期設定
    ms = glob("music/*.mp3")
    for m in ms:
        pygame.mixer.music.load(m)  # 音楽ファイルの読み込み
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(1)
    nt = time()
    root = tk.Tk()
    root.title("invader")
    cv = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
    cv.pack()
    menubar = tk.Menu(root)
    root.configure(menu=menubar)
    menubar.add_command(label="QUIT", underline=0, command=root.quit)

    shot_img = Image.open("gai.jpg")
    shot_tkimg = ImageTk.PhotoImage(shot_img)
    ene_img = Image.open("astro.jpg")
    ene_tkimg = ImageTk.PhotoImage(ene_img)

    ene = enemy()
    ene.draw()
    hankei = 70
    for s in range(1, 9):
        rad = pi * s / 4
        fx = WINDOW_WIDTH / 2 + cos(rad) * hankei
        fy = 200 + sin(rad) * hankei
        enemybullet = EnemyBullet(fx, fy, rad)
        enemybullet.draw()
        enemybullet.shoot()

    # インスタンス生成
    # cannon = Cannon(WINDOW_WIDTH // 2, CANNON_Y)
    enemies = []
    root.mainloop()
