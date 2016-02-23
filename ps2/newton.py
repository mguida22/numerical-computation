#!/usr/bin/env python3

THRESHOLD = 0.0001;
MAX_TRIES = 100;
guess_a = -1;

def f(x):
    # replace with function
    return x

i = 0;
while (i < MAX_TRIES):
    guess_b = guess_a - (f(guess_a) / cos(guess_a))

    if (f(guess_b) > 0 - THRESHOLD) && (f(guess_b) < 0 + THRESHOLD):
        print(f(guess_b))
        print(guess_b)
        print(i)
        print('finished')
        break

    guess_a = guess_b
    i += i

print('couldn\'t solve in ' + MAX_TRIES + ' iterations)
