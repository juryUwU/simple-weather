
from datetime import datetime
from datetime import date
from matplotlib import cm
from time import sleep
import random
from rich.progress import track
import webbrowser
import datetime
import pyttsx3
import speech_recognition
from pyowm import OWM
import pyowm
from pyowm.utils import config
from pyowm.utils import timestamps
import pyautogui
import subprocess
import os
owm = OWM('023f8075107f72dd81cf7c25cdbc6e30')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Hanoi,VN')
w = observation.weather

w.detailed_status         
w.wind()                 
w.humidity               
w.temperature('celsius')  
w.rain                    
w.heat_index              
w.clouds       
print("\u001b[33mToday:\u001b[0m")
print(w.detailed_status)
print("\u001b[33mWind:\u001b[0m")
print(w.wind())
print("\u001b[33mhumidity\u001b[35m(%)\u001b[33m:\u001b[0m")
print(w.humidity)
print("\u001b[33mtemperature\u001b[35m(ºC)\u001b[33m:\u001b[0m")
print(w.temperature('celsius'))
print("\u001b[33mRain:\u001b[0m")
print(w.rain)
print("\u001b[33mheat index:\u001b[0m")
print(w.heat_index)
print("\u001b[33mcloud\u001b[35m(%)\u001b[33m:\u001b[0m")
print(w.clouds)
