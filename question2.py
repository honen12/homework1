##Question2: from decimal to binary
while True :
     try:##معالجة حالة ادخال المستخدم  لاحرف
          x=int(input('enter decimal number please ,enter -1 to terminate program:'))
          if x==-1:
               break
          list1=[]
          while True:
               l=x%2
               x=x//2
               list1.append(l)
               if(x==0):
                    break
          list1.reverse()
          print("the binary number is",list1)
     except ValueError as err :
          print(err)
          print(' error, you must enter just number  for program work ')
