import wave
import struct
import math
# 设置音频参数
sample_rate = 44100  # 采样率，表示每秒采样多少次
duration = 5  # 音乐时长，单位为秒
# 计算采样次数和采样点数
num_samples = int(sample_rate * duration)
num_frames = num_samples
# 创建音频文件
wav_file = wave.open("twinkle.wav", "wb")
# 设置音频文件参数
wav_file.setnchannels(1)  # 单声道
wav_file.setsampwidth(2)  # 采样宽度，表示每个采样点占用多少字节
wav_file.setframerate(sample_rate)  # 采样率，表示每秒采样多少次
# 生成小星星音乐数据
notes = [262, 262, 392, 392, 440, 440, 392,
         349, 349, 330, 330, 294, 294, 262]
durations = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
             0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]
for i in range(len(notes)):
    # 计算当前音符的采样点数
    note_frames = int(sample_rate * durations[i])
    # 生成当前音符的音乐数据
    for j in range(note_frames):
        # 计算当前时刻的采样点数据
        t = float(j) / sample_rate
        sample = int(32767 * 0.5 * math.sin(2 * math.pi * notes[i] * t))
        # 将采样点数据写入音频文件
        wav_file.writeframes(struct.pack("<h", sample))
# 关闭音频文件
wav_file.close()