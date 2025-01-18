n = 1234

# Most used Traditional method : TC - O(m) where  m = len(n) , SC - O(1) 
def f1(n):
    while n > 9:
        digit_sum = 0
        while n:
            digit_sum += n % 10
            n //= 10
        n = digit_sum
    return n

# Beginner friendly simpler method : TC - O(m) where  m = len(n) , SC - O(1) 
def f2(n):
    while n > 9:
        n = sum(int(i) for i in str(n))
    return n
    

print(f1(n))
print(f2(n))
    
