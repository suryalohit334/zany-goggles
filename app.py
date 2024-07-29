from flask import Flask, render_template
import requests
import time
import logging
 
# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
 
# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")

TOKEN = "6994416717:AAH_qEF1vSy1gZc1nXQ4eyM4dErJshFGJaM"
chat_id = "998041732"
app = Flask(__name__)

@app.route("/")
def hello_world():
    for i in range(1000):
        print("output")
        message=f"run::{i}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)
        time.sleep(58)
    return render_template("index.html", title="Hello")



@app.route("/test")
def hello_world1():
    message=f"test1"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url) 
    mess="SAMPLE_TEST"
    return    mess


if __name__ == "__main__":
    app.run(debug=True)


