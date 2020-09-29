# %%
# Calculate the mean, median and mode
def custom_mean (numbers):
    return sum(numbers)/ len(numbers)

def custom_median (numbers):
    numbers.sort()
    middle = len(numbers)//2

    if len(numbers)%2 == 0:
        return (numbers[middle-1]+numbers[middle])/2 
    else:
        return numbers[middle]

def custom_mode (numbers):

    dicct = dict()
    for n in numbers:
        try: dicct[n] += 1
        except: dicct[n] = 1
    
    key = 0
    val = -1
    for k, v in dicct.items():
       if v > val:
           key = k
           val = v
       elif (v == val) & (k < key): key = k
    
    return key

#x = int(input())
#numbers = list(map(int, input().split()))
x = 10
numbers = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]   

mean = custom_mean(numbers)
median = custom_median(numbers)
mode = custom_mode(numbers)

print(mean, median, mode
,sep = '\n')


# %%
# Calculate the weighted mean
x = 5
numbers = [10, 40, 30, 50, 20]
weights = [1, 2, 3, 4, 5]

def custom_wmean (numbers, weights) :
    numerador = []
    for x, y in zip(numbers, weights):
        numerador.append(x*y)
    
    res = round(sum(numerador)/ sum(weights), 1)
    return res

print(custom_wmean(numbers, weights))
