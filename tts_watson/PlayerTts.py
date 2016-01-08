import pyaudio
import wave
from tts_watson.TextToSpeechService import TextToSpeechService


class PlayerTts:
    RATE = 22050
    SAMPWIDTH = 2
    NCHANNELS = 1

    def __init__(self):
        self.textToSpeechService = TextToSpeechService()

    def play(self, text):
        req = self.textToSpeechService.synthesize(text)
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(self.SAMPWIDTH),
                        channels=self.NCHANNELS,
                        rate=self.RATE,
                        output=True)
        bytesRead = 0
        dataToRead = ''
        for data in req.iter_content(1):
            dataToRead += data
            bytesRead += 1
            if bytesRead % 2048 == 0:
                stream.write(dataToRead)
                dataToRead = ''
        stream.stop_stream()
        stream.close()
        p.terminate()

    def playToTest(self):
        wf = wave.open('hello_world.wav', 'rb')
        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()
        print wf.getsampwidth()
        print wf.getnchannels()
        print wf.getframerate()
        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # read data
        data = wf.readframes(2000)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(2000)

        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()
