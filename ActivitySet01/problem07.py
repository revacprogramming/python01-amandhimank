# Strings

text = "X-DSPAM-Confidence:    0.8475"
n = len(text)
s = text.find(":")
str = text[s+2:]
number = float(str)
print(number)