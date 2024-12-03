with open("input.txt", "r") as f:
    lines = f.readlines()

safe_reports = 0

for line in lines:
    prev = -1
    direction = ""
    was_safe = True
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
                was_safe = False
                break
        elif num - prev < 0 and abs(num - prev) <= 3: 
            if(direction == ""):
                direction = "dec" 
            if(direction != "dec"):
                was_safe = False
                break
        else:
            # Ignore this line as it cannot meet the criteria
            was_safe = False
            break
        prev = num
    if was_safe:
        safe_reports += 1

print(safe_reports)