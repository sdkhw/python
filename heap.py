class heap():
    
    def __init__():
        pass
    

class MinHeap:
    def __init__(self, data=None):
        self.heap = data[:] if data else []
        self.size = len(self.heap)


    # def _build_heap(self):
    #     # 마지막 부모 노드부터 내려가며 heapify 수행
    #     for i in range((self.size // 2) - 1, -1, -1):
    #         self._heapify_down(i)
            
    def peek(self):
        return self.heap[0]
    

    def add(self, n):
        self.heap.append(n)
        self.size += 1
        idx = len(self.heap) -1 # 마지막 원소 인덱스

        while True:
            if self.heap[idx] < self.heap[idx // 2]:
                self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx] 
                # 말단 노드값이 더 작으면 노드값 바꿈 
                idx = idx//2
            else: break

    def remove(self):
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.size = len(self.heap)
        idx = 1 
        while True:
            if self.heap[idx] > self.heap[idx*2] or self.heap[idx] > self.heap[idx*2 +1]:
                
            pass


    def show(self):
        print(self.heap)


nums = [0,2,4,3,5, 7, 9]

minheap = MinHeap(nums)
minheap.show()

print(minheap)
# minheap.heapify(1)
minheap.heapify(10)
minheap.show()

print( 2// 3 )



# nums[2], nums[3] = nums[3], nums[2]
# print(nums)