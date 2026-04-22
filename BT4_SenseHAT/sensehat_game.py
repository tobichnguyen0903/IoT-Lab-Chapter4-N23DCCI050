rom sense_emu import SenseHat
import random, time

sense = SenseHat()
sense.clear()

# Vi tri nhan vat (trang) va muc tieu (xanh la)
px, py = 3, 3
tx, ty = random.randint(0,7), random.randint(0,7)
score = 0

def draw():
    sense.clear()
    sense.set_pixel(tx, ty, [0, 255, 0])      # Muc tieu = Xanh la
    sense.set_pixel(px, py, [255, 255, 255])  # Nhan vat = Trang

draw()

print("Game bat dau! Su dung Joystick tren Emulator de di chuyen.")
print("Nhan vao giua Joystick de xem diem.")

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            # Xu ly di chuyen va chan khong cho vuot bien (0-7)
            if event.direction == 'up' and py > 0:
                py -= 1
            elif event.direction == 'down' and py < 7:
                py += 1
            elif event.direction == 'left' and px > 0:
                px -= 1
            elif event.direction == 'right' and px < 7:
                px += 1
            elif event.direction == 'middle':
                sense.show_message(str(score), text_colour=[255,255,0])

            # Kiem tra neu an duoc muc tieu
            if px == tx and py == ty:
                score += 1
                print(f'Ghi ban! Diem hien tai: {score}')

                # Hieu ung Flash vang khi ghi diem (Yeu cau cua buoc 5)
                sense.clear([255, 255, 0])
                time.sleep(0.2)

                 # Tao muc tieu moi ngau nhien
                tx = random.randint(0, 7)
                ty = random.randint(0, 7)

            draw()
    time.sleep(0.05)





