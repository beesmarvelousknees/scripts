# Birthday Problem
# n = num samples, ex num strings generated
# d = num possible outcomes, ex 16 chars ** strlen
# Outputs the probability of collision.

# This example says, try 100k hex keys of length 8 chars and get prob of collision.
# Seems hex string len 14 is magic number for no collisions btw
#n = 1000000
#d = 16 ** 8  

n = 100000
d = 16 ** 8  

prob = 1 - ((d - 1)/d) ** ((n*(n-1))/2)

print(f"{prob*100}%")
