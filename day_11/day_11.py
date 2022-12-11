#!/usr/bin/python3

def init_monkey(m, d):
    # Check if it's already created.
    try:
        if d[m]["created"] == True:
            return d[m], d
    except KeyError:
        pass

    # Define target subdict
    d[m] = {}
    target = d[m]

    # Initialise subkeys
    target["items"]         = []
    target["operation"]     = []
    target["test"]          = 0
    target["if_true"]       = 0
    target["if_false"]      = 0
    target["inspections"]   = 0
    target["created"]       = True

    return target, d


def solve(rounds, monkeys, part):
    round = 0
    item = 0

    # Start rounds
    while round < rounds:

        # Monkeys loop
        for m in monkeys.keys():
            # New target
            t = monkeys[m]

            # Items loop
            for item in t["items"]:
                t["inspections"] += 1
                if t["operation"][1] == "old":
                    amount = item
                else:
                    amount = int(t['operation'][1])
                match t["operation"][0]:
                    case "+":
                        item += amount
                    case "*":
                        item *= amount

                # Losing interest
                if part == 1:
                    item //= 3
                if part == 2:
                    item %= mod

                # Condition to jump
                if item % t["test"] == 0:
                    monkeys[t['if_true']]["items"].append(item)

                else:
                    monkeys[t['if_false']]["items"].append(item)
                
            t["items"] = []


        # Round complete
        round += 1

    # Check inspections
    inspections = []
    for m in monkeys.keys():
        # New target
        t = monkeys[m]
        
        print(f'Monkey {m} inspected items {t["inspections"]} times.')
        inspections.append(t["inspections"])

    inspections = sorted(inspections, reverse=True)
    print(f"Part {part}: {inspections[0] * inspections[1]}")


# Populate dict
monkeys = {}
lines = []
mod = 1
with open("./puzzle_inputs/11.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        lines.append(line)
        
        # New monkey, change target
        if line.startswith("Monkey"):
            t, monkeys = init_monkey(int(line.split(" ")[1][0]), monkeys)
                    
        # Get items
        if "Starting items" in line:
            line = line.split(": ")
            items = line[1].split(", ")
            for item in items:
                t["items"].append(int(item))        

        # Get math
        if "Operation" in line:
            line = line.split(": ")[1].split("old ")[1].split(" ")
            t["operation"].append(line[0])
            t["operation"].append(line[1])

        # Get divisible by
        if "Test" in line:
            # print(line.split("divisible by ")[1])
            t["test"] = int(line.split("divisible by")[1])
            mod *= t["test"]

        # Get conditions
        if "true" in line:
            t["if_true"] = int(line[len(line)-1])
        if "false" in line: 
            t["if_false"] = int(line[len(line)-1])


if __name__ == '__main__':
    solve(20, monkeys, 1)
    solve(10000, monkeys, 2)