def prime_no(p_no):
    if 1 < p_no < 1000:
        for i in range(2, int(p_no / 2)):
            if p_no % i != 0:
                print("no is a prime no")
                return i+1
            else:
                print("no is not a prime_no")
                return i+1

    return p_no


prime_no(1777)
