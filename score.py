def calPoints(ops) -> int:
    """
    type ops: List[str] - List of Operators
    rtype: int - Sum of scores after performing all operations 
    """
    scoreset = range(100)
    result = 0

    scores = list()
    print(ops)

    for value in ops:
        print("Value is {}".format(value))
        print(type(value) == int)
        print(value == "c")
        print(value == "d")
        print(value == "+")

        if type(value) == int:
            print("int detected")
            scores.append(value)    

        elif value == "c":
            print("C detected")
            scores.pop()

        elif value == "d":
            lenscore = len(scores)
            print("D score length is {}".format(lenscore))
            scores.append(scores[lenscore - 1] * 2)

        elif value == "+":
            lenscore = len(scores)
            print("+ score length is {}".format(lenscore))
            scores.append(scores[lenscore - 1] + scores[lenscore - 2])

        print(scores)

    for score in scores:
        result += score

    return result



if __name__ == '__main__':
    # line = input()
    # ops = list(line)
    # ops = line.strip().split()
    # ops = line.split()
    # ops = [5, 2, "c", "d", "+"]  
    line = input()
    ops = list(line) 

    print(calPoints(ops))