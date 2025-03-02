file = open(fr"H:\Learn_Python\14_FilesHandling\txt1.txt",'r')
num_lines,num_words = 0,0

for line in file:
    line = line.strip('\n')
    words = line.split()
    num_words += len(words)
    num_lines += 1
file.close()

def count_letter_occurrence(letter):
    file = open(fr"H:\Learn_Python\14_FilesHandling\txt1.txt",'r')
    content = file.read()
    file.close()
    return content.count(letter)

def count_letters():
    cleaned_txt = ""
    file = open(fr"H:\Learn_Python\14_FilesHandling\txt1.txt",'r')
    for line in file:
        cleaned_txt += "".join(line.split())
    file.close()
    return len(cleaned_txt)
    
    

print(f"Number Of Lines Is => {num_lines}")
print(f"Number Of Words Is => {num_words}")
print(f"Number Of Chars Is => {count_letters()}")
print(f"Number Of \"l\" Char Is => {count_letter_occurrence('l')}")


