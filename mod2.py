def sum1(l):
    j = 0
    for i in l:
        j = j + i
    return j
def sum2(l):
    j = 0
    return l[0]*2 + l[1]/2. + l[2] + l[3] + l[4]**2
def main(n):
    l = [0,0,0,0,0]
    for i1 in range(1,n):
        for i2 in range(1,n):
            for i3 in range(1,n):
                for i4 in range(1,n):
                    for i5 in range(2,n):
                        l = [i1,i2,i3,i4,i5]
                        if sum1(l) == sum2(l):
                            print l
