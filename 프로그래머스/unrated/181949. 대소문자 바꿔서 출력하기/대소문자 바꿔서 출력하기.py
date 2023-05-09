str = input()
new_str = ""
for c in str:
    i = ord(c)
    if i >= 97:
        i -= 32
    else:
        i += 32
    new_str += chr(i)
    
print(new_str)