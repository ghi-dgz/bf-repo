def to_ord_list(strig: str):
    return [ord(char) for char in strig]

def to_bf_code(ordstrig: str):
    return [('+'*char + '>') for char in ordstrig]

def both(inp: str):
    return to_bf_code(to_ord_list(inp))

returns = both("<.>+-[]")
#print(returns)
print("".join(returns))