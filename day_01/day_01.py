calories_list = []
calories_total = 0

with open("./day_01/input.txt", "r") as f:
    for line in f:
        if line == "\n":
            calories_list.append(calories_total)
            calories_total = 0
            continue
        
        calories_total += int(line)

sorted_calories = sorted(calories_list, reverse=True)
print("Part 1 =", sorted_calories[0])
    
print("Part 2 =", sorted_calories[0] + sorted_calories[1] + sorted_calories[2])
    


