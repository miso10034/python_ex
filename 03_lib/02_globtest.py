import glob,os

path = os.path.dirname(__file__)
result = glob.glob(path+'/01*.*') # ?하나면 글자 아무거나 1개 ?? 두개면 2개
print(result)

