import os
num = 1
while num <= 50:
    if num == 25:
        file = open(fr"H:\Learn_Python\14_FilesHandling\special-text.txt",'w')
        num += 1
    else:
         file = open(fr"H:\Learn_Python\14_FilesHandling\txt{num}.txt",'w')
         file.write(f"Elzero Web School => {num}")
         num += 1
    file.close()

print(os.getcwd())
print(os.path.dirname(__file__))
print(os.path.basename(os.path.abspath(__file__)))

print(num-1)