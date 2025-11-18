import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    tmr = 0
    kk_img = pg.image.load("fig/3.png") #練習3
    kk_img = pg.transform.flip(kk_img, True, False) #練習3
    bg_img_flip = pg.transform.flip(bg_img, True, False) #練習8
    kk_rct = kk_img.get_rect() #練習10
    kk_rct.center = (300, 200) #練習10
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        delta = [-1, 0] # 演習1:デフォルトは左移動
        
        # 左右の移動量 (X方向) を計算
        if key_lst[pg.K_RIGHT]:
            delta[0] = +1 # 演習1:右キーで右に進む
        elif key_lst[pg.K_LEFT]:
            delta[0] = -2

        # 上下の移動量 (Y方向) を計算
        if key_lst[pg.K_UP]:
            delta[1] = -1
        if key_lst[pg.K_DOWN]:
            delta[1] = +1
            
        kk_rct.move_ip(tuple(delta)) # 演習2: move_ipは1回だけ実行

        screen.blit(bg_img, [-tmr, 0]) #練習5
        screen.blit(bg_img_flip, [-tmr + 1600, 0]) #練習7,練習8
        screen.blit(bg_img, [-tmr + 3200, 0]) #練習9
        screen.blit(kk_img, kk_rct) #練習4
        pg.display.update()
        tmr += 1 

        if tmr == 3200: #練習9
            tmr = 0     
        clock.tick(200) #練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()