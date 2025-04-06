# Birthday Problem
# d = num possible outcomes, ex 16 chars ** strlen
# prob = probability of collision
# Outputs num samples, ex num strings generated, to get that prob of collision.

# Seems hex string len 14 is magic number for no collisions

import math

d = input("Please give num possible outcomes: ")
prob = float(input("Please give probability (0 to 1) of collision: "))

# Allow simple math expressions like 16 ** 5 for example to be given for d.
d = eval(d)


# At d + 1, some outcome must repeat due to finite outcomes.
if prob == 1.0:
    print("Collision is guaranteed after the following number of samples: ", end="")
    print(d + 1)
else:
    print("Expect the given probability of collision after the following number of samples: ", end="")
    print(math.ceil((1 + math.sqrt(1 + 8 * math.log(1 - prob) / math.log((d - 1) / d))) / 2))

