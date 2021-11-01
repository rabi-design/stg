import random, pygame, sys, os
from math import sin, cos, pi
from time import time
from glob import glob
from pygame.locals import *
WINDOW_HEIGHT = 600 # ウィンドウの高さ
WINDOW_WIDTH = 600  # ウィンドウの幅
sys.setrecursionlimit(100000)
CANNON_Y = 500  # 自機のy座標
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (100, 100)
NUMBER_OF_ENEMY = 18  # 敵の数
ENEMY_SHOOT_INTERVAL = 200  # 敵がランダムに弾を打ってくる間隔
BULLET_HEIGHT = 1  # 弾の縦幅
BULLET_WIDTH = 2  # 弾の横幅
BULLET_SPEED = 1  # 弾のスピード(10 ms)
bull_n = 0
z = 0
zz = 0
s = 0
sf = True
rec_1x = 200
rec_1y = WINDOW_HEIGHT
rec_2x = WINDOW_WIDTH
rec_2y = 400
n = 0
nt = time()

w = 50
h = 50

bulletx = {}
bullety = {}
bulletf = {}
bulletx2 = {}
bullety2 = {}
bullett2 = {}
bulletf2 = {}
HP = {}
mybullets = []
# mu = music()
# mu.bgm()

shot_img = pygame.image.load("images/gai.jpg")
ene_img = pygame.image.load("images/astro.jpg")
cannon_img = pygame.image.load("images/jiki.jpg")
bg_img = pygame.image.load("images/black.jpg")

ene_w = WINDOW_WIDTH / 2 - 80
ene_h = 100
PLAYER_X = WINDOW_WIDTH / 2
PLAYER_Y = CANNON_Y


# noinspection PyAttributeOutsideInit,PyMethodMayBeStatic,PyGlobalUndefined
class Cannon:  # 自機

    def bind(self):
        self.key_event(pygame.key.get_pressed())

    # def pressed(self, event):
    #     mybullet = MyBullet(event.x, self.y)
    #     mybullet.draw()
    #     mybullet.shoot()

    def key_event(self, event):
        global PLAYER_X, PLAYER_Y, sf, s
        mo = 0.5
        key = event
        myb = mybullet()
        if key[K_RSHIFT] == 1 or key[K_LSHIFT] == 1:
            mo = 0.05
        if key[K_RIGHT] == 1:
            PLAYER_X += mo
            if PLAYER_X > WINDOW_WIDTH - 25:
                PLAYER_X = WINDOW_WIDTH - 25
        if key[K_LEFT] == 1:
            PLAYER_X -= mo
            if PLAYER_X < 0:
                PLAYER_X = 0
        if key[K_UP] == 1:
            PLAYER_Y -= mo
            if PLAYER_Y < 0:
                PLAYER_Y = 0
        if key[K_DOWN] == 1:
            PLAYER_Y += mo
            if PLAYER_Y > WINDOW_HEIGHT - 25:
                PLAYER_Y = WINDOW_HEIGHT - 25
        if key[K_x] == 1:
            global tm
            if s < 3 and sf == True:
                tm = time()
                s += 1
                sf = False
                m = music()
                m.se_bom()

        if key[K_z] == 1:
            global bull_n, z
            z += 1
            if z % 200 == 1:
                myb.setb()
                bull_n += 1
        screen.blit(cannon_img, [int(PLAYER_X), int(PLAYER_Y)])


# noinspection PyAttributeOutsideInit,PyMethodMayBeStatic,PyGlobalUndefined
class mybullet:
    def setb(self):
        PSHOT_X = PLAYER_X
        PSHOT_Y = PLAYER_Y - 50
        bulletx[bull_n] = PSHOT_X
        bullety[bull_n] = PSHOT_Y
        bulletf[bull_n] = True

    # noinspection PyUnresolvedReferences,PyUnboundLocalVariable
    def shoot(self):
        for i in range(bull_n):
            if bulletf[i]:
                if 0 < bulletx[i] <= WINDOW_HEIGHT and 0 < bullety[i] < WINDOW_WIDTH:
                    if (bulletx[i] - ene_w) ** 2 + (bullety[i] - ene_h) ** 2 < 2500:
                        bulletf[i] = False
                    bullety[i] -= 0.5
                    screen.blit(shot_img, [int(bulletx[i]), int(bullety[i])])
                else:
                    bulletf[i] = False

    def rotate(self):
        global rec_1x, rec_2y
        rect = pygame.Rect(
            int(WINDOW_WIDTH / 2 - rec_1x / 2),
            0,
            int(rec_1x),
            int(rec_1y)
        )
        rec_1x -= 0.7
        screen.fill((255, 255, 255, 200), rect)
        rect2 = pygame.Rect(
            0,
            int(WINDOW_HEIGHT - rec_2y),
            int(rec_2x),
            int(rec_2y)
        )
        rec_2y -= 1.4
        screen.fill((255, 255, 255, 60), rect2)





