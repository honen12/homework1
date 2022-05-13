names=['honen','adnan','ibrahem','sara','mohamad']
while True:
     name=input('enter the name,please::-1 for terminate program:')
     if name=='-1':
          print('thank you')
          break
     if name in names:
          print(name,'is gruadeted')
     elif name not in names:
          print(name,'is not gruadeted sorry')
     
