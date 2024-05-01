import art
from game_data import data
import random

A = random.choice(data)
B = random.choice(data)

def check(A, B):
    """Checks to see if A is equal to B"""
    while A == B:
        B = random.choice(data)
    return B
    
def compare(a, b):
    if a['follower_count'] > b['follower_count']:
        return True
    else:
        return False

B = check(A, B)

print(art.logo)
print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
print(art.vs)
print(f"Against A: {B['name']}, a {B['description']}, from {B['country']}")
choice = input("Who has more followers? Type 'A' or 'B': ").lower()

if choice == "a":
    comp = compare(A, B)
else:
    comp = compare(B, A)

if comp:
    print(f"{A['name']} has more followers.")
else:
    print(f"{B['name']} has more followers.")