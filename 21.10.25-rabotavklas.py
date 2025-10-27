import os
import random

PATH = r"C:\Users\marti\allFolder\code\Martin-Panayotov-Scriptovi-9v\21-10-25-vklas"  # <-- change this to your real folder
os.makedirs(PATH, exist_ok=True)

def wipe_directory(): #delete old generated files to have clean results
    for name in os.listdir(PATH):
        full_path = os.path.join(PATH, name)
        if "file" in name and os.path.isfile(full_path): 
            os.remove(full_path)

def SetFileCount():
    n = int(input("Enter file count:"))
    for i in range(1, n+1):
        path = os.path.join(PATH,f"file_{i}.txt")
        with open(path,"w",encoding="utf-8") as f:
            f.write(f"This is file {i} of the bunch")

    print(f"Saved {n} files")

def RandomFileCount():
    count = random.randint(1, 15)
    for i in range(1, count + 1):
        path = os.path.join(PATH,f"random_file_{i}.txt")
        with open(path,"w",encoding="utf-8") as f:
            f.write(f"This is random file {i}")

    print(f"Saved {count} files")

def ReadAndEdit():
    file_path = os.path.join(PATH, "large_text.txt")
    output_file = os.path.join(PATH, "filtered_file.txt")
    if not os.path.exists(file_path):
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(
'''This
is
an
example
text
'''                )
    with open(file_path,"r",encoding="utf-8") as source, open(output_file,"w",encoding="utf-8") as out: #output cleared by "w"
        for index, line in enumerate(source, 1): #index lines
            if index %2 != 0:
                out.write(line)

    print("built new file")

wipe_directory()
SetFileCount()
RandomFileCount()
ReadAndEdit()


