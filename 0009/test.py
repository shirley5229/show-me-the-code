#coding='utf-8'

def getnum(a,b):
    r=a%b
    if r==0:
        return b
    else:
        a,b=b,r
        return getnum(a,b)

if __name__=="__main__":
    a,b=input().split(',')
    a,b=int(a),int(b)
    min= b if a>b else a
    print(min)
    #a,b=lambda a<b:b,a
    n=getnum(a,b)  
    print(n)
