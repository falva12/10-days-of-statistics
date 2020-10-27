#%%
#Task1. In a single toss of 2 fair (evenly-weighted) six-sided dice,
# find the probability that their sum will be at most 9.

def dice_probability(dice1, dice2, n):
    permut = []

    for s1 in dice1:
        for s2 in dice2:
            permut.append(s1+s2)
    
    numerador = 0
    denominador = len(permut)
    for comb in permut:
        if comb<=n: numerador+=1
    
    return numerador/denominador
    
dice1 = range(1, 7)
dice2 = range(1, 7)

dice_probability(dice1, dice2, 9)

#%%
#Task2. In a single toss of 2 fair (evenly-weighted) six-sided dice,
# find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

def prob_2_dices(num: int, how: str ="at most"):
    

    '''

    num [int]: sum of values of 2 dices that you want to calculate the probability

    how [string]: could be "at most", "at least" "more than", "less than", "equal"

    '''

    dice1 = range(1, 7)
    dice2 = range(1, 7)

    count = 0
    count_true = 0

    for n1 in dice1:

        for n2 in dice2:

            sum_dices = n1 + n2

            if sum_dices <= num and how == "at most":
                count_true += 1
            elif sum_dices < num and how == "less than":
                count_true += 1
            elif sum_dices > num and how == "more than":
                count_true += 1
            elif sum_dices >= num and how == "at least":
                count_true += 1
            elif sum_dices == num and how == "equal":
                count_true += 1

            count += 1

    return (count_true / count)


print(  prob_2_dices(6, how="equal") )

#%%
#Task3. There are 3 urns labeled X, Y, and Z.
# -Urn X contains 4 red balls and 3 black balls.
# -Urn Y contains 5 red balls and 4 black balls.
# -Urn Z contains 4 red balls and 4 black balls.
# One ball is drawn from each of the 3 urns.
# What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

import pandas as pd

urns = pd.DataFrame(data=[[4, 3], [5, 4], [4, 4]]
                    , index=['X', 'Y', 'Z']
                    , columns=['red', 'black'])

urns['p_red'] = urns['red']/(urns['red']+ urns['black'])
urns['p_black'] = 1-urns['p_red']

P = urns.loc['X','p_red'] * urns.loc['Y','p_red'] * urns.loc['Z','p_black'] \
    + urns.loc['Z','p_red'] * urns.loc['X','p_red'] * urns.loc['Y','p_black']\
    + urns.loc['Y','p_red'] * urns.loc['Z','p_red'] * urns.loc['X','p_black']
P


def filledOrders(order, k):
    # Write your code here
    result=0
    count=0
    print(k, len(order))
    for o in order:
        count+=1
        if o<=k: result+=1
        print(o, o<=k, result)
    return result