import os

from scipy.fftpack import ss_diff 
a=input()
if os.path.exists(a):
    print(f'Name of {"File" if os.path.isfile(a) else "Dir"}: {os.path.basename(a)}')
    print("Catalog: ")
    for i in os.listdir(a):
        i_s=os.path.join(a, i)
        if os.path.isfile(i_s):
            print(f'FILE: {i_s}')

        else:
            print(f'Dir: {i_s}')
else:
    print('False')

# pwd 