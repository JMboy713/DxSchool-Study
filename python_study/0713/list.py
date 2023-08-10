from collections import deque

history=deque(maxlen=3)

data=[1,2,3,4]

for i in data:
    history.append(i)
print(history)