from random import randint
from montecarlo import montecarlo

def flip_coin(g):
    return randint(0, 1) == 0

mc = montecarlo(flip_coin)
result = mc.run()
print "Result returned: " + str(result)