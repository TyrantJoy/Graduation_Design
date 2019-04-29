import pyaudio
import wave

'''定义音频处理类'''
class Audio():

    '''初始化各项属性,如果想要修改音频的音质从这里修改'''
    def __init__(self):
        self.CHUNK = 8192
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.RECORD_SECONDS = 3

    '''录音,需要传入文件名字'''
    def record_audio(self, file_name):
        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(file_name, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    '''播放音频文件,需要传入文件名字'''
    def play_audio(self, filename):

        # 只读方式打开wav文件
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()
        # 打开数据流
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        # 读取数据
        data = wf.readframes(self.CHUNK)
        # 播放
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(self.CHUNK)
        # 停止数据流
        stream.stop_stream()
        stream.close()
        wf.close()
        # 关闭 PyAudio
        p.terminate()
