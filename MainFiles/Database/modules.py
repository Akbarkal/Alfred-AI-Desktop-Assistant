####------------------------------- All Modules Used ------------------------------

################################### Import Modules ##################################

try:
    from pywikihow import search_wikihow
    from pywhatkit.core import exceptions
    from pytube import YouTube
    from PIL import Image
    from winotify import Notification, audio
    from bs4 import BeautifulSoup
    from googletrans import Translator
    from playsound import playsound
    from gtts import gTTS
    from currency_converter import CurrencyConverter
    from bing_image_downloader import downloader
    from face_recognition_models import *
    from urllib import request
    import face_recognition
    import cv2
    import numpy as np
    import dlib
    import speech_recognition as sr
    import pywhatkit as kit
    import time as t
    import screen_brightness_control as pct
    import win32gui
    import smtplib
    import requests
    import webbrowser
    import pyautogui
    import datetime
    import math
    import json
    import random
    import wikipedia
    import pyjokes
    import psutil
    import pickle
    import os
    import subprocess
    from tuyapy import TuyaApi
    import sys
    import pyttsx3
    import pytz
    import threading
    import winshell

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',180)

    
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

except Exception as e: 
    import sys
    import pyttsx3
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',180)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait() 

    print("Alfred Not Available\n")
    speak("Alfred Not Available")
    print("Please connect to internet...")
    speak("please connect to internet. or check network connection")
    sys.exit()

####------------------------------- End -------------------------------------------