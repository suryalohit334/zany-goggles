from flask import Flask, render_template
import requests
import time
import logging
import sys
logging.basicConfig(
     filename='log_file_name.log',
     level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)


TOKEN = "6994416717:AAH_qEF1vSy1gZc1nXQ4eyM4dErJshFGJaM"
chat_id = "998041732"
app = Flask(__name__)

@app.route("/")
def hello_world():
    for i in range(1000):
        logging.debug('debug')
        logging.info('info')
        logging.warning('warning')
        logging.error('error')
        logging.exception('exp')
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


