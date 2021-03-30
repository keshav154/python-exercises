#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio


from time import time
from pygame import mixer
from datetime import datetime

def musicloop(mp3file, stopper):
    mixer.init()
    mixer.music.load(mp3file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
def logger(msg):
    with open("logger.txt", "a") as t:
        t.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    eyessecs = 30*60
    exercisesecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("water drinking time enter drank to stop alarm")
            musicloop('water.ogg', 'drank')
            init_water = time()
            logger('Drank water at')

        if time() - init_eyes > eyessecs:
            print("eyes exercise time enter doneeyes to stop alarm")
            musicloop('eyes.ogg', 'doneeyes')
            init_eyes = time()
            logger('Did eyes exercise at')

        if time() - init_exercise > exercisesecs:
            print("Exercise time enter donephy to stop alarm")
            musicloop('physical.ogg', 'donephy')
            init_exercise = time()
            logger('physical exercise done at')
