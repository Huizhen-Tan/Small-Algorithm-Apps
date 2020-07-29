"""
This code randomly and repeatly gives you four cards, and you can take your time to come up with a way, using only operators (+,-,*,/) to get 24 points.
Press q to quit, and others to see the answer and continue.
Note that calculations in the answer is from left to right without operator priority.
"""

from itertools import permutations, product
from random import sample

def valid(num, case):
    """
    num: [1,2,3,12]
    case: (1,2,3) as (+,-,*)
    """
    dic = {1:'A',11:'J',12:'Q',13:'K'}
    ans = num[0]
    string = str(ans) if ans not in dic else dic[ans]
    for index, op in enumerate(case):
        if op == 1:
            ans += num[index+1]
            string = string + '+'
        elif op == 2:
            ans -= num[index+1]
            string = string + '-'
        elif op == 3:
            ans *= num[index+1]
            string = string + '*'
        elif op == 4:
            ans /= num[index+1]
            string = string + '/'
        q = str(num[index+1]) if num[index+1] not in dic else dic[num[index+1]]
        string = string + q
    if ans == 24:
        return (1, string)
    return (0,None)

def valid2(cards):
    operator = product([1,2,3,4],repeat=3)
    d = []
    for num_case in permutations(cards,4):
        if num_case not in d:
            d.append(num_case)
            for op_case in operator:
                validation = valid(num_case,op_case)
                if validation[0]==1:
                    return validation[1]
    return None

while 1:
    SAMPLE = sample(['A','J','Q','K']+[str(i) for i in range(2,11)],4) #['3', '2', 'A', 'Q']
    cards = list(map(int,' '.join(SAMPLE).replace('J','11').replace('Q','12').replace('K','13').replace('A','1').split())) #[3,2,1,12]
    VALID = valid2(cards)
    if VALID:
        print(' '.join(SAMPLE))
        if input() == 'q':
            print(VALID)
            print('---------')
            break
        else:
            print(VALID)
            print('---------')



