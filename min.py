
n = int(input("n:"))
s = 0
for i in range(1,n+1):
     x = int(input('number:' + str(i) + '=')) 
     s += x
     m = s/n
print('mean',m)
