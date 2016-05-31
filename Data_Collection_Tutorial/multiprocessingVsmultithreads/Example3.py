'''
Improve the parallel working using multiprocessing module and its map()
Good for CPU-intensive work
'''
import time
import urllib2
from multiprocessing.dummy import Pool as ThreadPool # multi-threading not multi-processing
urls = [
    "http://www.python.org",
    "http://www.python.org/about/",
    "http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html",
    "http://www.python.org/doc/",
    "http://www.python.org/download/",
    "http://www.python.org/getit/",
    "http://www.python.org/community/",
    "https://wiki.python.org/moin/",
    "http://planet.python.org/",
    "https://wiki.python.org/moin/LocalUserGroups",
    "http://www.python.org/psf/",
    "http://docs.python.org/devguide/",
    "http://www.python.org/community/awards/"
    # etc..
    ]
def work_load(url):
    response = urllib2.urlopen(url)
    print response.info()
    return response
# Make the Pool of workers
start_time = time.time()
pool = ThreadPool() # default value is equal to the number of cores
# Open the urls in thier own threads and return results
#results = pool.map(urllib2.urlopen, urls)
results = pool.map(work_load, urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()
print "Total time: " + str(time.time() - start_time)