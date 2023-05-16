def integrate_c(double a, double b, int N) -> double :
    cdef double s = 0
    cdef int i
    cdef double dx = (b-a) /N
    for i in range(N):
        s += 2.71828182846**(-(a+i*dx)**2)
    return s*dx