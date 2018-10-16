# import the os module
import os

# detect the current working directory and print it
dirpath = os.getcwdb()  
print ("The current working directory is %s" % dirpath)


# define the name of the directory to be created
path = "/Users/muhamedamin/Downloads/PYTHON/directory"

# define the access rights 777 (r&w by all) 
# 755 (readable and accessible by all users, and write access by only the owner)

access_rights = 0o755

try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)
