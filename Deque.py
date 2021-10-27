from collections import deque

cq=deque(maxlen=3)

cq.append(1)
cq.append(2)
cq.append(3)
cq.append(4)
cq.popleft()
#cq.clear()
print(cq)