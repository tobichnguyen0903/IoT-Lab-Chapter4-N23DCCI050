import psutil
from datetime import datetime
from time import sleep

# Mở file ghi log (Bước 5)
log_file = open('system_log.txt', 'w')

try:
    while True:
        # Đọc CPU usage (Bước 2)
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        # BƯỚC 7: Phân loại trạng thái CPU
        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        # Đọc RAM và Disk (Bước 3)
        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024 ** 2)
        ram_total_mb = ram.total // (1024 ** 2)
        ram_pct = ram.percent

        disk = psutil.disk_usage('/')
        disk_pct = disk.percent

        # Lấy thời gian hiện tại và tạo chuỗi thông tin (Cập nhật Bước 7: thêm {status})
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = f'[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used_mb}/{ram_total_mb} MB ({ram_pct}%) | Disk: {disk_pct}% | {status}'
        
        # In ra terminal
        print(line)
        
        # BƯỚC 7: In thêm dòng cảnh báo nổi bật nếu CPU vượt mức NORMAL
        if status != 'NORMAL':
            print(f'  ⚠ {status}: CPU đang ở {cpu_avg:.1f}%')

        # Ghi vào file log và flush (Bước 5)
        log_file.write(line + '\n')
        log_file.flush()

        # Nghỉ 2 giây trước khi lặp lại
        sleep(2)

# BƯỚC 6: Xử lý ngắt chương trình khi bấm Ctrl + C
except KeyboardInterrupt:
    print('\nDừng giám sát.')
    
# BƯỚC 6: Đóng file an toàn
finally:
    log_file.close()
    print('Log saved to system_log.txt')
