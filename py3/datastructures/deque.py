from collections import deque

queue = deque(["John", "Jim"])
print(queue)


# also append will push the element at the end
queue.append('Allen')
print(queue)


# will remove the first element like {shift}
queue.popleft()
print(queue)

# will pop the last element of the queue
queue.pop()
print(queue)



