def solve(numheads, numlegs):
    c=2*numheads
    d=numlegs-c
    rabbits=int(d/2)
    chicken=int(numheads-rabbits)
    print("chicken -",chicken,",","rabbits -",rabbits)
solve(35,94)


