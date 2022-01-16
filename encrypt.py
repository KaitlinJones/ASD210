

plainText = input("Please enter a message: ")
distance = input("Please enter the distance: ")
code = ""
for ch in plainText:
    ordVal = ord(ch)
    cipherVal = ordVal + int(distance)
    if cipherVal > 127:
        cipherVal = distance - (127 - ordVal + 1)
    code += chr(cipherVal)
print(code)
 