print(""" 
************************************************************************

Application that returns the number of repetitions of elements in the list.
*Enter as many values ​​as you want to prepare a dictionary in the program.
*The moment you press the 'q', it will give you feedback as it has reached its purpose.
                                                                   *** by İLHAN ÖDÜN ***
************************************************************************
""")
yourlist = []
key = []
values = []
value = 0
while True:
    default = input("Please enter a value: ")
    if default == 'q':
        break
    else:
        yourlist.append(default)
    
print("The list your entered: {}".format(yourlist))
for i in yourlist:
    for j in range (0,len(yourlist)):
        if yourlist[j] == i:
            value += 1
        setvalue = value
        keynumber = i 
    key.append(keynumber)
    values.append(setvalue)
        
        
    value = 0
    

dictionary = dict(zip(key,values))
print(dictionary)


   
           
    
    
    

    
    
    
    
    
    

    

    
        
    
        
