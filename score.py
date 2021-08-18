def calPoints(ops) -> int:
    """
    type ops: List[str] - List of Operators
    rtype: int - Sum of scores after performing all operations 
    """

    result = 0

    scores = list()

    for value in ops:
        if value == 'c' or value == 'C' or value == 'd' or value == 'D' or value == '+':
            if value == "c" or value == "C":
                if len(scores) < 1:
                    continue

                else:
                    scores.pop()

            elif value == "d" or value == "D":
                if len(scores) < 1:
                    continue

                else:
                    lenscore = len(scores)
                    scores.append(scores[lenscore - 1] * 2)

            elif value == "+":
                if len(scores) < 2:
                    continue
                
                else:
                    lenscore = len(scores)
                    scores.append(scores[lenscore - 1] + scores[lenscore - 2])
        
        else:
            value = int(value)
            scores.append(value)

    for score in scores:
        result += score

    return result
         
if __name__ == '__main__':
    while True:
        line = input()
        ops = line.strip().split()
        print(calPoints(ops))
