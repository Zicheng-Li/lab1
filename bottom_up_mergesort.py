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
