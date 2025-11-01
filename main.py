# Autor: Eduardo Ogliari, 2025

# Largura e altura da janela
WIDTH = 600
HEIGHT = 600

# Tamanho de cada tile do level
TILE_SIZE = 32

# Quantos tiles por largura e altura de tela
TILES_PER_WIDTH = 18
TILES_PER_HEIGHT = 18

GRAVITY = 12.0
PLAYER_MOVEMENT_SPEED = 200.0
JUMP_HEIGHT = -6.0

# Lista onde cada índice corresponde à um tile do jogo
# Legenda:
# '  ' -> Espaço em branco
# 't ' -> Topo de plataforma
# 'r ' -> Lado direito de plataforma
# 'l ' -> Lado esquerdo de plataforma
# 'c ' -> Centro de plataforma
# 'tl' -> Canto esquerdo superior de plataforma
# 'tr' -> Canto direito superior de plataforma
# 'e ' -> Inimigo
# 'p ' -> Jogador
# 'g ' -> Goal
level = [
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    'g ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    't ', 't ', 'tr', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', 'tl', 'tr', '  ', 'e ', '  ', '  ', 'tl', 'tr', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', 't ', 't ', 't ', 't ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'tl', 'tr', '  ', '  ', '  ',
    'p ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'tl', 'c ', '  ', '  ', '  ', '  ',
    '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'tl',
    't ', 'tr', '  ', '  ', '  ', '  ', '  ', '  ', 'tl', 't ', 'tr', '  ', '  ', '  ', '  ', '  ', 'tl', 't ', 'c ',
    'c ', 'r ', '  ', '  ', 'e ', '  ', '  ', 'tl', 'c ', 'c ', 'r ', '  ', 'e ', '  ', '  ', '  ', 'l ', 'c ', 'c ',
    'c ', 'c ', 't ', 't ', 't ', 't ', 't ', 'c ', 'c ', 'c ', 'c ', 't ', 't ', 't ', 't ', 't ', 'c ', 'c ', 'c ',
    'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ',
    'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c ', 'c '
]


# Classe utilizada para posição
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Botões de interface
class Button:
    def __init__(self, text, rect):
        self.rect = rect
        self.text = text

    def draw(self):
        screen.draw.textbox(self.text, self.rect,
                            color="white", background="midnightblue")


# Tiles do level
class Tile:
    def __init__(self, x, y, sprite_name):
        self.rect = Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.sprite_name = sprite_name

    def draw(self):
        screen.blit(self.sprite_name, (self.position.x, self.position.y))


# Frame de animação
class Frame:
    def __init__(self, file_name, duration):
        self.file_name = file_name
        self.duration = duration


# Animação de sprite
class Animation:
    def __init__(self, animation_name, frames):
        self.animation_name = animation_name
        self.frames = frames


# Componente que gerencia as animações de um objeto
class AnimationComponent:
    def __init__(self, animations):
        self.animations = animations
        self.current_animation = None
        self.animation_dt = 0
        self.frame_index = 0

    def get_current_frame_sprite(self):
        sprite_name = ""
        if self.current_animation:
            sprite_name = self.current_animation.frames[self.frame_index].file_name
        return sprite_name

    def set_animation(self, animation_name):
        if self.current_animation:
            if animation_name == self.current_animation.animation_name:
                return

        for a in self.animations:
            if a.animation_name == animation_name:
                self.current_animation = a
                self.animation_dt = 0
                self.frame_index = 0
                break

    def update(self, dt):
        if self.current_animation:
            self.animation_dt += dt
            if (self.animation_dt >= self.current_animation.frames[self.frame_index].duration):
                self.animation_dt = 0.0
                self.frame_index = (
                    self.frame_index + 1) % len(self.current_animation.frames)


# Objeto que ao encostar encerra o level
class Goal:
    def __init__(self, sprite_name, position):
        self.sprite_name = sprite_name
        self.rect = Rect(position.x, position.y, TILE_SIZE, TILE_SIZE)
        self.finished = False

    def draw(self):
        screen.blit(self.sprite_name, (self.rect.x, self.rect.y))


