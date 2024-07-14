
listmaximum=[20,60,70,90,500,700,800,99]
       
def findmax(a):
      for item in listmaximum:
        if item > a:
            print(item)
            print("i,m there")
            
    
        else:
            continue
      
       #print("No maximum items")    
    
print("This are the maximum number above the threshold " + str(findmax(100)))