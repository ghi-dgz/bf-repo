# random bf snippets

yeah

# bf summarised

|command|what does that do|interpreter implementation|
|:-:|:-:|:-:|
|+|increments current cell|tape[pointer] += 1|
|-|decrements current cell|tape[pointer] -= 1|
|>|moves pointer forwards one|pointer += 1|
|<|moves pointer back one|pointer -= 1|
|[|start loop|if tape[pointer] == 0: # skip to closing ] in code reading|
|]|end loop|if tape[pointer] != 0: # go backwards to opening [ in code reading|
|,|take input|
|.|write to output current cell|