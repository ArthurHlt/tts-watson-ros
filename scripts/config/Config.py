import yaml
import os
from utils.Singleton import Singleton


@Singleton
class Config:
    CONFIG_FILE = "../config.yml"

    def __init__(self):
    	currentDir = os.path.dirname(os.path.realpath(__file__))
        streamConfig = file(currentDir +"/../"+ self.CONFIG_FILE, 'r')
        self.yamlConfig = yaml.load(streamConfig)

    def getWatsonConfig(self):
        return self.yamlConfig["watson-tts"]

    def getAudioChunk(self):
        return self.yamlConfig["audio-chunk"]
