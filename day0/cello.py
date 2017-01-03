## Play audio (.mp3 files of Bach Cello)
 # Music source:
# How to Play Audio: http://stackoverflow.com/questions/260738/play-audio-with-python/34179010#34179010
## using these steps on my Mac works - not tested on any other OS (linux, win, etc.)
 # import subprocess
 # subprocess.call(["afplay", "path/to/audio/file"])

import glob
import random
import subprocess
import time

base_folder = "/Users/fungineer/100-days-of-code/day0/bach_cello_mp3s/"
file_type = ".mp3"

glob_path = base_folder+'*'+file_type  # make a list of all mp3s in base_folder

mp3_list = glob.glob(glob_path)

def play_audio(song_file):
    # this function just plays an audio file
    subprocess.call(["afplay", song_file])

def get_random_file(file_list):
    return random.choice(file_list)

# def play_for_time(timer):
#     """This function could keep trying to play songs for the amount of time set."""


# other ideas for an audio player
# get length of sound file (based on size and hertz?)


play_audio(get_random_file(mp3_list))

## glob documentation
 # https://docs.python.org/2/library/glob.html