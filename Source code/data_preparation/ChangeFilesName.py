import os
# specify your path of directory
path = r"C:\Users\Mahmoud_Mansour\Downloads\Compressed\test_fire"
x=0
z=0
# call listdir() method
# path is a directory of which you want to list
directories = os.listdir( path )

# This would print all the files and directories
for file in directories:
    if file.endswith('.png'):
        os.rename(path+"\\"+file, 'image {}.png'.format(x))
        x+=1
    elif file.endswith('.jpg'):
        os.rename(path+"\\"+file, 'image {}.jpg'.format(x))
        x+=1
    elif file.endswith('.txt'):
        os.rename(path+"\\"+file, 'image {}.txt'.format(z))
        z+=1
print("دارت يا صيع")