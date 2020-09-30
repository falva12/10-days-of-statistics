#%%
#Task1. Given an array, X, of n integers, calculate the respective first quartile (Q1)
#, second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

def custom_median(numbers) :

    numbers = sorted(numbers)
    middle = len(numbers)//2

    if len(numbers)%2 == 0:
        return (numbers[middle-1]+numbers[middle])/2 
    else:
        return numbers[middle]

def custom_quartiles(numbers) :
    numbers = sorted(numbers)
    middle = len(numbers)//2
    lower = numbers[:middle]

    if len(numbers)%2 == 0:
        upper = numbers[middle:]
    else:
        upper = numbers[middle+1:]

    return int(custom_median(lower)), int(custom_median(numbers)), int(custom_median(upper))


x = 9
numbers = [3, 7, 8, 5, 12, 14, 21, 13, 18]

for n in custom_quartiles(numbers):
    print(n)

#%%
#Task2. The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles.
# Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements,
# construct a data set, S, where each xi occurs at frequency fi.
# Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place.

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

def create_repnumbers(numbers, reps):
    lst = []
    for n, r in zip(numbers, reps):
        for i in range(r):
            lst.append(n)
    return lst

def custom_interquartiles(numbers) :
    numbers = sorted(numbers)
    middle = len(numbers)//2
    lower = numbers[:middle]

    if len(numbers)%2 == 0:
        upper = numbers[middle:]
    else:
        upper = numbers[middle+1:]

    return round(float(custom_median(upper) - custom_median(lower)),1)


numbers = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8
    , 9, 10, 20, 10, 40, 30, 50, 20, 10, 40, 30, 50]
reps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10
        , 40, 30, 50, 20, 10, 40, 30, 50, 20]

rep_numbers = create_repnumbers(numbers, reps)
custom_interquartiles(rep_numbers)

#%%
#Task3. Given an array, X, of N integers, calculate and print the standard deviation.
# Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format).
# An error margin of +/-0.1 will be tolerated for the standard deviation.

def custom_median(numbers) :
        
    numbers = sorted(numbers)
    middle = len(numbers)//2

    if len(numbers)%2 == 0:
        return (numbers[middle-1]+numbers[middle])/2 
    else:
        return numbers[middle]

def custom_mean (numbers):
    return sum(numbers)/ len(numbers)

def custom_std_dev(numbers):

    mean = custom_mean(numbers)
    numerator = sum( (x - mean) ** 2 for x in numbers)
    denominator = len(numbers)
    return (numerator/denominator)**(1/2)

x = 5
numbers = [10, 40, 30, 50, 20]

print(custom_std_dev(numbers))