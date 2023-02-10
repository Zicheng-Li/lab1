
import math
import random
import timeit
import matplotlib.pyplot as plot

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# *************************************


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s


    

# Experiment 4
def exp4(n,m):
    quick_times=[]
    merge_times=[]
    heap_times=[]
    for i in range(n):
        L=create_random_list(i,m)
        L2 = L.copy()
        L3 = L.copy()
        start= timeit.default_timer()
        quicksort(L)
        end=timeit.default_timer()
        quick_times.append(end-start)
        
        start= timeit.default_timer()
        mergesort(L2)
        end=timeit.default_timer()
        merge_times.append(end-start)
        
        start= timeit.default_timer()
        heapsort(L3)
        end=timeit.default_timer()
        heap_times.append(end-start)
    print("The quickion sort time is ")
    print(quick_times)    
    print("The merge sort time is " )   
    print(merge_times)    
    print("The heapion sort time is ")    
    print(heap_times)
    return quick_times, merge_times, heap_times

# Experiment 7 bottom_up_mergesort code
def bottom_up_mergesort(L):
    length=len(L)
    if(length<=2):                  #This is the edge case when list is smaller than 2
        if(length<2):
            return L
        else:
            if(L[0]>L[1]):
                L[0],L[1]=L[1],L[0]
            return L
    i=2
    while(i<length):                #This loop will track the number of window size
        j=i//2
        w=i
        while(j<=length):           #This loop will split the part of list into right and left
            left=L[w-i:j]
            right=L[j:min(w,length)]    #j is the mid point
            temp = merge(left, right)

            L[w-i:min(w,length)]=temp
            j=j+i
            d=j-length
            if(0<d<(i//2)):              #This is in case the last part of list is samller than mid point j
                left=L[w:w+d]
                right=L[w+d:]
                temp = merge(left, right)
                L[w:length]=temp
            w=w+i
    
        i=i*2
    if(i>=length):                       #This is to sort the whole list one last time
        l=length-len(temp)
        left=L[:l]
        right=L[l:]
        temp = merge(left, right)

        L=temp
    return L

L2=[-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,-87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,-6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,-69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,92,52,-45,-2,85,-63,56,55,12,-85,77,-39]
print(bottom_up_mergesort(L2))

# Experiment 7 for testing
def exp7(n,m):
    topmerge=[]
    bottomerge=[]
    for i in range(n):
        L=create_random_list(i,m)
        L2 = L.copy()
        start= timeit.default_timer()
        mergesort(L)
        end=timeit.default_timer()
        topmerge.append(end-start)
        
        start= timeit.default_timer()
        bottom_up_mergesort(L2)
        end=timeit.default_timer()
        bottomerge.append(end-start)
    return topmerge, bottomerge



# ******************* run exp4 and exp7 *******************
# out,out1,out2 = exp4(1000,100)
# plot.plot(out2,label="heap")
# plot.plot(out1, label="merge")
# plot.plot(out, label="quick")
# plot.xlabel("list length")
# plot.ylabel("time")
# plot.legend()
# plot.show()

# out,out1 = exp7(3000,100)
# plot.plot(out1, label="bottom_up_merge")
# plot.plot(out, label="top_down_merge")
# plot.xlabel("list length")
# plot.ylabel("time")
# plot.legend()
# plot.show()