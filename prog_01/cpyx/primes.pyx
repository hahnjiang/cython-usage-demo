from libcpp.vector cimport vector

def primes(int nb_primes):
    cdef int n, i, len_p
    cdef vector[int] p
    p.reserve(nb_primes)

    n = 2
    while p.size() < nb_primes:
        # Is n prime?
        for i in p[:len_p]:
            if n % i == 0:
                break

        # If no break occurred in the loop, we have a prime.
        else:
            p.push_back(n)
        n += 1

    return p
