from decimal import *
import math

getcontext().prec = 60

def main():
    left = 345931597484997194738850308051392249857;
    right = 345931597484997194738850308052682194945;
    b = 443426488243037769948249630619149892803;

    l = (Decimal(left)/Decimal(b))
    r = (Decimal(right)/Decimal(b))

    print(l)
    print("----")
    print(r)
    print("----")

    diff = r-l
    print(diff)
    print("---")

    print(math.log(diff, 2) * -1)

    power = 98
    print("----")
    print(l*2**power)
    print("----")
    print(r*2**power)


    print("----")
    print(bin(247233988505789350519350844136)[2:])


if __name__ == "__main__":
    main()
