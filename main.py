from matplotlib import image
from flask import Flask
app = Flask(__name__)

open(giesel.jpeg)
    

@app.route("/")
def hello():
   return "Hello World!"

#actually hosts the webserver
if __name__ == "__main__":
   app.run(host='0.0.0.0')