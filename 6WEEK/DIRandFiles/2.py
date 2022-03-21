import os
a=input()
print('Exist:', os.access(a, os.F_OK))
print('Readable:', os.access(a, os.R_OK))
print('Writable:', os.access(a, os.W_OK))
print('Executable:', os.access(a, os.X_OK))