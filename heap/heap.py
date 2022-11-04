import heapq
example = [4, 6, 7, 3, 5]
heapq.heapify(example)
# Print example
print(list(example))

example = []
# Push example
heapq.heappush(example, 5)
heapq.heappush(example, 3)
heapq.heappush(example, 1)
heapq.heappush(example, 6)

# Print example
print(list(example))

heapq.heappush(example, 5)
# printing modified heap
print("The modified heap after push is : ", end="")
print(list(example))
# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(example))

example = []
# Push example
heapq.heappush(example, 5)
heapq.heappush(example, 3)
heapq.heappush(example, 1)
heapq.heappush(example, 6)
print(list(example))

#Replace example
print(heapq.heapreplace(example,4))
print(list(example))

