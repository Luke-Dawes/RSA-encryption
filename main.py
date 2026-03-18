from math import lcm, gcd, ceil, sqrt
from random import randint

def findPrime() -> int:
    with open("primeNums.txt") as f:
        text = f.read().split()
        num1 = randint(0,len(text))
        num2 = randint(0,len(text))
        if num1 == num2:
            print("error")
        return int(text[num1]), int(text[num2])

def findN(a, b):
    return a*b

def findToitient(a, b):
    return lcm(a-1,b-1)

p, q = findPrime()
n = findN(p, q)
totient = findToitient(p,q)

E = 1
while True:
    E += 2
    if gcd(E, totient) == 1:
        break

D = pow(E, -1, totient) #may be -2


def encrypt(text: str, e: int, n: int): #n = MOD
    newText = []
    for i in text:
        temp = ord(i)
        temp = pow(temp, e, n)
        newText.append(temp)
    return newText

def decrypt(text: list[int], d: int, n: int):
    newText = ""
    for i in text:
        newText += chr(pow(i, d, n))
    return newText

text = "hello does this work and does this get slower when i add more things beacuse it should however, it may not be noticeable "
encrypted = encrypt(text, E, n)
testingText = decrypt(encrypted, D, n)
print(f"prime1 = {p}\nprime2 = {q}\nn = {n}\ntotient = {totient}\nE = {E}\nD = {D}\nbase Text = {text}\nencrypted = {encrypted}\ndecrypted text = {testingText}")


def worseBruteForce(encrypted: list[int], n: int):
    #very very bad
    for potentialD in range(127,10000000000000000000000000000):
        valid = True
        for i in encrypted:
            temp = pow(i,potentialD,n)
            if temp > 127:
                valid = False
                break
        
        if valid:
            print(f"possible values of d are: {potentialD}")

def bruteForceWithMaths(encrypted: list[int], n: int):
    with open("primeNums.txt") as f:
        primeNumbers = f.read().split()
    numberPrimeNumbers = [int(x) for x in primeNumbers]
    print("done --- below this is the brute force attempt at finding p and q")
    highestVal = ceil(sqrt(n))
    num1 = 0
    for nums in numberPrimeNumbers:
        if nums > highestVal:
            print("error")
        if n % nums == 0 and nums != n:
            print(f"smaller number is: {nums}")
            num1 = nums
            break
    
    num2 = n // num1

    print(f"numbers are {num1}, {num2}")

bruteForceWithMaths(encrypted, n)