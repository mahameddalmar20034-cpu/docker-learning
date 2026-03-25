

from flask import Flask
from redis import Redis
import os
app = Flask(__name__)

redis_client = Redis(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')))
@app.route('/')
def hello_world():
    return 'CoderCo Containers Session!'
@app.route('/count')
def read_count():
   count=redis_client.incr('visits')
   return f'Number of visits: {count}' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)