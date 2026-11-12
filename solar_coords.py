import math

def zero_shortest(x, y, z):
    coo = [x, y, z]

    return(shortest(zero_x(coo), zero_y(coo), zero_z(coo)))

def shortest(a, b, c):
    
    a_len = 0
    b_len = 0
    c_len = 0
    
    for i in range(3):
        a_len += abs(a[i])
        b_len += abs(b[i])
        c_len += abs(c[i])
    
    if a_len <= b_len and a_len <= c_len:
        return a
    elif b_len <= c_len:
        return b
    else:
        return c

def zero_x(c):
    x=int(c[0])
    y=int(c[1])
    z=int(c[2])
    
    return([0, y+x, z-x])

def zero_y(c):
    x=int(c[0])
    y=int(c[1])
    z=int(c[2])
    
    return([x+y, 0, z+y])
    
    
def zero_z(c):
    x=int(c[0])
    y=int(c[1])
    z=int(c[2])
    
    return([x-z ,y+z ,0])

def xyz(u,v):
    u = int(u)
    v = int(v)
    
    if u == 0:
        x = 0
        y = -1 * v
        z = 0
    
    elif abs(v) == math.ceil(abs(u)/2):
        x = -1* u 
        y = 0
        z = 0
    
    elif u < 0:
        x = u * -1
        y = math.floor(u/2) - v
        z = 0
    else:
        x = 10
        y = v * -1
        z = u * -1
    
    print(zero_shortest(x, y, z))

u = input("U: ")
v = input("V: ")

xyz(u, v)

input("Press any key to quit...") 
