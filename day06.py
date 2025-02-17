import random

def guess_number(low, high, answer, chance) -> int:
    mid =  (low+high) // 2
    print(f'Guess number is {mid}')
    fp.write(f'Guess number is {mid}\n')


    while chance != 0:
        if mid == answer:
            print(f'You win. Answer is {answer}')
            fp.write(f'You win. Answer is {answer}\n')
            return
        elif mid > answer:
            chance = chance - 1
            print(f'{mid} is bigger. Chance left : {chance}')
            fp.write(f'{mid} is bigger. Chance left : {chance}\n')
            return guess_number(low, mid, answer, chance) #mid가 크므로 상한에 mid를 배정, mid-1을 하는 이유는 어차피 mid가 답이 아니므로 상한을 -1해도 상관없음
        else:
            chance = chance - 1
            print(f'{mid} is lower. Chance left : {chance}')
            fp.write(f'{mid} is lower. Chance left : {chance}\n')
            return guess_number(mid, high, answer, chance)
    else:
        print(f'You lost. Answer is {answer}')
        fp.write(f'You lost. Answer is {answer}')


if __name__ == "__main__":
    low = 1
    high = 100
    chance = 7
    answer = random.randint(low, high)
    with open('guess.txt', 'w') as fp:
        guess_number(low, high, answer, chance)