# Classe para objetos que se movem
class MovingEntity:
    def __init__(self, animations):
        self.animation_component = AnimationComponent(animations)
        self.move_vector = Vector2(0, 0)
        self.bounds = Rect(0, 0, 32, 32)
        self.velocity = Vector2(0, 0)
        self.on_ground = False
        self.sprite_collider_offset = Vector2(16, 32)
        self.movement_speed = 1.0

    def update(self, dt):
        pass

    def debug_draw(self):
        screen.draw.rect(self.bounds, (255, 0, 0))

    def draw(self):
        sprite_name = self.animation_component.get_current_frame_sprite()

        if sprite_name:
            pos = Vector2(self.bounds.x - self.sprite_collider_offset.x,
                          self.bounds.y - self.sprite_collider_offset.y)
            screen.blit(sprite_name, (pos.x, pos.y))

    def update_collision(self, dt):
        global tiles
        ground_check = False

        self.bounds.y -= self.move_vector.y * dt

        # Se está pulando, então não está no chão
        if self.velocity.y < 0.0:
            self.on_ground = False

        # Só aplica gravidade se não está encostando no chão
        if self.on_ground == False:
            self.velocity.y += dt * GRAVITY
            if self.velocity.y > 100.0:
                self.velocity.y = 100.0

        self.bounds.y += self.velocity.y

        if self.velocity.y < 0.0:
            # Testa colisão com parte de baixo de um tile
            for t in tiles:
                air_rect = self.bounds.copy()
                air_rect.y -= 1

                if air_rect.colliderect(t.rect):
                    if air_rect.y <= t.rect.y + t.rect.h:
                        adjusted_position_y = t.rect.y + t.rect.h + 0.1
                        self.bounds.y = adjusted_position_y
                        self.velocity.y = 0.0
                        break
        else:
            # Testa colisão com parte de cima de um tile
            for t in tiles:
                ground_rect = self.bounds.copy()
                ground_rect.y += 1

                if ground_rect.colliderect(t.rect):
                    ground_check = True
                    adjusted_position_y = t.rect.y - self.bounds.h - 0.1
                    self.bounds.y = adjusted_position_y
                    break

            self.on_ground = ground_check

            if self.on_ground:
                self.velocity.y = 0

        # Movimenta jogador no eixo X
        self.bounds.x += self.move_vector.x * dt * self.movement_speed

        # Testa colisão pelos lados
        for t in tiles:
            if self.bounds.colliderect(t.rect):
                if self.bounds.x <= t.rect.x + t.rect.w and self.bounds.x + self.bounds.w > t.rect.x + t.rect.w:
                    if (self.bounds.y <= t.rect.y and self.bounds.y + self.bounds.h > t.rect.y) or (self.bounds.y > t.rect.y and self.bounds.y + self.bounds.h > t.rect.y + t.rect.h):
                        self.bounds.x = t.rect.x + t.rect.w + 0.1
                        break

                elif self.bounds.x + self.bounds.w >= t.rect.x:
                    if (self.bounds.y <= t.rect.y and self.bounds.y + self.bounds.h > t.rect.y) or (self.bounds.y > t.rect.y and self.bounds.y + self.bounds.h > t.rect.y + t.rect.h):
                        self.bounds.x = t.rect.x - self.bounds.w - 0.1
                        break

        # Testa colisão com os cantos esquerdo e direito da tela
        if self.bounds.x < 0:
            self.bounds.x = 0
        elif self.bounds.x + self.bounds.w > WIDTH:
            self.bounds.x = WIDTH - self.bounds.w


# Classe do jogador
class Player(MovingEntity):
    def __init__(self, player_animations):
        super().__init__(player_animations)
        self.jump_pressed = False
        self.movement_speed = PLAYER_MOVEMENT_SPEED

    def on_key_down(self, key):
        if key == keys.SPACE and self.on_ground:
            self.jump_pressed = True

    def update_move(self):
        self.move_vector.x = 0.0
        self.move_vector.y = 0.0

        if keyboard.left:
            self.move_vector.x = -1.0
        elif keyboard.right:
            self.move_vector.x = 1.0

        if self.jump_pressed:
            self.jump_pressed = False
            self.velocity.y = JUMP_HEIGHT
            if sound_enabled:
                sounds.jump.play()

    def update(self, dt):
        self.update_move()
        self.update_collision(dt)

        if self.on_ground:
            if self.move_vector.x > 0:
                self.animation_component.set_animation('player_walk')
            elif self.move_vector.x < 0:
                self.animation_component.set_animation('player_walk_flip')
            else:
                self.animation_component.set_animation('player_idle')
        else:
            if self.move_vector.x > 0:
                self.animation_component.set_animation('player_jump')
            else:
                self.animation_component.set_animation('player_jump_flip')

        self.animation_component.update(dt)


