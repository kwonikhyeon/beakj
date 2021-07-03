import sys
value = {'black' : 0,'brown' : 1,'red' : 2,'orange' : 3,
         'yellow' : 4,'green' : 5,'blue' : 6,'violet' : 7,
         'grey' : 8,'white' : 9, }
a = input()
b = input()
c = input()
print((value[a]*10 + value[b]) * (10**value[c]))