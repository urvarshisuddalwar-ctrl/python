# #mkdir -> to create a new folder / directory
# #rmdir -> to remove any folder/directory


# ""

# # FILES
# # x -> This mode will only create the file and file and if already exists we will get an error back

# # w -> Agar file exists nahi kar rahi hai so this mode will create one and insert the content inside  the file.

# # a
# # r
# # ""
# # #mode  1: x -> just to create the file
# # #open ("Garba.txt","x")

# # #mode 2:w -> if there is any content inside the file so the new one will replace the old one.
# # #file =open ("Garba .txt,"w) 
# # file.write ("khelo garba khub kehlo din raat khelo")

# #Mode 3: a -> add the text at the last.
# # file = open("Garba .txt","a")
# # file.write("\n This message is newly added")

# # #Mode 4: r -> read the content inside of the file
# # file = open("garba.txt","r")
# # print(file.read())



# import os


# with open("sample.txt","w") as file:
#     file.write("This is new file")
    

# #CRUD - CREATE ,READ ,UPDATE, DELETE
# os.remove("Garba.txt")

from pathlib import Path
import os
def create_folder():
    name = input("TELL your folder name:-")
    p =Path(name)

    if p.exists():
        print("this folder name already exist please try again")
        create_folder()
    else:
        p.mkdir()
        print("folder created successfully !")

def read_folder():
    p= Path("")
    names =list(p.rglob("*"))
    return names


def update_folder(): 
    name = input("which folder ypu wnat to update:")
    old_p = Path(name)

    if old_p.exists():
        new_name = input("Tell new folder name:-") 
        new_p = Path(new_name)
        old_p.rename(new_p)
        print("folder name changed succesfully")
    else:
        print("no such folder exist please try again")
        update_folder()

def delete_folder():
    name = input("Tell your folder name:-")
    p = Path(name)

    if not p.exists():
        print("this folder name does not exist please try again")
        delete_folder()
    else:
        p.rmdir()
        print("folder deleted succesfully !")

def create_file():
    name = input("Tell your file name with extension")
    p = Path(name)

    if p.exists():
        print("file already exists please try again")
        create_file()
    else:
        with open(p,"w")as file:
            data = input("Enter what  you want to write:")
            file.write(data)
            print("succesfully created")

def read_file():
    name =input("Tell your file name with extention")
    p =Path(name)
    if p.exists() and p.is_file():
        with open(p,"r") as file:
            data =file.read()
            print("\n\n\n Your file data is\n\n\n")
            print(data)


 

def delete_file():
    name =input("Tell your file name with extension")
    p=Path(name)
    if p.exists() and p.is_file():
     os.remove(p)
     print("file deleted succesfully")
    else:
     print("No such file exist please try again")
     delete_file()

def update_file():
  names = read_folder()
  for i in names:
        i =str(i)
        p =Path(i)
        if p.is_file():
            print(i)

name =(input("which file you want to update"))
p =Path(name)

if p.exists() and p.is_file():
    print("press 1 to change the file name")
    print("press 2 to overwrite the file")
    print("press 3 to append something in your file")

    check =int(input("Tell your output:-"))

    if check ==1:
        new_name =input("Tell the new name :-")
        new_p =Path(new_name)
        p.rename(new_p)

    elif check ==2:
        with open(p,'w')as file:
            data =input("what do you want to overwrite:-")
            file.write(data)
            print("overwritten succesfully")

    elif check ==3:
        with open(p,'a')as file:
            data =input ("what do you want to append:-")
            file.write(""+data)
            print("appended succesfully")
    else:
        print("no such file exists please try again")
        update_file()
 



print("Press 1 for Creating a folder: ")
print("Press 2 for Releting any folder: ")
print("Press 3 for Updating any folder : ")
print("Press 4 for Deleting any folder: ")
print("press 5 for Creating a file: ")
print("print 6 for Reading any file: ")
print("print 7 for updating any file:")
print("print 8 for Deleting any file:")


res = int(input("Tell your response:-"))

if res == 1:
    create_folder()

if res == 2:
  read_folder()

if res ==3:
    update_folder()

if res==4:
    delete_folder()

if res==5:
    create_file()

if res==6:
    read_file()

if res == 7:
    update_file()

if res==8:
    delete_file()








