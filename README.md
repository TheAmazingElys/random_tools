# Random Tools

[![Build Status](https://api.travis-ci.org/rallesiardo/random_tools.svg?branch=master)](https://travis-ci.org/rallesiardo/random_tools)
[![PyPI version](https://badge.fury.io/py/random-tools.svg)](https://badge.fury.io/py/random-tools)


## random_tools.Signal

```python
from random_tools import Signal

on_event = Signal()
on_event.connect(print)
on_event.emit("this will be printed")

```

## random_tools.true_every

```python
from random_tools import true_every

this_true_every_3_calls = true_every(3) # will return True every 3 calls

false_1 = next(this_true_every_3_calls) # False
false_2 = next(this_true_every_3_calls) # False

true_1 = next(this_true_every_3_calls) # True

false_3 = next(this_true_every_3_calls) # False
false_4 = next(this_true_every_3_calls) # False

true_2 = next(this_true_every_3_calls) # True

```
