import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print("时间到！")

# 设置专注时长（以秒为单位）
focus_duration = 25 * 60

print("专注模式启动！")
countdown(focus_duration)
print("专注模式结束！")
