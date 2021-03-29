
'''
In this file will try Interactive mode in VsCode it's like Jupyter Notebook
each cell shall start with '# %%'
in this Example will play with os library

'''
# %%
import os
# os.path
path = os.getcwd()
print(path)
# first make dir name: test in folder will run
folder = "test"
os.mkdir(folder)
# go to test folder
os.chdir(folder)
cpath = os.getcwd()
print(cpath)
file = "test.py"
# crate the file test.py then write in the file
f = open(file, mode="a")


def write_in_file():
    stre = "3"
    f.write("# test\nprint("+stre+")\n")
    f.write("def a(x):\n\tprint(x)\n")
    f.write("a(3)")


write_in_file()
# close file
f.close()
# %%
'''
here play with os library
'''
# par=os.pardir
# print(par)
# go to the upper folder
os.chdir("..")
path = os.path.abspath(os.getcwd())
# It will return a string containing the absolute path to the running script.
# dir_list = os.listdir(path)
print(path)
# print(dir_list)
# os.chdir("python")
# path1 = os.path.abspath(os.getcwd())
# dir_list1 = os.listdir(path1)
# print(path1)
# print(dir_list1)
os.chdir("test")
path2 = os.path.abspath(os.getcwd())
print(path2)

# %%
'''
read file
'''
path = os.path.abspath(os.getcwd())
print(path)
dir_list = os.listdir(path)
print(dir_list)
filepy = open(dir_list[0], mode="r")
print(filepy.read())
filepy.close()

# %%
'''
the correct way to play with folders in pathon
always doing that way to avoid problems.
'''
cwd = os.getcwd()
try:
    os.chdir("test")
    print("in the file", os.getcwd())
except Exception as e:
    print(e)
finally:
    print("Restoring the path")
    os.chdir(cwd)
    print("current dir is ", os.getcwd())
