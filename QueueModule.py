import queue as q

cq=q.Queue(maxsize=3)
print(cq.qsize())
cq.put(1)
cq.put(2)
cq.put(3)
cq.get()
print(cq.qsize())