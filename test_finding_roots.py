import pytest
from finding_roots import bisector, newton_raphson

def test_bisector():
    
    a = -100
    b = 100
    
    expected_roots = -3.1723976135253906
    result = bisector(a, b)
    assert result == expected_roots
    

def test_newton_raphson():

    a = 0.99999999
    expected_roots = -3.1723311745740306
    assert newton_raphson(a) == expected_roots