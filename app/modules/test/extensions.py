from flask_caching import Cache
import time

cache = Cache()

# count time wrap func
# used for testing
def timecount(func):

    def wrapped(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("\ntime: ", (end-start)*1000 // 1, "ms")

    return wrapped