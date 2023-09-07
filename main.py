from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

@app.route('/')
def home2():
    return render_template('index.css')

if __name__ == '__main__':
    app.run()


@app.route('/')
def song_input():
    song = str(input())
    return song

if __name__ == '__main__':
    app.run()

@app.route("/")
def hello():
    return "Hello World!"
#actually hosts the webserver
if __name__ == "__main__":
    app.run(host='0.0.0.0')