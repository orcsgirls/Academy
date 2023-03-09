import json
from os import path, getuid
from flask import Flask, request, jsonify, send_from_directory
from aiy.voice.audio import play_wav
from aiy.leds import Leds, Color
import os
import subprocess
import tempfile
import glob

SOUND_FOLDER = "Sounds/"

app = Flask(__name__)
leds = Leds()

#--- Helpers ----------------------------------------------------
RUN_DIR = '/run/user/%d' % getuid()

def say(text, lang='en-GB', volume=60, pitch=130, speed=100, device='default'):
    data = "<volume level='%d'><pitch level='%d'><speed level='%d'>%s</speed></pitch></volume>" % \
           (volume, pitch, speed, text)
    
    with tempfile.NamedTemporaryFile(suffix='.wav', dir=RUN_DIR) as f:
        cmd = 'pico2wave --wave %s --lang %s "%s" && aplay -q -D %s %s' % \
             (f.name, lang, data, device, f.name)
        subprocess.check_call(cmd, shell=True)

#--- Helper page ------------------------------------------------

@app.route('/')
def index():
    return send_from_directory('Static', 'index.html')

#--- PLay sound file --------------------------------------------

@app.route('/play', methods=['GET'])
def play_sound():
    value = request.args.get('value')
    file = path.join(SOUND_FOLDER,value+'.wav')
    if path.exists(file):
        play_wav(file)
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'sound not found'})

#--- Control button led -----------------------------------------

@app.route('/led', methods=['GET'])
def control_led():
    value = request.args.get('value')
    if value == 'red':
        leds.update(Leds.rgb_on(Color.RED))
    elif value == 'green':
        leds.update(Leds.rgb_on(Color.GREEN))
    elif value == 'blue':
        leds.update(Leds.rgb_on(Color.BLUE))
    elif value == 'off':
        leds.update(Leds.rgb_off())
    else:
        return jsonify({'status': 'invalid value'})
    
    return jsonify({'status': 'ok'})

#--- Say given text ----------------------------------------------

@app.route('/say', methods=['GET'])
def do_speak():
    value = request.args.get('value')
    pitch = request.args.get('pitch')
    if(value):
        if(pitch):
            say(value, pitch=int(pitch))
        else:
            say(value)
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'error': 'missing parameter'})

#--- List available sound files ----------------------------------

@app.route('/list', methods=['GET'])
def list_sounds():
    sounds = glob.glob(path.join(SOUND_FOLDER,'*.wav'))
    if(len(sounds)>0):
        return jsonify([{'sound': os.path.basename(s)} for s in sounds])
    else:
        return jsonify({'error': 'no sounds found'})
    
#--------------------------------------------------------------
app.run(host='0.0.0.0', port=5000)
