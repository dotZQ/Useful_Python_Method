'''
def ipow(a,n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * a
            n -= 1
        n = n//2
        a *= a
    return result
'''
def powRe(a,n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n%2 == 1:
        return a*powRe(a,n-1)
    total = powRe(a,n//2)
    return total**2

print(powRe(2,100))