#calculator.py
def sum(m,n): #requirement specification: sum must perform n increments to the value of m and return the result.
    for _ in range(abs(n)):
        if n>0:
            m+=1
        else:
            m-=1
    return m

def divide(m,n):
    if n==0: return
    result=0;
    if n<0 and m<0: return divide(-m,-n)
    elif n<0: return -divide(m,-n)
    elif m<0: return -divide(-m,n)
    while m>0:
        m-=n
        result+=1
    return result
