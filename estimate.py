import math
import random
import unittest


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

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimation is not accurate enough.")
            
    def test_high_iters(self):
        for i in range(199, 300):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimation is accurate enough.")


class TestMonteCarlo(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(1001)
        pi1 = monte_carlo(1001)
        
        self.assertNotEqual(pi0, pi1, "Estimation was equal")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Estimation was different")

    def test_accuracy(self):
        for i in range(101, 201):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimation with high accuracy")
        


    
if __name__ == "__main__":
    unittest.main()

