from Arduino import Arduino
from os import system
import time
system("sudo chmod 744 /dev/ttyACM0")
board = Arduino("9600",port="/dev/ttyACM0")
time.sleep(3)
board.digitalWrite(13,"LOW")
print "Desligada por 3 segundo"
print "Ligada por 6 segundos"
time.sleep(6)
board.digitalWrite(13, "HIGH")
board.digitalWrite (13,"LOW")
board.digitalWrite(13, "HIGH")
board.digitalWrite (13,"LOW")
