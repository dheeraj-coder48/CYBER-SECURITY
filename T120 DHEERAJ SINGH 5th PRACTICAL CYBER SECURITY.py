print("T120 DHEERAJ SINGH")
print()
import random

p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))

a = int(input("Enter private key of Alice: "))
b = int(input("Enter private key of Bob: "))

A = pow(g, a, p)
B = pow(g, b, p)

alice_key = pow(B, a, p)
bob_key = pow(A, b, p)

print()
print("Dheeraj's public key:", A)
print("Manya's public key:", B)

print("Dheeraj's shared secret:", alice_key)
print("Manya's shared secret:", bob_key)
print()
if alice_key == bob_key:
    print("Key exchange successful.")
else:
    print("Key exchange failed.")
