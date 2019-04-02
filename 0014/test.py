
arr=[2,4,1,8,7,6,5]

def bubbleSort(arr):
    count=len(arr)
    for i in range(count):
        #print('i:'+str(i))
        # i 就是当前排序好的元素个数，从0开始，表示排序完成0到n个
        for j in range(count-i-1): 
            #print('j:'+str(j))
            #每次循环的结束点都是比较当前未排序元素的倒数第2个和最后1个
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

if __name__=="__main__":
    print(bubbleSort(arr))
