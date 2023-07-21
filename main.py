import os
import datetime
import shutil
name=datetime.datetime.now()
datee=str(name.date())
fpath = "F:"
path=os.path.join(fpath, datee)
newpath=str(path)+r"\\"

try:
    os.mkdir(path)
    print("Folder %s created!" % path)
except FileExistsError:
    print("Folder %s already exists" % path)
artfiles = [f for f in os.listdir(fpath) if '.art' in f.lower()]
rlffiles = [f for f in os.listdir(fpath) if '.rlf' in f.lower()]
print(artfiles)
for file in artfiles:

    source = fpath + file
    destination = newpath + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)
for file in rlffiles:

    source = fpath + file
    destination = newpath + file
    # move file
    shutil.move(source, r"F:\Relief\\")
    print('Moved:', file)