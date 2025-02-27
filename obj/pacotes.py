import math

num=127

def numPrimo(num):
    if(num%2)==0:
        return "não é primo"
    for i in range(3, int(math.sqrt(num))+1,2):
        print(i)
        if(num%i)==0:
            return "nâo é primo"
    return "è primo"

print(numPrimo(71))
