from flask import Flask, Response
from flask_cors import CORS
from flask_sse import sse
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__,  static_url_path='', static_folder='static')
cors = CORS(app)

def get_message():
    '''this could be any function that blocks until data is ready'''
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message())
    return Response(event_stream(), mimetype="text/event-stream")

# sched = BackgroundScheduler(daemon=True)
# sched.add_job(event_stream,'interval',seconds=1)
# sched.start()

if __name__ == '__main__':
    app.run(debug=True, port=80, threaded=True)