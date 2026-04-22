from machine import Pin
import dht
import time

# Khởi tạo các chân LED (Giống Bước 1)
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

# Khởi tạo chân DHT22 (Giống Bước 3)
sensor = dht.DHT22(Pin(16))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # In ra thông số
        t = time.localtime()
        ts = f'{t[3]:02d}:{t[4]:02d}:{t[5]:02d}'
        print(f'[{ts}] Temp: {temp:.1f}°C | Humidity: {hum:.1f}%')
        
        # Bắt đầu logic cảnh báo
        if temp > 30:
            red.value(1); yellow.value(0); green.value(0)
            print('  >> CẢNH BÁO: NHIỆT ĐỘ CAO!')
        elif hum > 80:
            red.value(0); yellow.value(1); green.value(0)
            print('  >> CẢNH BÁO: ĐỘ ẨM CAO!')
        else:
            red.value(0); yellow.value(0); green.value(1)
            print('  Bình thường.')
            
    except Exception as e:
        print(f'Lỗi: {e}')
        
    time.sleep(2)
