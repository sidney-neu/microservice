import multiprocessing
import gevent.monkey
gevent.monkey.patch_all()

bind = '0.0.0.0:5000' 
workers = 4 # multiprocessing.cpu_count() # * 2  + 1
worker_class = 'gevent'
preload_app = True
reload = False