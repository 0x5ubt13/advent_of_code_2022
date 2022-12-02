def calculate_score_part1(opp, me, score):
    if me == 'X':
        score += 1
        if opp == 'C':
            score += 6
        if opp == 'A':
            score += 3
        
    if me == 'Y':
        score += 2
        if opp == 'A':
            score += 6
        if opp == 'B':
            score += 3

    if me == 'Z':
        score += 3
        if opp == 'B':
            score += 6
        if opp == 'C':
            score += 3

    return score


def calculate_score_part2(opp, me, score):
    if me == 'X':
        if opp == 'A':
            score += 3
        if opp == 'B':
            score += 1
        if opp == 'C':
            score += 2
    if me == 'Y':
        score += 3
        if opp == 'A':
            score += 1
        if opp == 'B':
            score += 2
        if opp == 'C':
            score += 3
    if me == 'Z':
        score += 6
        if opp == 'A':
            score += 2
        if opp == 'B':
            score += 3
        if opp == 'C':
            score += 1

    return score


def solve():
    score1, score2 = 0, 0
    with open("./day_02/input.txt", "r") as f:
        for line in f:
            l = line.strip().split(" ")
            score1 = calculate_score_part1(l[0], l[1], score1)
            score2 = calculate_score_part2(l[0], l[1], score2)
            
    return score1, score2


def main():
    print(solve())


if __name__ == '__main__':
    main()
