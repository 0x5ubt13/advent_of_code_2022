instructions = []
with open("./puzzle_inputs/10.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("add"):
            ins = line.split(" ")
            instructions.append(ins[0])
            instructions.append(ins[1])
        else:
            instructions.append(line)

iterator_instructions = iter(instructions)
previous = next(iterator_instructions)
current = previous

# Part 1 vars
cycles = 1
tick = [20, 60, 100, 140, 180, 220]
x = 1
strengths = []

# Part 2 vars
CRT_lines = []
beam = ""
beam_cycle = 1

# Main loop
while True:
    # Cycle start
    
    # Part 1:
    signal_strength = cycles * x
    if cycles in tick:
        strengths.append(signal_strength)

    # Part 2:
    if beam_cycle - 1 == x - 1 or beam_cycle - 1 == x or beam_cycle - 1 == x + 1:
        beam += "#"
    else:
        beam += " "
    
    if beam_cycle % 40 == 0:
        # New CRT line
        beam_cycle = 0 
        CRT_lines.append(beam)
        beam = ""
    
    # Execute instruction
    if current != "noop":
        if previous == "addx":
            try:
                x += int(current)
            except ValueError:
                pass

    # End of cycle
    cycles += 1
    beam_cycle += 1

    # Prep next tick
    try:
        previous = current
        current = next(iterator_instructions)
    except StopIteration:
        break

part_1 = sum(i for i in strengths)
print("Part 1 ->", part_1)
print("Part 2:")
for line in CRT_lines:
    print(line)

"""
My image:
####  ##  ###   ##    ## ####   ## ####
   # #  # #  # #  #    # #       #    #
  #  #    ###  #  #    # ###     #   #
 #   #    #  # ####    # #       #  #
#    #  # #  # #  # #  # #    #  # #
####  ##  ###  #  #  ##  #     ##  ####
"""