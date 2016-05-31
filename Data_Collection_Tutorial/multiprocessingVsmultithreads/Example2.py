'''
IBM tutorials on multi-threads for online data collection.
A more realistic thread pool example
'''

import time
import threading
import Queue
import urllib2

class Consumer(threading.Thread):
    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self._queue = queue
        self._name = name
    def run(self):
        while True:
            content = self._queue.get()
            if isinstance(content, str) and content == 'quit':
                break
            response = urllib2.urlopen(content)
        print '%s has done!' % self._name

def Producer(urls):
    if len(urls) < 1:
        print "No job need to do!"
        return
    queue = Queue.Queue()
    worker_threads = build_worker_pool(queue, 4)
    start_time = time.time()
    # Add the urls to process
    for url in urls:
        queue.put(url)
    # Add the poison pill
    for worker in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()
    print 'Done! Time taken: {}'.format(time.time() - start_time)

def build_worker_pool(queue, size):
    workers = []
    for id in range(size):
        worker = Consumer(queue, str(id))
        worker.start()
        workers.append(worker)
    return workers

if __name__ == "__main__":
    urls = [
        "http://www.python.org", "http://www.yahoo.com",
        "http://www.scala.org", "http://www.google.com"
    ]
    Producer(urls)