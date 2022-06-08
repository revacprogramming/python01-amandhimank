# Lists

fname = "dataset/romeo.txt"
#fname = input("Enter file name: ")
fh = open(fname)
lst = fh.read()
l = []
for line in lst.split():
    l.append(line)
l.sort()
lt = []
for i in l:
    if i not in lt:
        lt.append(i)
    
print(lt)
