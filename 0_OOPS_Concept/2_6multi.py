import multiprocessing
def test():
    print("this is my multiprocessing prog")

if __name__ == "__main__": # main process
    m = multiprocessing.Process(target = test)
    print("this is my main programme")
    m.start()
    m.join()