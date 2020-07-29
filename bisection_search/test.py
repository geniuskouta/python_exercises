x = 25
epsilon = 0.01
numGuesses = 0
low = 0
high = max(1.0, x)
answer = (high + low)/2.0

while abs(answer**2 - x) >= epsilon:
    print('low: ', low, 'high: ', high)
    numGuesses += 1
    if answer**2 < x:
        low = answer  # store the low value at the moment
    else:
        high = answer
    answer = (high + low)/2.0 # make half the total of high and low
print('numGuesses', numGuesses)
print(answer, 'is close to square root of', x)
