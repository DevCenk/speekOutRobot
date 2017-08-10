#!/usr/bin/python 

import rospy
import pyaudio
import wave
from std_msgs.msg import String

class play_voice(object):

    def __init__(self):

        # define stream chuck
        self.chunk = 2048 
        
        # define the path of the wav files
        self.path_wel = "/home/cenk/Desktop/wel.wav"
        self.path_left = "/home/cenk/Desktop/left.wav"
        self.path_right = "/home/cenk/Desktop/right.wav"

        # init node
        rospy.init_node('voice_play')

        # play the welcome wav
        self.playfile(1, self.path_wel)

        while not rospy.is_shutdown():
            #self.wel = 0
            self.left = 0
            self.right = 0
            rospy.Subscriber('cmd', String, self.receive)
            
            #self.playfile(self.wel, self.path_wel)
            self.playfile(self.left, self.path_left)
            self.playfile(self.right, self.path_right)

    def playfile(self,flag,path):
        #play the wav file under the given path if the flag is 1 
        if flag == 0:
            return

        #open a wav format music  
        f1 = wave.open(path ,"rb")
    
        #instantiate PyAudio  
        p1 = pyaudio.PyAudio()

        #open stream  
        stream1 = p1.open(format = p1.get_format_from_width(f1.getsampwidth()),  
                        channels = f1.getnchannels(),  
                        rate = f1.getframerate(),  
                        output = True)  

        #read data
        data = f1.readframes(self.chunk)  
        
        #play stream  
        while len(data)>0:  
            stream1.write(data)  
            data = f1.readframes(self.chunk)
        
        #stop stream  
        stream1.stop_stream()  
        stream1.close()  
    
        #close PyAudio  
        p1.terminate()

    def receive(self,data):
        if data.data == 'left':
            self.left = 1
        if data.data == 'right':
            self.right = 1

if __name__ == "__main__":
    play_voice()
        
