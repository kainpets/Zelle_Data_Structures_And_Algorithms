# time_search.py
import time

def search(items, target):
    try:
        return items.index(target)
    except ValueError:
        return -1

items = range(1000000) # create a big list

start = time.time()
search(items, 999999) # look for the last item
stop = time.time()
print(stop - start)

start = time.time()
search(items, 499999) # look for the middle item
stop = time.time()
print(stop - start)

start = time.time()
search(items, 10) # look for an item near the front
stop = time.time()
print(stop- start)