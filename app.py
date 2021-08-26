from rq import Queue
from worker import conn
from utils import count_words_at_url
from flask import Flask
import time
app = Flask(__name__)
@app.route("/task/<tokens>")
def index(tokens):
    q = Queue(connection=conn)
    result = q.enqueue(count_words_at_url, 'http://heroku.com')
    return succ




if  __name__ == "__main__": 
    app.run(threaded=True, port=5000,debug=True)
