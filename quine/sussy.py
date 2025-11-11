inp = input("> ")
print("uwu\n\n")
output = ""
positron = 3
uwu = list('<.>+')
for char in inp:
    uwuu = uwu.index(char) 
    travels = uwuu - positron
    if travels >= 0:
        output += ">" * travels
    else:
        output += '<' * (-1 * travels)
    output += '.'
    positron = uwuu
print(output)
