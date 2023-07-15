import pygame
import random

# 初期化
pygame.init()

# 画面サイズ
screen_width = 640
screen_height = 480

# 画面作成
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Invaders")

# 色
white = (255, 255, 255)
black = (0, 0, 0)

# プレイヤー
player_width = 50
player_height = 50
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height - 10
player_speed = 5
player = pygame.Rect(player_x, player_y, player_width, player_height)

# 弾
bullet_width = 5
bullet_height = 10
bullet_speed = 10
bullet_color = white
bullets = []

# エイリアン
alien_width = 50
alien_height = 50
alien_speed = 2
alien_rows = 2
alien_cols = 6
alien_padding = 10
aliens = []
for row in range(alien_rows):
    for col in range(alien_cols):
        alien_x = col * (alien_width + alien_padding) + alien_padding
        alien_y = row * (alien_height + alien_padding) + alien_padding
        alien = pygame.Rect(alien_x, alien_y, alien_width, alien_height)
        aliens.append(alien)

# エイリアンの画像
alien_image = pygame.image.load("alien.png")

# ゲームループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player.x + player.width / 2 - bullet_width / 2
                bullet_y = player.y
                bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
                bullets.append(bullet)

    # プレイヤー移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    elif keys[pygame.K_RIGHT] and player.x < screen_width - player_width:
        player.x += player_speed

    # 弾移動
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # 衝突判定
    for bullet in bullets:
        for alien in aliens:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)

    # エイリアン移動
    for alien in aliens:
        alien.x += alien_speed
        if alien.x < 0 or alien.x > screen_width - alien_width:
            alien_speed = -alien_speed
            for a in aliens:
                a.y += alien_height
    screen.fill(black)
    # エイリアンの描画
    for alien in aliens:
        screen.blit(alien_image, alien)

    # 描画
    pygame.draw.rect(screen, white, player)
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)
    pygame.display.update()

    # ウェイト
    pygame.time.wait(50)

# 終了
pygame.quit()

