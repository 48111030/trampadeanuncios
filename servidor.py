from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/ejecutar')
def ejecutar():
    subprocess.Popen(['python', 'scriptlikeo.py'])
    return 'Script ejecutado correctamente desde el botón'

app.run()
