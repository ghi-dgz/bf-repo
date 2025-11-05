import sys
def bf(code, input_tape, input_auto_zero):
    input_read_pos = 0
    num_zeros = 1 
    tape = [0] * num_zeros
    tickerpos = 0
    last_print = "input"

    def remove_non_commands(code):
        commands = list("><+-.,[]?")
        return ''.join(c for c in code if c in commands)
    
    i = 0
    while i < len(code):
        char = code[i]
        
        if char == '>':
            tickerpos += 1
            if tickerpos >= num_zeros: # INFINITE TAPE (for my purposes)
                num_zeros += 1
                tape.append(0) 
        elif char == '<':
            tickerpos -= 1
            if tickerpos < 0:
                tape.insert(0, 0) # INFINITE TAPEEEEEEEE
                #tickerpos = num_zeros - 1
        elif char == '+':
            tape[tickerpos] = (tape[tickerpos] + 1) % 256
        elif char == '-':
            tape[tickerpos] = (tape[tickerpos] - 1) % 256
        elif char == '?':
            if last_print == "output": print("")
            print(tape)
            if 0 <= tickerpos <= len(tape)-1:
                pos = 1  
                for k, val in enumerate(tape):
                    if k == tickerpos:
                        break
                    pos += len(str(val))
                    if k < len(tape) - 1:
                        pos += 2
                print(' ' * pos + '^')
            else:
                print(tickerpos)
            last_print = "debug"

        elif char == '.':
            print(chr(tape[tickerpos]), end='')
            last_print = "output"
        elif char == ',':
            if len(input_tape) <= input_read_pos and not input_auto_zero:
                if last_print == "output": print("")
                input_tape += input("input: ")

            if len(input_tape) > input_read_pos:
                tape[tickerpos] = ord(input_tape[input_read_pos]) % 256
                input_read_pos += 1
            else:
                tape[tickerpos] = 0
            last_print = "input"
            
        elif char == '[':
            if tape[tickerpos] == 0:
                    # find matching ]
                    count = 1
                    i
                    while count > 0:
                        i += 1
                        if code[i] == "[":
                            count += 1
                        elif code[i] == "]":
                            count -= 1
        elif char == ']':
            if tape[tickerpos] != 0:
                    # find matching [
                    count = 1
                    while count > 0:
                        i -= 1
                        if code[i] == "]":
                            count += 1
                        elif code[i] == "[":
                            count -= 1
        else:
            pass
        i += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_tape = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2][0:2] != "--") else ""
        input_auto_zero = False if input_tape == "" else True

        with open(sys.argv[1], 'r') as file:
            bf(file.read(), input_tape=input_tape, input_auto_zero=input_auto_zero)
    else:
        print("Usage: python bf_intp.py [file] [args]")