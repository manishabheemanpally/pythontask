# test_script.py

import script

def test_add():
    """
    Test the add function with various inputs.
    """
    assert script.add(1, 2) == 3
    assert script.add(-1, 1) == 0
    assert script.add(0, 0) == 0
    assert script.add(100, 200) == 300
    assert script.add(-5, -5) == -10
