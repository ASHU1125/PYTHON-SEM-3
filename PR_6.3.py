string = "12203AB3"
L1 = []
count = 0
for i in string:
    if i not in L1:
        L1.append(i)
        for j in string:
            if i == j :
                count += 1
        print(i,"(",count,"Times )") 
        count = 0