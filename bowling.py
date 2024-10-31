def divide_into_rounds(n_rounds, throws):
    round_throws = []
    current_round = []

    for i in range(len(throws)):
        current_round.append(throws[i])
        # Strike
        if throws[i] == 10:
            round_throws.append(current_round)
            current_round = []
        elif len(current_round) == 2:
            round_throws.append(current_round)
            current_round = []

        if i == len(throws) -1:
            round_throws.append(current_round)

    while len(round_throws) > n_rounds:
        round_throws[-2] = round_throws[-2] + round_throws[-1]
        del round_throws[-1]

    return round_throws

def solve(round_throws):
    scores = [0 for i in range(len(round_throws))]

    # Calculate individual scores
    for i in range(len(round_throws)):# - 1, -1, -1):
        round_score = sum(round_throws[i])

        # Strike
        if round_score == 10 and len(round_throws[i]) == 1:
            # If there was a next round
            if i + 1 < len(round_throws):
                # 1st throw
                round_score += round_throws[i + 1][0]

                # 2nd throw
                if len(round_throws[i + 1]) > 1:
                    round_score += round_throws[i + 1][1]
                else:
                    # If there was a next (next) round
                    if i + 2 < len(round_throws):
                        round_score += round_throws[i + 2][0]
        
        # Spare
        elif round_score == 10:
            # If there was a next round
            if i + 1 < len(round_throws):
                round_score += round_throws[i + 1][0]

        # Neither
        scores[i] = round_score

    #print(scores)

    # Sum the scores of the previous round
    for i in range(1, len(round_throws)):
        scores[i] = scores[i] + scores[i-1]

    return scores

if __name__ == '__main__':
    raw_input = input("Input:")
    arguments = raw_input.split(":")
    n_rounds = int(arguments[0])
    throws = [int(v) for v in arguments[1].split(",")]

    round_throws = divide_into_rounds(n_rounds, throws)
    #print(round_throws)

    round_scores = solve(round_throws)
    round_scores_s = [str(v) for v in round_scores]

    output = ",".join(round_scores_s)
    print(output)
