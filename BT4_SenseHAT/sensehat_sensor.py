from sense_emu import SenseHat
import time

sense = SenseHat()

print("Dang doc du lieu cam bien... Nhan Ctrl+C de dung.")

try:
    while True:
        # Lay du lieu tu cac cam bien
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        press = sense.get_pressure()

        # In ket qua ra man hinh Terminal
        print(f'Temp: {temp:.1f}C | Humidity: {hum:.1f}% | Pressure: {press:.1f} mbar')

        # Doc moi giay mot lan
        time.sleep(1)
except KeyboardInterrupt:
    sense.clear()
    print('\nDa dung doc cam bien.')



