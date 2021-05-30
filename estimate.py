import random


def wallis(n):
    t=n+1
    pi=1
    for i in range(1,t):
         pi *= (((4*(i**2)))/((4*(i**2))-1))
    pi *= 2
    return pi

def monte_carlo(n):
    c = 0
    tc = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        distance = ((x**2)+(y**2))**(1/2)
        if distance < 1:
            c += 1
            tc += 1
        else:
            tc += 1
    pi=(4*(c/tc))
    return pi

