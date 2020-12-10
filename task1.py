from sympy import *

x,y,z= symbols("x y z")
n1 = sympify(input('give equation:'))
l=list(degree_list(n1))
t = len(l)
if t==1:
    p = l[0]
    q = 0
    r = 0
    
if t==2:
    p = l[0]
    q = l[1]
    r = 0

if t==3:
    p = l[0]
    q = l[1]
    r = l[2]
    
        
if (p==1 and q==1 and r==1):
    print("linear equation of three variable")
elif ((p==1 and q==1) or (q==1 and r==1) or (p==1 and r==1)):
    print('linear equation of two variable')
    
else:
    if p==1 or q==1 or r==1:
        print("linear equation")
        
    if p==2 or q==2 or r==2:
        print("quadratic equation")
    if p==3 or q==3 or r==3:
        print("cubic equation")
    if p==4 or q==4 or r==4:
        print("biquadratic equation")
    if p>4 or q>4 or r>4:
        print("polynomial equation of degree greater than 4")
        