class enemy:
    # noinspection PyAttributeOutsideInit
    def draw(self):
        self.id = screen.blit(ene_img, [int(ene_w), int(ene_h)])

# noinspection PyMethodMayBeStatic
class pre:
    def ene_bu(self):
        global nt, n
        hankei = 70
        if zz % 200 == 0 or zz ==0:
            nt = time()
            bulletx2[n] = []
            bullety2[n] = []
            bulletf2[n] = []
            for r in range(32):
                rad = pi * r / 16
                fx = ene_w + cos(rad) * hankei + 50
                fy = ene_h + sin(rad) * hankei + 50

                bulletx2[n].append(fx)

                bullety2[n].append(fy)

                bulletf2[n].append(True)
            n += 1
        enemybullet = EnemyBullet()
        enemybullet.shoot()



    def hp(self):
        hankei = 40
        nt = time()
        for r in range(1, 128):
            rad = pi * r / 64
            fx = ene_w + cos(rad) * hankei
            fy = ene_h + sin(rad) * hankei
            enemybullet = EnemyBullet(rad, nt)


# noinspection PyMethodMayBeStatic,PyAttributeOutsideInit,PyGlobalUndefined
class EnemyBullet:  # 敵の弾
    def move(self, x, y):
        x = int(x)
        y = int(y)
        screen.blit(shot_img, [x, y])

    def hein(self, x, y, rad):
        global th
        x = x
        y = y
        if PLAYER_Y < y  < PLAYER_Y + 50 and PLAYER_X < x  < PLAYER_X + 50:
            try:
                if time() - th > 0.3 or time() - th == 0:
                    music().se_bom()
            except:
                pass
            th = time()
            return "e", "r"
        if 0 < y <= WINDOW_HEIGHT and 0 < x < WINDOW_WIDTH:

            x += BULLET_SPEED * cos(rad)
            y += BULLET_SPEED * sin(rad)
        else:
            return "e", "r"
        return x, y

    # noinspection PyUnresolvedReferences,PyUnboundLocalVariable
    def shoot(self):
        global bulletx2, bullety2, bulletf2, rad_h


        for m in range(n):
            try:
                if 1 > time() - nt > 0.5:
                    rad_h = pi / 2

                # elif 0.5 <= time() - nt:
                #     rad_h = -1 * pi / 2
                bulletf2[m][j] = False
            except:
                pass

            count = 0
            for j in range(32):
                try:
                    rad = pi * j / 16 + rad_h
                    x = bulletx2[m][j]
                    y = bullety2[m][j]

                    u, v = self.hein(x, y, rad)
                    if u == "e" or v == "r":
                        count += 1
                        if count == 31:
                            bulletx2.pop(m)
                            bullety2.pop(m)
                            bulletf2.pop(m)
                            rad_h += pi / 2
                        continue
                    bulletx2[m][j], bullety2[m][j] = u, v
                    self.move(bulletx2[m][j], bullety2[m][j])
                except:
                    pass


# def destroy2():
#     cv.delete(HP[0])
#     HP[0].pop()


# noinspection PyMethodMayBeStatic
class music:
    def bgm(self):
        pygame.mixer.init(frequency = 44100)  # 初期設定
        ms = glob("music/*.mp3")
        for m in ms:
            pygame.mixer.music.load(m)  # 音楽ファイルの読み込み
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(1)

    def se_bom(self):
        ms = "music/SE/pityu3.wav"
        m = pygame.mixer
        m.init(frequency=44100)  # 初期設定
        a = m.Sound(ms)  # 音楽ファイルの読み込み
        a.set_volume(0.5)
        a.play()


# noinspection PyGlobalUndefined
def main():
    global sf, rec_1x, rec_2y, zz
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_img, [0, 0])
    ene = enemy()
    ene.draw()

    cannon = Cannon()
    cannon.bind()
    prepare = pre()
    prepare.ene_bu()
    zz += 1
    # prepare.hp()
    mybmain = mybullet()
    mybmain.shoot()
    if not sf and time() - tm < 2:
        mybmain.rotate()
    else:
        sf = True
        rec_1x = 200
        rec_2y = 400
    pygame.display.update()

    clock.tick()
    # インスタンス生成

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    rad_h = 0
    pygame.init()
    pygame.display.set_caption("シューティングゲーム")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    clock = pygame.time.Clock()
    music().bgm()

    while True:
        main()