# Classe de inimigo
class Enemy(MovingEntity):
    def __init__(self, enemy_animations):
        super().__init__(enemy_animations)
        self.movement_speed = 50.0
        self.bounds.h = 16
        self.sprite_collider_offset.x = 0.0
        self.sprite_collider_offset.y = 16
        self.move_vector.x = 1.0
        self.defeated = False

    def set_defeated(self, value):
        self.defeated = value
        if self.defeated:
            self.animation_component.set_animation('enemy_hit')
            # Inimigo derrotado é removido após 2 segundos
            clock.schedule_unique(self.cleanup, 2.0)

    def cleanup(self):
        enemies.remove(self)

    def update(self, dt):
        global tiles

        if self.defeated:
            pass
        else:
            distance_from_wall = 4.0

            # Basicamente, o inimigo se move para esquerda ou direita até colidir com um tile, que o faz mudar de direção
            if self.move_vector.x > 0.0:
                right_rect = self.bounds.copy()
                right_rect.x += distance_from_wall

                for t in tiles:
                    if right_rect.colliderect(t.rect):
                        if (right_rect.x + right_rect.w) >= t.rect.x and right_rect.x < t.rect.x:
                            self.move_vector.x = -1.0
                            break
            elif self.move_vector.x < 0.0:
                left_rect = self.bounds.copy()
                left_rect.x -= distance_from_wall

                for t in tiles:
                    if left_rect.colliderect(t.rect):
                        if left_rect.x < t.rect.x + t.rect.w and left_rect.x + left_rect.w > t.rect.x + t.rect.w:
                            self.move_vector.x = 1.0
                            break

            self.update_collision(dt)

            if self.on_ground:
                if self.move_vector.x > 0:
                    self.animation_component.set_animation('enemy_walk')
                elif self.move_vector.x < 0:
                    self.animation_component.set_animation('enemy_walk_flip')
                else:
                    self.animation_component.set_animation('enemy_idle')

            self.animation_component.update(dt)


# -------------------- Inicialização --------------------------------------------------------
# Lista com todas as animações do personagem controlado
player_animations = [
    Animation("player_idle", [Frame("character_pink_front", 0.5), Frame(
        "character_pink_front_blink", 0.25)]),
    Animation("player_walk", [Frame("character_pink_walk_a", 0.25), Frame(
        "character_pink_walk_b", 0.25)]),
    Animation("player_walk_flip", [Frame("character_pink_walk_a_flip", 0.25), Frame(
        "character_pink_walk_b_flip", 0.25)]),
    Animation("player_jump", [Frame("character_pink_jump", 0.0)]),
    Animation("player_jump_flip", [Frame("character_pink_jump_flip", 0.0)]),
    Animation("player_hit", [Frame("character_pink_hit", 0.0)]),
]


# Lista com todas as animações de um inimigo
enemy_animations = [
    Animation("enemy_idle", [Frame("slime_normal_walk_a", 0.5), Frame(
        "slime_normal_walk_b", 0.25)]),
    Animation("enemy_walk", [Frame("slime_normal_walk_a", 0.25), Frame(
        "slime_normal_walk_b", 0.25)]),
    Animation("enemy_walk_flip", [Frame("slime_normal_walk_a_flip", 0.25), Frame(
        "slime_normal_walk_b_flip", 0.25)]),
    Animation("enemy_hit", [Frame("slime_normal_flat", 0.0)])
]

goal = None
player = Player(player_animations)
player.animation_component.set_animation("player_idle")

tiles = []
enemies = []
stars = []

paused = False
sound_enabled = True

button_height = 30
button_width = 300

start_button = Button("Iniciar", Rect(
    WIDTH/2 - button_width/2, HEIGHT/2, button_width, button_height))

sound_button = Button("Som: ON", Rect(WIDTH / 2 - button_width/2,
                      HEIGHT/2 + button_height + 10, button_width, button_height))

exit_button = Button("Sair", Rect(WIDTH / 2 - button_width/2,
                     HEIGHT / 2 + (button_height*2) + 20, button_width, button_height))

tile_position_x = 0
tile_position_y = 0

star_pos_y = -HEIGHT - 100
star_offset_x = 0

# Inicializa estrelas que descem do céu
for i in range(16):
    star_pos_x = 0

    if i % 2 == 0:
        star_offset_x = 16
    else:
        star_offset_x = 0

    for y in range(16):
        stars.append(Vector2(star_pos_x + star_offset_x, star_pos_y))
        star_pos_x += WIDTH / 16
    star_pos_y += (HEIGHT + 50) / 16


