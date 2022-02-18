from itertools import permutations
permutations 
def perm(string):
    perms=[''.join(p) for p in permutations(string)]
    return perms
string=input()
print(perm(string))
