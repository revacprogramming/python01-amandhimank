# Files

fname = "dataset/mbox-short.txt"
 #fname = input("Enter file name: ")
fh = open(fname)
count = 0
number = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        n = line.find(":")
        number += float(line[n+1:])
        count += 1
        
print("Average spam confidence:",number/count)