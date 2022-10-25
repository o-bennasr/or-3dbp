from py3dbp import Packer, Bin, Item
import pytest

def test_one_bin_one_item():
    packer = Packer()

    packer.add_bin(Bin('large-2-box', 23.6875, 11.75, 3.0, 70.0))

    packer.add_item(Item('50g [powder 1]', 3.9370, 1.9685, 1.9685, 1))

    packer.pack()

    assert len(packer.bins) == 1

"""
import py3dbp
print(py3dbp.__file__) #TODO Customize the implementation to use pulp
# "/home/oussema/anaconda3/lib/python3.9/site-packages/py3dbp/__init__.py"
"""

