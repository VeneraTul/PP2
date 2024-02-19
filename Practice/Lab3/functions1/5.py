from itertools import permutations
def all_permutations(s):
    numes = list()
    for a in s:
        numes.append(a)
    permutationss = list(permutations(numes))
    for permutation in permutationss:
        print(''.join(permutation))
    
    
s = input()
all_permutations(s)