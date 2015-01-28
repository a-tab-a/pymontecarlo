# pymontecarlo
A small Python library for creating simple Monte Carlo simulations.

## Installation
```bash
pip install montecarlo
```

## Usage
(See examples directory for more examples)
```python
from random import randint
from montecarlo import montecarlo

def flip_coin(g):
    if randint(0, 1) == 0:
        return True
    return False

mc = montecarlo(flip_coin)
mc.run()
```
