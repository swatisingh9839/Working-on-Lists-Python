import math 

def smooth_a(a,n):
    denominator = 2*n + 1
    newlist = []
    for i in range(0,len(a)):
        minC = countMinInd(i,n)
        #print(minC, '\n')
        maxC = countMaxInd(i,n,len(a))
        #print(maxC,'\n')
        #print(a[max(i-n,0)])
        #print(a[min(i+n+1,len(a))])
        newVal = sum(a[max(i-n,0):min(i+n+1,len(a))]) + (a[0]*minC) + (a[-1]*maxC)
        
        #print(newVal)
        newlist.append(newVal/denominator)
    return newlist

def countMaxInd(i,n,length):
    count = 0
    startVal = i+n
    while startVal >= length:
        count += 1
        startVal -= 1
    return count

def countMinInd(i,n):
    count = 0
    startVal = i-n
    while startVal < 0:
        count += 1
        startVal += 1
    return count    

def smooth_b(a,n):
    newList = []
    for i in range(0,len(a)):
        minIndex = max(i-n,0)
        maxIndex = min(i+n+1,len(a))
        ct = maxIndex - minIndex
        newVal = sum(a[minIndex:maxIndex])
        newList.append(newVal/ct)
    return newList

def calc_mean(lis):
    return sum(lis)/len(lis)

def round_list(a_list,ndigits):
    new_a_list = [round(elem,ndigits) for elem in a_list]
    return new_a_list

x = [1, 2, 6, 4, 5, 0, 1 ,2]
print('smooth_a(x, 1):',smooth_a(x, 1))
print('smooth_a(x, 2):',smooth_a(x, 2))
print('smooth_b(x, 1):',smooth_b(x, 1))
print('smooth_b(x, 2):',smooth_b(x, 2))

print('smooth_a(x, 1) rounded: ',round_list(smooth_a(x, 1), 2))


    
