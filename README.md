# pymontecarlo
A small Python library for creating simple Monte Carlo simulations.

## Installation
```bash
pip install montecarlo
```

## Usage
(Under construction)
```python
from montecarlo import montecarlo

def setup():
    ...

def test():
    if (...):
        return True
    return False

mc = montecarlo(func, setup=setup)
mc.run(iterations=100000)
```
