####code 3
l2=['Network','Math','Programming','Physics','Music']
c=0
for i in range(len(l2)):
     if l2[i].startswith('P'):
         c=c+1
         print('the item {} that starts with P letter is / {}   /and its index is  {} '.format(c,l2[i],i)) 
