''' 
Standard Producer/Consumer Threading Pattern
'''
import time
import threading
import Queue

class Consumer(threading.Thread):
    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self._queue = queue
        self._name = name
    def run(self):
        while True:
            # queue.get() blocks the current thread unitl an item is retrieved.
            msg = self._queue.get()
            # Checks if the current message is the 'Poison Pill'
            if isinstance(msg, str) and msg=='quit':
                # if so, exits the loop
                break
            # "Processes" (or in our case, prints) the queue item
            print "I'm a %s, and I receive %s!!" % (self._name, msg)
        # Always be friendly!
        print "Bye bye!"

def Producer():
    # Queue is used to share items between the threads.
    queue = Queue.Queue()
    # Create an instance of the worker 
    worker = Consumer(queue, 'worker')
    worker1 = Consumer(queue, 'another worker')
    # start calls the internal run() method to kick off the thread
    worker.start()
    worker1.start()
    # variable to keep track of when we started
    start_time = time.time()
    # While under 5 seconds
    while time.time() - start_time < 5:
        # "Produce" a piece of work and stick it in the quue for the Consumer to process
        queue.put('something at %s' % time.time())
        # Sleep a bit just to avoid an absurd number of messages
        time.sleep(1)
    # This the "poison pill" method of killing a thread
    queue.put('quit')
    queue.put('quit')
    # wait for th thread to close down
    worker1.join()
    worker.join()

if __name__ == '__main__':
    Producer()