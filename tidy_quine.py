program = [
   '',
   '# Write start of program up to introducer for string list',
   'print("#!/usr/bin/python")',
   'print("program = [")',
   '',
   '# Write whole program as strings',
   'for line in program:',
   '   print("   " + repr(line) + ",")',
   '',
   '# Write terminator for string list',
   'print("]")',
   '',
   '# Write end of program',
   'for line in program:',
   '   print(line)',
]

# Write start of program up to introducer for string list
print("program = [")

# Write whole program as strings
for line in program:
   print("   " + repr(line) + ",")

# Write terminator for string list
print("]")

# Write end of program
for line in program:
   print(line)
