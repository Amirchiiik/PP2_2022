import string
class String1:
    def __init__(self,s):
        self.s=s
    def __str__(self):
        return self.s.upper()
n=input("Enter any string:\n")
print(f'Your string in uppercase is:\n{String1(n)}')