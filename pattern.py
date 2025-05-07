
alphabet_arr = ['A','B','C','D','E']


n = 5
work_till= (n*2) - 1

for i in range (0,work_till):
    if (i<n):
        # pass
        for sp in range(0,n-1-i):
            print(" ",end="")
            
        for j in range(0,i+1):
            print(alphabet_arr[j] , end='')
            if j!=i:
                print(" ", end='')
                
        for sp in range(0,n-1-i):
            print(" ",end="")
        print("")
    else:
        # print("---")
        l = work_till - i -n
        l = -l
        # print(f"{i=},{work_till=},{n=},{l=}")
        
        for sp in range(0,l):
            print(" ",end="")
            
            
        for j in range(0,work_till-i):
            print(alphabet_arr[j] , end='')
            if (j<work_till-i-1):
            # if j!=work_till-i:
                print(" ", end='')
                
                
        for sp in range(0,l):
            print(" ",end="")
        
        print("")



