from flask import Flask 
  
app = Flask(__name__) 

@app.route('/') 
def start(): 
    return 'This app was lauched at startup'
  
if __name__ == '__main__': 
    app.run(host='0.0.0.0') 
