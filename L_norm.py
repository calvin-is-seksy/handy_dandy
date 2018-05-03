def L_norm(p):
    myList = [1.9, 2.6, 2.6, 0.8, 0.2, 0.1, 0.4]
    mySum = 0.0
    for i in myList: 
        mySum += i**p
return mySum**(1.0/p)
