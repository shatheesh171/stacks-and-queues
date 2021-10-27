from multiprocessing import Queue

cq=Queue(maxsize=3)
cq.put(1)
cq.put(2)
print(cq.qsize())
print(cq.get())