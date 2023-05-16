import time
import calc
from numba import jit


@jit
def integrate_j(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += 2.71828182846**(-(a + i * dx)**2)
    return s * dx


def integrate_f(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += 2.71828182846**(-(a + i * dx)**2)
    return s * dx


'''
0.13940280918664258
19.242555141448975
0.13940280918664258
2.4434239864349365
0.13940280918664258
1.8654460906982422
'''
if __name__ == "__main__":
    st = time.time()
    print(integrate_f(1.0, 10.0, 100000000))
    en = time.time()
    print(en - st)

    st = time.time()
    print(integrate_j(1.0, 10.0, 100000000))
    en = time.time()
    print(en - st)

    st = time.time()
    print(calc.integrate_c(1.0, 10.0, 100000000))
    en = time.time()
    print(en - st)
