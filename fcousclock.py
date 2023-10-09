import time
import winsound

def start_focus_timer(duration_in_minutes):
    # 将输入的分钟数转换为秒数
    duration_in_seconds = duration_in_minutes * 60

    print("开始专注，持续 {} 分钟...".format(duration_in_minutes))

    # 等待指定时间
    time.sleep(duration_in_seconds)

    # 播放提示音
    frequency = 1500  # 声音频率
    duration = 1000   # 声音持续时间
    winsound.Beep(frequency, duration)

    print("专注时间到！")

# 以25分钟为一段时间进行专注
start_focus_timer(25)
