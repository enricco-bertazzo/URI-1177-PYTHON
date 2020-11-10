t = 0
numero = int(input("")) 

for i in range(0,1000):
    print("N[{}] = {}".format(i, t))
    if t < (numero -1): 
        t = t + 1
    else:
        t = 0
        i = i + 1