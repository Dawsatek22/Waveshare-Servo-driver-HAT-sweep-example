#NL:deze code is voor de Waveshare ServoDriver HAT met een raspberry pi zero W board.
#ENG:this code is forWaveshare Servo Driver HAT with a raspberry pi zero W board.
#NL:er is zijn links voor software aan de einde van de code.
#ENG: there are links for the software at the end of the code.


import time #NL: deze module importeert de tijd.ENG: this module import the time.

from adafruit_servokit import ServoKit #NL: deze code gebruikt de adafruit_servokit servo module .ENG: this code use the Adafruit_Servokit module
kit = ServoKit(channels=16) #NL: activeert 1 kanaal. #ENG: activates 1 channel
while True: # NL: gaat in een loop.ENG:goes in a loop
    kit.servo[0].angle = 180 #NL: servo maakt een 180 graden hoek .ENG: servo makes 180 degrees angle
    time.sleep(1) #NL: tijd vertraagt 1 seconde. ENG: time slows 1 second.
    kit.servo[0].angle = 0 #NL: servo maakt een 0 graden hoek.ENG:servo makes a 0 degrees angle
    time.sleep(1) #NL: tijd vertraagt 1 seconde. ENG: time slows 1 second.
#NL:link for more info of the Servo hat at: https://www.waveshare.com/wiki/Servo_Driver_HAT
#ENG: link  voor meer info over de Servo hat in: https://www.waveshare.com/wiki/Servo_Driver_HAT   

