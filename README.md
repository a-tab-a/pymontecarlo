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
