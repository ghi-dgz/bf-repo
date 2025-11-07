# random bf snippets

i added rickroll
```
git clone https://github.com/ghi-dgz/bf-repo.git
cd bf-repo
python bf.py rickroll/rick.bf
```
congrats you just got rickrolled
 
# bf summarised

|command|what does that do|interpreter implementation|
|:-:|:-:|:-:|
|+|increments current cell|tape[pointer] += 1|
|-|decrements current cell|tape[pointer] -= 1|
|>|moves pointer forwards one|pointer += 1|
|<|moves pointer back one|pointer -= 1|
|[|start loop|if tape[pointer] == 0: # skip to closing ] in code reading|
|]|end loop|if tape[pointer] != 0: # go backwards to opening [ in code reading|
|,|take input|tape[pointer] = ord(input(""))|
|.|write to output current cell|print(chr(tape[pointer]))|

# interpreter

I wrote a python interpreter, but there are some personalisations/modifications/alterations.  
- Added ? function which prints the current tape
- Added ! function which prints information on code passed in(number of steps in total, infinite loop, time taken, number of bit operations)
- There is an input tape, which can be passed into the interpreter, and if it runs out the interpreter can ask for input if that is turned on. If no input tape is passed, it will ask for input when input is needed, if more than enough is passed it is stored
- Tape specification -> infinite tape, looped tape, and tape with walls on either end (moving left when at the start does nothing)
- % for sleeping for 0.1 seconds (used in animations and games)
  
You can use the interpreter as well as set these by reading the source code.  
nah im joking you use python bf.py [filepath] [input] [args]
e.g. `python bf.py done/misc/multi_input_cat.bf "Hello, world"` (quotes are required if you want to put spaces in the input)