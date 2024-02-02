import model # will import the _init_ details
from model import get_logger

def run_task():
    log = get_logger(__file__)
    model.init()
    log.info("this is")

    from model import src

    src.src()

if __name__ == "__main__":
    run_task()


