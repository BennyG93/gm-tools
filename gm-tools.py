from webapp import app
from threading import Timer
import webbrowser

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    print("hello world")
    Timer(1, open_browser).start()
    app.run()
