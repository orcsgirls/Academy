import json
from flask import Flask, request, jsonify
from playsound import playsound
from os import path

app = Flask(__name__)

@app.route('/play', methods=['GET'])
def play_sound():
    name = request.args.get('name')
    file = path.join('Sounds',name+'.wav')
    if path.exists(file):
        playsound(file)
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'sound not found'})
    
#--------------------------------------------------------------
app.run()