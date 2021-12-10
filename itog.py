import os
from pprint import pprint
path = os.getcwd()
print(path)
def association():
    list_of_files = os.listdir('hw2')
    list_files = []
    path = os.getcwd()
    for file in list_of_files:
        os.chdir(path + "\hw2")
        with open(file) as f:
            text_file = str(f.read)
            str_file = f.readlines()
            quantity = len(str_file) 
            list_files.append([file, quantity, str_file])  
    os.chdir(path)
    
    list_b = sorted(list_files, key=lambda x: x[1])
    # pprint(list_b)
    with open('itog.txt', 'w') as file:
        
        for txt_file in list_b:
            file.write(txt_file[0] + '\n')
            file.write(str(txt_file[1]) + '\n')
            file.write(" ".join(txt_file[2]) + '\n')






association()
# D:\программа\hw_files