import pygame
import math

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

BH_X, BH_Y = 400, 300
BH_RADIUS = 20  # Batas event horizon
BH_MASS = 50000
G = 0.5

cahaya_list = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            cahaya_list.append({'x': float(mx), 'y': float(my), 'vx': 4.0, 'vy': -1.0})

    screen.fill(("#02051f"))

    # Gambar Black Hole Cokelat
    pygame.draw.circle(screen, ("#131314"), (BH_X, BH_Y), BH_RADIUS)

    # Physics Engine
    # Gunakan list comprehension untuk menyaring partikel yang belum masuk
    cahaya_baru = []
    for c in cahaya_list:
        dx = BH_X - c['x']
        dy = BH_Y - c['y']
        dist = math.sqrt(dx**2 + dy**2)

        # Logika: Kalau kena event horizon, foton 'ditelan' (jangan ditambah ke list baru)
        if dist < BH_RADIUS:
            continue 

        # Gravitasi
        force = (G * BH_MASS) / (dist**2)
        ax = (dx / dist) * force
        ay = (dy / dist) * force
        
        c['vx'] += ax
        c['vy'] += ay
        
        c['x'] += c['vx']
        c['y'] += c['vy']
        
        # Gambar partikel
        pygame.draw.circle(screen, ("white"), (int(c['x']), int(c['y'])), 2)

        # Simpan partikel yang masih "hidup"
        cahaya_baru.append(c)
    
    cahaya_list = cahaya_baru # Update list dengan partikel yang masih ada

    pygame.display.flip()
    clock.tick(60)

pygame.quit()