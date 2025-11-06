Bf is a One thing to keep in mind:
- The inventor of brainf*ck does not care about the programmer.
- The inventor cares about whoevers writing the interpreter(him)
- Therefore, the interpreter is extremely simple, the program writing
- IS NOT!!!
- it's also turing complete
There are 8 commands in Brainf*ck
+- [] ,. <>
There is The tape. Not any tape, The Tape.
The commands and tape have a few implementations and interpretations.
However, the original compiler uses this set of rules:
- The tape is an array with 30,000 u8 integers
- The commands do stuff to the tape. This includes, reading and writing.
There is also a pointer. this is an integer that shows 
- Also, I can't remember what the original program did but let's just say


| 0 | 0 | 0 | 0 |
  ^ 
  |
  |
<  >

?
++
?
[>++<-]
?