from calculator import calculator

def test_soma():
    c = calculator()
    assert (c.soma(4,5) == 9)