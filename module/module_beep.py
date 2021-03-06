import os
import subprocess
# Define path
file_path = os.path.abspath(__file__)

def beep(when):
    ###############
    #
    # use this module to make beep sound
    #
    # param >> when >> start or stop
    #
    # return >> None
    #
    ###############

    beep_wave = file_path.replace(
        'module/module_beep.py', 'beep/{}.wav').format(when)
    # beep_sound
    subprocess.call('aplay -q --quiet {}'.format(beep_wave), shell=True)

if __name__ == '__main__':
    beep("start")

