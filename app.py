from flask import Flask

from escpos.printer import Network

kitchen = Network("192.168.1.100") #Printer IP Address
kitchen.text("Hello World\n")
kitchen.barcode('1324354657687', 'EAN13', 64, 2, '', '')
kitchen.cut()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"