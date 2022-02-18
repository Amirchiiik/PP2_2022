def solve(heads,legs):
    if legs%2!=0 or heads>legs or heads==0:
        return "There is no solution"
    rabb=(legs-2*heads)/2
    ch=heads-rabb
    return int(rabb),int(ch)
heads=int(input("Enter the number of heads:\n"))
legs=int(input("Enter the number of legs:\n"))
res1,res2=solve(heads,legs)
print("The number of rabbits "+str(res1)+" and the number of chickens "+str(res2))
