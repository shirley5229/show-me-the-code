arr=[2,4,1,8,7,6,5,11,3]

def insertSort(arr):
    count=len(arr)
    for i in range(1,count):
        #i表示从位置1开始向右遍历，第一个元素位置0是已排序好的
        print('i:'+str(i))
        for j in range(i,0,-1):
            #j代表当前已排序的数字的结束位置
            print('j:'+str(j))
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]

    return arr

if __name__=="__main__":
    print(insertSort(arr))
