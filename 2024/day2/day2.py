with open("input.txt", "r") as f:
    lines = f.readlines()

safe_reports = 0

def check_line(line: str) -> bool:
    prev = -1
    direction = ""
    for val in line.split(" "):
        num = int(val)
        if(prev == -1):
            prev = num
            # Stop processing
            continue
        if num - prev > 0 and abs(num - prev) <= 3:
            if(direction == ""):
                direction = "inc" 
            if(direction != "inc"):
                return False
        elif num - prev < 0 and abs(num - prev) <= 3: 
            if(direction == ""):
                direction = "dec" 
            if(direction != "dec"):
                return False
        else:
            # Ignore this line as it cannot meet the criteria
            return False
        prev = num
    return True

fail_lines = []

for line in lines:
    # Process directly
    if check_line(line):
        safe_reports += 1
    else:
        fail_lines.append(line)

# Brute force check if any 1 number can be removed and pass the test
for line in fail_lines:
    split_line = str(line).split(" ")
    for i in range(len(split_line)):
        new_line = split_line[:i] + split_line[i+1:]
        if check_line(" ".join(new_line)):
            safe_reports += 1
            break

print(safe_reports)