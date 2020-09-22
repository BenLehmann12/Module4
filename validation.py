
def average(score1,score2,score3):
    NUMBER_TESTS = 3
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    return float((score1+score2+score3)/NUMBER_TESTS)

if __name__ == '__main__':
    print(average(80,70,90))
