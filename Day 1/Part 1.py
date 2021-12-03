previous_depth = 0
current_depth = 0
increases = 0
file = open("input.txt")
for line in file:
    if current_depth == 0:
        current_depth = int(line)
        print(f"{current_depth}  (First Depth)")
    else:
        previous_depth = current_depth
        current_depth = int(line)
        if current_depth > previous_depth:
            print(f"{current_depth}  (Increase)")
            increases = increases + 1
        elif current_depth < previous_depth:
            print(f"{current_depth}  (Decrease)")
print(f"Times increased - {increases}")

