# pymontecarlo
A small Python library for creating simple Monte Carlo simulations.

## Installation
```bash
pip install montecarlo
```

## Usage
(See examples directory for more examples)
```python
from montecarlo import montecarlo
from random import randint

def flip_is_heads(g):
    return randint(0, 1) == 0

mc = montecarlo(flip_coin)
mc.run()
```

Output:
```
Iteration #10000: 0.5079
Iteration #20000: 0.50485
Iteration #30000: 0.5059
Iteration #40000: 0.50295
Iteration #50000: 0.5016
...
Iteration #970000: 0.499608247423
Iteration #980000: 0.499712244898
Iteration #990000: 0.499737373737
Iteration #1000000: 0.499728
======================
======= FINAL ========
======================
Iteration #1000000: 0.499728
```