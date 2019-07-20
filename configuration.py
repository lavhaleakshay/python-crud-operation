from os import environ as env
import multiprocessing

#pass a port number on which user wants to run his application
PORT = env.get("SERVE_PORT")
if PORT == None:
    print ("Environment variable not found")
    raise SystemExit("Environment port not defined please set SERVER_PORT environment variable")
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()



