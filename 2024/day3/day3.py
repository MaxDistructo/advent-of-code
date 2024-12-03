import re
with open("input.txt", "r") as f:
    lines = f.readlines()
single_line = ""
for line in lines:
    single_line += line

mul_instructions = []
mul_instructions.extend(re.findall(r"(?:do\(\))|(?:don't\(\))|(?:mul\([0-9]*,[0-9]*\))", single_line))
#print(mul_instructions)
sum = 0
process = True
for instruction in mul_instructions:
    if instruction == "do()":
        process = True
    elif instruction == "don't()":
        process = False # disable this line to get part 1
    elif process:
        split_str = instruction.split(',') 
        sum += int(split_str[0].replace("mul(", "")) * int(split_str[1].replace(")",""))
print(sum) 
