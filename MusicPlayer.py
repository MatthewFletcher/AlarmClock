from threading import Thread

def loopA():
    for i in range(100):
        #Sample Task
def loopB():
    for i in range(100):
        #Sample Task B

threadA = Thread(target = loopA)
threadB = Thread(target = loopB)


threadA.run()
thradB.run()

#Do work independently of loopA and loopB

threadA.join()
threadB.join()
