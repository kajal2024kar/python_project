#this code count all the digit fron 1 to th given number
def digitcount(num:int):
    count = 0
    for n in range(1,num+1):
        for c in range(len(str(n))):
            count +=1
    return count

n = int(input("enter a number:"))
print(digitcount(n))