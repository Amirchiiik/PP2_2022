import os

def DIRandFILE(path):
    for i in os.listdir(path):
        i_s=os.path.join(path, i)
        if os.path.isfile(i_s):
            print(f'FILE: {i_s}')

        else:
            print(f'Dir: {i_s}')
            DIRandFILE(i_s)

path=input()
DIRandFILE(path)
