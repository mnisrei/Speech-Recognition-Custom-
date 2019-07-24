from pocketsphinx import LiveSpeech
import speech_recognition as sr
r = sr.Recognizer()
sample_rate = 44000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
while True:
        with sr.Microphone(sample_rate = sample_rate,chunk_size = chunk_size) as source:
                #wait for a second to let the recognizer adjust the  
                #energy threshold based on the surrounding noise level 
                r.adjust_for_ambient_noise(source) 
                print ("Say Something")
                #listens for the user's input 
                audio = r.listen(source)
        try:
                #Uses PhocketSphinx in speechrecognition 
                print(r.recognize_sphinx(audio,"jap"))
        except sr.UnknownValueError:
                print("Sphinx could not understand audio")
        except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

