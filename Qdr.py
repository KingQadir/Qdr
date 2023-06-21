import os, platform
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
    from Qdr import Fire	
    Fire()

elif bit == '32bit':
    from Qdr32 import Fire
    Fire()
else:
    print('\n\x1b[1;91m[×] Your Device is Not Supported This Tool !');exit()
