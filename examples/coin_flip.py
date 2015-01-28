from random import randint
from montecarlo import montecarlo

def flip_is_heads(g):
    return randint(0, 1) == 0

mc = montecarlo(flip_is_heads)
result = mc.run()
print "Result returned: " + str(result)