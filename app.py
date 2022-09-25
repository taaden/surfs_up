
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/welcome') 

def welcome():
    return 'aloha'

@app.route('/rains') 
def rain():
    return 'Precipitation'

@app.route('/station') 
def stations():
    return 'Stations'

@app.route('/12') 
def monthly_temps():
    return 'Monthly Temp'

@app.route('/stats')
def statistics():
    return 'Statistics'

if __name__ =="__main__":
    app.run(debug= True)