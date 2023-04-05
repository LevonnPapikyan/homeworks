# exersice one
def triangle(size,symbol = "#"):
    l = []
    for i in range(1,size+1):
        l.append([symbol] * i)
    print(l,sep = '\n')

# exercise two
def find_gcd_(*numbers):
    l = list(numbers)
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    num1=l[0]
    num2=l[1]
    gcd=find_gcd(num1,num2)
   
    for i in range(2,len(l)):
        gcd=find_gcd(gcd,l[i])
    return gcd

#exercise three
counter = 0
def fib(n):
    global counter
    counter += 1
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(10))
print(counter)

#exercise 4
def prime_factors(num):
    if num<1:
        raise "input needs positive number"
    if num==1:
        return 1
    def check_prime(number):
        for i in range(2, int(number/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (number % i) == 0:
                return False
        else:
                 return True
        
    prime_list = []
    for i in range(2,num+1):
       if check_prime(i):
           if num%i==0:
               prime_list.append(i)
    return prime_list

#exercise 5
def jumping_frog(height_of_pipes, max_jump):
   fails = False
   while len(height_of_pipes)!=2:
    
        if abs(height_of_pipes[-1] - height_of_pipes[-2]) > max_jump:
           fails = True
           break
        else:
           height_of_pipes.pop(-1)
   if fails == True:
        return "Game over"
   elif  abs(height_of_pipes[-1] - height_of_pipes[-2]) > max_jump:
        return "Game over"
   else: return "Frog wins"

   print(12)