# Instancia todos os objetos a partir da lista com tiles
for block in level:
    pos_x = (TILE_SIZE * tile_position_x)
    pos_y = (TILE_SIZE * tile_position_y)

    tag = block.strip()

    if tag == 'c':
        tiles.append(Tile(pos_x, pos_y, 'terrain_grass_block_center'))
    elif tag == 't':
        tiles.append(Tile(pos_x, pos_y, 'terrain_grass_block_top'))
    elif tag == 'tr':
        tiles.append(Tile(pos_x, pos_y, 'terrain_grass_block_top_right'))
    elif tag == 'tl':
        tiles.append(Tile(pos_x, pos_y, 'terrain_grass_block_top_left'))
    elif tag == 'r':
        tiles.append(Tile(pos_x, pos_y, 'terrain_grass_block_right'))
    elif tag == 'l':
        tiles.append(Tile(pos_x, pos_y, 'terrain_grass_block_left'))
    elif tag == 'e':
        enemy = Enemy(enemy_animations)
        enemy.animation_component.set_animation("enemy_idle")
        enemy.bounds.x = pos_x
        enemy.bounds.y = pos_y
        enemies.append(enemy)
    elif tag == 'p':
        player.bounds.x = pos_x
        player.bounds.y = pos_y
    elif tag == 'g':
        goal = Goal("sign_exit", Vector2(pos_x, pos_y))

    tile_position_x += 1

    if (tile_position_x > TILES_PER_WIDTH):
        tile_position_x = 0
        tile_position_y += 1


# Reseta as posições de inimigos e do jogador ao encostar em um inimigo
def reset_positions():
    global tile_position_x
    global tile_position_y
    tile_position_x = 0
    tile_position_y = 0

    enemies.clear()

    for block in level:
        pos_x = (TILE_SIZE * tile_position_x)
        pos_y = (TILE_SIZE * tile_position_y)

        tag = block.strip()

        if tag == 'e':
            enemy = Enemy(enemy_animations)
            enemy.animation_component.set_animation("enemy_idle")
            enemy.bounds.x = pos_x
            enemy.bounds.y = pos_y
            enemies.append(enemy)
        elif tag == 'p':
            player.bounds.x = pos_x
            player.bounds.y = pos_y

        tile_position_x += 1

        if (tile_position_x > TILES_PER_WIDTH):
            tile_position_x = 0
            tile_position_y += 1


def on_key_down(key):
    global paused

    player.on_key_down(key)

    if key == keys.ESCAPE:
        paused = not paused


def on_mouse_down(pos, button):
    global paused
    global sound_enabled

    if button.LEFT:
        if paused == False:
            if start_button.rect.collidepoint(pos):
                paused = True
            elif exit_button.rect.collidepoint(pos):
                quit()
            elif sound_button.rect.collidepoint(pos):
                sound_enabled = not sound_enabled
                if sound_enabled:
                    sound_button.text = "Som: ON"
                    music.unpause()
                else:
                    sound_button.text = "Som: OFF"
                    music.pause()


def draw_tiles():
    for t in tiles:
        screen.blit(t.sprite_name, (t.rect.x, t.rect.y))
        # screen.draw.rect(t.rect, (0, 255, 0))


def update(dt):
    if paused == False:
        return

    player.update(dt)

    for e in enemies:
        if e.defeated:
            continue

        e.update(dt)

        # Verifica se inimigo colidiu com o jogador
        # Se encostou por cima o inimigo é derrotado, caso contrário o jogador é derrotado
        if e.bounds.colliderect(player.bounds):
            if player.velocity.y > 0.0 and player.on_ground == False and player.bounds.y + player.bounds.h >= e.bounds.y:
                print("DEFEAT")
                if sound_enabled:
                    sounds.hit.play()
                e.set_defeated(True)
                player.velocity.y = JUMP_HEIGHT / 2
            else:
                print("DAMAGE")
                if sound_enabled:
                    sounds.restart.play()
                reset_positions()
                break

    if goal:
        # Se encostou na plaquinha, encerra o jogo
        if goal.rect.colliderect(player.bounds):
            if goal.finished == False:
                print("GOAL")
                goal.finished = True
                enemies.clear()

                music.play('end')
                if sound_enabled == False:
                    music.pause()

        # Anima as estrelas
        if goal.finished:
            for i in range(len(stars)):
                stars[i].y += dt * 50
                if stars[i].y >= HEIGHT:
                    stars[i].y = -50


def draw():
    screen.clear()
    screen.fill((110, 150, 220))

    # Apenas desenha as estrelas se o jogo já encerrou
    if goal.finished:
        for s in stars:
            screen.blit('star', (s.x, s.y))

    draw_tiles()

    for e in enemies:
        e.draw()
        # e.debug_draw()

    goal.draw()

    player.draw()
    # player.debug_draw()

    # Apenas desenha a interface se o jogo está pausado
    if paused == False:
        start_button.draw()
        sound_button.draw()
        exit_button.draw()
        screen.draw.textbox("Espaco = Pular", Rect(
            0, HEIGHT - 100, 300, 30), color="white", background="black")
        screen.draw.textbox("Setas = Movimento", Rect(
            0, HEIGHT - 50, 300, 30), color="white", background="black")


music.play('musica')
