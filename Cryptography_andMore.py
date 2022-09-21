import sys
import numpy as np
import matplotlib.pyplot as plt
import math

def Encryption(M,r,n):
    return pow(M,r,n)

def Decryption(C, d, n):
    return pow(C, d, n)

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

def send_DSig(M,d,n):
    return pow(M,d,n)

def receive_DSig(C,r,n):
    return pow(C,r,n)

def find_d(p,q,r):
    d = 1
    m = (p-1)*(q-1)
    '''n = p*q'''
    while (r*d%m != 1):
        d = d + 1
    return d

"""Scalar (dot) product = u1*v1 + u2*v2 + ... un*vn """
def dotProd():
    u=np.array([3,4,5,7])
    v=np.array([-1,3,6,7])
    return np.dot(u,v)

def calc_angle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

a = np.array([1, 2, 0, 1])
b = np.array([3, 0, 1, 2])
#c = np.array([0,0,2,0,1,0,0,0,3,0,0,0,0,2,1,0])

print("A vs B:", calc_angle(a, b))
#print("B vs C:", calc_angle(b, c))
#print("A vs C:", calc_angle(a, c))


"""Norm = sqrt( (u1*u1)+ (u2*u2) )"""

"""TF-ID = TF*log(N/DF)"""

"""A = np.array([[0.7, 0.6, 0.7], [0.6, 0.5, 0.6], [0.7, 0.6, 0.7]])
cm = plt.get_cmap("gray")
plt.imshow(A, interpolation="nearest", cmap=cm, vmin=0, vmax=1)
plt.show()"""

"""u=np.array([3,4,5,7])
v=np.array([-1,3,6,7])
print(u+v)"""

"""Rotate 90_deg: (a,b) -> (-b,a)"""
"""Rotate 180_deg: (a,b) -> (-a,-b)"""
"""Rotate vertical_Flip: (a,b) -> (a,-b)"""
"""Rotate horizontal_Flip: (a,b) -> (-a,b)"""

"""A = np.matrix([[2, 1], [0, -1]])
x = np.matrix([[3], [1]])
print(A*x)"""

'''T1 = np.matrix([[1, 2], [0, 1]])'''
'''T2 = np.matrix([[3,0], [-2,1]])
A = np.matrix([-3,2])
print(T2*A) #->transformation'''

A = np.array([[3, 1], [-2, 4]]])
x = np.array([[1,-2], [-1,2], [3,-1]]) #->can't * if diff inner dimensions
#print(np.asmatrix(A)*np.asmatrix(x))
print(x@A)

"""A = np.matrix([[3, 1], [-2, 4]])
I = np.identity(2)
print("A=", A)
print("I=", I)
print(A*I)
print(I*A)"""

def applytrans(trans):
    shape = np.array([[4,-3]])
    plt.plot(shape[0], shape[1], 'g')  # original shape in green
    print("shape:")
    print(shape)
    new_shape = trans @ shape
    plt.plot(new_shape[0], new_shape[1], 'r') # new shape in red
    print("new shape:")
    print(new_shape)
    plt.grid(True)
    plt.axis("equal")
    plt.show()

'''rotation by 60° anti-clockwise = cos 60°, − sin 60 °
sin 60°, cos 60°'''

'''rotation by 60° clockwise = cos(−60)°, − sin(−60)°
sin(−60)°, cos(−60)° '''

'''A = np.matrix([[0,2,-1,1], [-1,3,4,2], [2,0,-1,0], [-1,-2,0,3]])
print("det\n", A, "=")
print(np.linalg.det(A))'''

print(np.cross([1,-3,2], [3,1,-1]))

# Bisection Algorithm
def f(x):
    return 4*x**3-3*x**3--14*x-22

def Bisection(f, a, b):
    m = (a+b)/2
    while (abs(f(m)) > 1e-6):
        print("[",  a, ",", b, "]")
        if f(m) * f(a) > 0:
            a = m
        else:
            b = m
        m = (a+b)/2
    return m

#print(Bisection(f, 2, 3))

#print(applytrans(np.array([[2, 0], [0, 2]])))
#print(dotProd())
#print(Encryption(4,7,187))
#print(Decryption(C, d, n))
#print(modInverse(7, 17))
#print(send_DSig(M,d,n)
#print(receive_DSig(C,r,n))
#print(find_d(11,17,7))
#print(sys.version)


key = 5
input = "MSG"
output = ""
for ch in input:
    if ch >= 'A' and ch <= 'Z':
        code = ord(ch) - ord('A')
        newCode = (code + key) % 26
        newCh = chr(newCode + ord('A'))
        output = output + newCh
    else:
        output = output + ch
#print(output)
















#
