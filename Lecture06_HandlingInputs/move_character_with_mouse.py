from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global  running
    global  x, y
    global  cx, cy
    global  calcx, calcy
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            count = 0
            calcx = (x - cx) / 50
            calcy = (y - cy) / 50

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse_pointer = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
calcx, calcy = 0, 0
count = 0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if count <= 6:
        cx = calcx + cx
        cy = calcy + cy
        count = count + 1

    character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
    mouse_pointer.clip_draw(0, 0, 50, 52, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    # get_events()

close_canvas()




