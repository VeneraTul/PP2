def filer(primeNum):
      print(list(filter(lambda x: all(x%i!=0 
                                      for i in range(2,x)),primeNum )))
      
filer([1,2,3,4,5,6])
