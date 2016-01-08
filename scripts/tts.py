#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from tts_watson.PlayerTts import PlayerTts

class TtsWatson:
	def __init__(self):
		self.playerTts = PlayerTts()
	def playSound(self, data):
		self.playerTts.play(data.data)

def listen():
	ttsWatson = TtsWatson()
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("text_to_speech", String, ttsWatson.playSound)
	print 'Ready to transform text into sound'
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
if __name__ == '__main__':
    listen()
    