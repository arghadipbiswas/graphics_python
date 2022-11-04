# import random

# def gameWin(comp,you):
#     if comp == you:
#         return None
#     elif comp == 's':
#         if you == 'g':
#             return True
#         elif you == 'w':
#             return False
#     elif comp == 'w':
#         if you == 'g':
#             return False
#         elif you == 's':
#             return True
#     elif comp == 'g':
#         if you == 's':
#             return False
#         elif you == 'w':
#             return True

# print("Computer choice Snake(s) Water(w) or Gun(g):")

# randNo = random.randint(1,3)
# if randNo == 1:
#     comp = 's'
# elif randNo == 2:
#     comp ='w'
# elif randNo == 3:
#     comp = 'g'

# you=input("Your choice Snake(s) Water(w) or Gun(g):")

# a=gameWin(comp,you)

# print(f"computer choose {comp} ")
# print(f"you choose {you} ")

# if(a==None):
#     print("Tie!")
# elif(a):
#     print("won!")
# else:
#     print("loss!")



e=(input())
int(e)
for i in range(e):
    p=input()
    y=p.lower()
    t=p.upper()
    s=int(p)
    if (y and t and s):
        print("YES")
    else:
        print("NO")