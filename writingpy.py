
stringtulis = "tulisan ini bakalan di append"

f = open("filesimpan.txt", "a")
f.write(stringtulis + "\n")
f.close()