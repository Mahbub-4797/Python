

'''
n = 5

*
**
***
****
*****

'''

'''
n = 5

for x in range(n+1):
    print(x*("*"))

'''



'''
n = 5 

*
***
*****
*******
*********

# 1 + 3 + 5 + 7 + 9

'''


'''
n = 5

for x in range(0,n,1):
    print(((x*2)+1)*("*"))

'''


'''
            total     space     (*/star)
     *        6         5        1
    **        6         4        2
   ***        6         3        3
  ****        6         2        4
 *****        6         1        5
******        6         0        6

'''

n = 6
space = " "
star = "*"

for x in range(1,n+1,1):
    print((space*(n-x)), star*x)