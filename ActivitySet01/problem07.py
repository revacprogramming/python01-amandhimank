# Strings

text = "X-DSPAM-Confidence:0.8475"
s = text.find(":")
str = text[s+1:]
number = float(str)
print(number)