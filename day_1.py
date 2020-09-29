# Calculate quartiles
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


# Calculate Standard Deviation

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


#Calculate interquantile
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