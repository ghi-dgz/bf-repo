python code

```py
# STEP 1
print(i)

# STEP 2
i = "print(i)"
print(i)

# STEP 3
i = "print('i = ' + chr(34) + i + chr(34) + chr(10) + i)"
print('i = ' + chr(34) + i + chr(34) + chr(10) + i)
```

bf
```bf
STEP 1:
0 A B C D E 0
^
>[.>]

STEP 2:
0 0 0 0 0 0 0
^
----[---->+<]>-

0 > [ . > ] 0
^
>[.>]

```
