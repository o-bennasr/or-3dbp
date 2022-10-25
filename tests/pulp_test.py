import pytest
from pulp import LpVariable, LpProblem, LpMinimize, value

def test_basic_lp():
    x = LpVariable("x", 0, 3)

    y = LpVariable("y", 0, 1)

    prob = LpProblem("myProblem", LpMinimize)

    prob += x + y <= 2

    prob += -4*x + y

    status = prob.solve()

    assert value(x) == 2 and value(y) == 0

"""    
import pulp
print(pulp.__file__)
"/home/oussema/anaconda3/lib/python3.9/site-packages/pulp/__init__.py"
"""

