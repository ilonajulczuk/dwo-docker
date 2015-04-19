import os
from flask import Flask
from redis import Redis


app = Flask(__name__)
redis_host = os.environ.get("REDIS_PORT_6379_TCP_ADDR", None)

if redis_host:
    redis = Redis(host=redis_host, port=6379)
else:
    redis = None


@app.route('/')
def hello():
    if redis:
        redis.incr('views')
        return (
            '<p>Hello DWO2015! This page has been seen {0} times.<p>'
            '<img src="http://imworld.aufeminin.com/story/20140424/cat-meme-219389_w1000.jpg">').format(
            int(redis.get('views')))
    else:
        return (
            '<p>Hello DWO2015! - still work in progress.</p>'
            '<img src="http://images6.fanpop.com/image/photos/33200000/meme-cats-33292012-500-360.jpg">')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
