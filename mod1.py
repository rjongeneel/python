def createListQuadrats(n):
    l = []
    i = 0
    while i<=n:
        i = i + 1
        l.append(i*i)
    return l

def createListTriangle(n):
    l, k = [], 0
    i = 0
    while i<=n:
        i = i + 1
        k = k + i
        l.append(k)
    return l

def checkList(x,l):
    return l.count(x)

def createList(l,size):
    k = []
    for i in l:
        if len(str(i)) == size:
            k.append(i)
    return k

def displayResult(l):
    print str(l[0])
    print str(l[1])
    print ' ' + str(l[2])
    print '  ' + str(l[3])
    print '   ' + str(l[4])
    print '    ' + str(l[5])
    print '     ' + str(l[6])
    print '      ' +str(l[7])

def displayCount(l):
    for i in range(8):
        print i+1, l.count(i+1)

def main():
    l1 = createListQuadrats(98)
    l2 = createListTriangle(139)
    l=[0,0,0,0,0,0,0,0]
    x=range(9)
    y=range(28)
    for i0 in createList(l2,3):
        l[0] = i0
        for i1 in createList(l2,4):
            l[1] = i1
            x[0] = int(str(l[0])[0]+str(l[1])[0])
            if checkList(x[0],l1) == 1:
                for i2 in createList(l2,4):
                    l[2] = i2
                    y[0] = int(str(l[0])[0])
                    y[1] = int(str(l[0])[1])
                    y[2] = int(str(l[0])[2])
                    y[3] = int(str(l[1])[0])
                    y[4] = int(str(l[1])[1])
                    y[5] = int(str(l[1])[2])
                    y[6] = int(str(l[1])[3])
                    y[7] = int(str(l[2])[0])
                    y[8] = int(str(l[2])[1])
                    y[9] = int(str(l[2])[2])
                    y[10] = int(str(l[2])[3])
                    x[1] = int(str(l[0])[1]+str(l[1])[1]+str(l[2])[0])
                    if checkList(x[1],l1) == 1:
                        for i3 in createList(l2,4):
                            l[3] = i3
                            y[11] = int(str(l[3])[0])
                            y[12] = int(str(l[3])[1])
                            y[13] = int(str(l[3])[2])
                            y[14] = int(str(l[3])[3])
                            x[2] = int(str(l[0])[2]+str(l[1])[2]+str(l[2])[1]+str(l[3])[0])
                            if checkList(x[2],l1) == 1:
                                for i4 in createList(l2,4):
                                    l[4] = i4
                                    y[15] = int(str(l[4])[0])
                                    y[16] = int(str(l[4])[1])
                                    y[17] = int(str(l[4])[2])
                                    y[18] = int(str(l[4])[3])
                                    x[3] = int(str(l[1])[0]+str(l[2])[3]+str(l[3])[2]+str(l[4])[0])
                                    if checkList(x[3],l1) == 1:
                                        for i5 in createList(l2,4):
                                            l[5] = i5
                                            y[19] = int(str(l[5])[0])
                                            y[20] = int(str(l[5])[1])
                                            y[21] = int(str(l[5])[2])
                                            y[22] = int(str(l[5])[3])
                                            x[4] = int(str(l[2])[3]+str(l[3])[2]+str(l[4])[1]+str(l[5])[0])
                                            if checkList(x[4],l1) == 1:
                                                for i6 in createList(l2,4):
                                                    l[6] = i6
                                                    y[23] = int(str(l[6])[0])
                                                    y[24] = int(str(l[6])[1])
                                                    y[25] = int(str(l[6])[2])
                                                    y[26] = int(str(l[6])[3])
                                                    x[5] = int(str(l[3])[3]+str(l[4])[2]+str(l[5])[1]+str(l[6])[0])
                                                    x[7] = int(str(l[5])[3]+str(l[6])[2])
                                                    x[8] = int(str(l[6])[3])
                                                    if checkList(x[5],l1) * checkList(x[7],l1) * checkList(x[8],l1) == 1:
                                                        for i7 in createList(l2,1):
                                                            l[7] = i7
                                                            y[27] = int(str(l[7])[0])
                                                            x[6] = int(str(l[4])[3]+str(l[5])[2]+str(l[6])[1]+str(l[7])[0])
                                                            if checkList(x[6],l1) == 1:
                                                                print x
                                                                print y            
                                                                displayResult(l)
                                                                displayCount(y)

if __name__ == "__main__":
    main()
