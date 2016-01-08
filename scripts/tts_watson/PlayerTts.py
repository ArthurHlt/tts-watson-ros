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
        print "Transform '"+ str(text) +"' into sound"
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
        print "Text: '"+ str(text) +"' has been transformed !"

