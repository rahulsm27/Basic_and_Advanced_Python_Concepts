import logging

def init():
    print("this is init")

logging.basicConfig(filename = "test1.log" , level = logging.DEBUG, format = "%(asctime)s %(name)s %(levelname)s %(message)s")

def get_logger(name : str) -> logging.Logger :
    return logging.getLogger(name)


