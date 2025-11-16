class A:
    pass

class B(A):
    pass 

class C(B):
    pass

class D(C):
    pass

print('MRO da classe D:', D.mro()) 
print('MRO da classe C:', C.mro())
print('MRO da classe B:', B.mro())
print('MRO da classe A:', A.mro())
