'''
------------------------------------------
p & q - simple
n = p*q 

f(n) = (p-1)*(q-1)


Evklid alg (e&k)

d * e = k * f(n)+1

privat - d
public - e

d = (k*f(n)+1)/e&k

privat_key - {d,n}
public_key - {e,n}


crypt_mess   = decrypt_mess**e mod(n)
decrypt_mess =   crypt_mess**d mod(n) 
------------------------------------------
'''

import random 

first_public	= random.randrange(10000, 100000)
second_public	= random.randrange(10000, 100000)

Alice_secret	= random.randrange(10000, 100000)
Bob_secret		= random.randrange(10000, 100000) 


A = (second_public**Alice_secret)	% first_public
B = (second_public**Bob_secret)		% first_public


A_secret_key	= (B**Alice_secret) % first_public
B_secret_key	= (A**Bob_secret)	% first_public


print()
print("################################")
print()
print("--------------------------------")
print("[~ BASE_DATA ~]")
print("--------------------------------")
print("first_public		", first_public)
print("second_public		", second_public)
print("Alice_secret		", Alice_secret)
print("Bob_secret		", Bob_secret)
print("--------------------------------")
print()
print("################################")
print()
print("--------------------------------")
print("[~ COMPUTE ~]")
print("--------------------------------")
print("A			", A)
print("B			", B)
print("--------------------------------")
print()
print("################################")
print()
print("--------------------------------")
print("[~ RESULT ~]")
print("--------------------------------")
print("Alice have:		", A_secret_key)
print("Bob have:		", B_secret_key)
print("--------------------------------")
print()
print("################################")







