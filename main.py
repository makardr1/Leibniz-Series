
# Pi_approximation

# In mathematics, the Leibniz formula for π, named after Gregory-Leibniz.

# the Gregory-Leibniz series: 4/1 - 4/3 + 4/5 - 4/7

from math import *

def Leibniz_Series():
    print("Welcome to Pi approximation!\n")
    n = int(input("Enter the number of terms to sum: "))
    approx = 0
    sign = - 1

    # Start Gregory-Leibniz series

    # Счётчик
    for i in range(1, n + 1):
        sign *= - 1
        approx += sign * (4 / (2 * i - 1))

    # End Gregory-Leibniz series

    print("Approximate value of pi is:", approx)

Leibniz_Series()