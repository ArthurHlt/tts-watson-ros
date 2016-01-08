import requests
from config.Config import Config


class TextToSpeechService:
    ACCEPT = 'audio/wav'

    """Wrapper on the Text to Speech service"""

    def __init__(self):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        """
        watsonConfig = Config.Instance().getWatsonConfig()

        # Local variables
        self.url = watsonConfig["url"]
        self.username = watsonConfig["user"]
        self.password = watsonConfig["password"]
        self.voice = watsonConfig["voice"]

    def synthesize(self, text):
        """
        Returns the get HTTP response by doing a GET to
        /v1/synthesize with text, voice, accept
        """

        return requests.get(self.url + "/v1/synthesize",
                            auth=(self.username, self.password),
                            params={'text': text, 'voice': self.voice, 'accept': self.ACCEPT},
                            stream=True, verify=False
                            )
