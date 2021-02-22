import time
from itertools import combinations, permutations

start_time = time.time()

pk1 = 8335663
pk2 = 8614349
pk1test = 5764801
pk2test = 17807724
modulo = 20201227

def looper(subject,loops,modulo,target):
    ans = (1,1)
    for i in range(loops):
        ans = (i+1,(ans[1] * subject) % modulo)
        print(f"{ans}")
        if ans[1] == target:
            print(f"Found target:{ans}")
            break
    return ans

def test():
    #TEST find nr of loops
    looper(7,1000,modulo,pk1test)
    #Found target:(8, 5764801)
    looper(7, 1000, modulo, pk2test)
    #Found target:(11, 17807724)
    #Find encryption key loop from 1 and key from 2
    loop = 8
    looper(pk2test,loop,modulo,-1)
    #(8, 14897079)
    #Check if it is the same other way around
    # Find encryption key loop from 2 and key from 1
    loop = 11
    looper(pk1test, loop, modulo, -1)
    #(11, 14897079)


def part1():
    #pk1 = 8335663
    #pk2 = 8614349
    #find nr of loops
    print(f"Find loops for pk1")
    looper(7,1000000000,modulo,pk1)
    #Found target:(6041183, 8335663)
    print(f"Find loops for pk2")
    looper(7,100000000000,modulo,pk2)
    #Found target:(8306869, 8614349)
    #Find encryption key loop from 1 and key from 2
    loop = 6041183
    looper(pk2,loop,modulo,-1)
    #
    #Check if it is the same other way around
    # Find encryption key loop from 2 and key from 1
    #loop = 8306869
    looper(pk1, loop, modulo, -1)
    #(8306869, 6408263)


#test()
part1()
print("--- %s seconds ---" % (time.time() - start_time))