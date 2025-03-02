import os
num = 50
while num != 40:
    os.remove(fr"H:\Learn_Python\14_FilesHandling\txt{num}.txt")
    num -= 1
