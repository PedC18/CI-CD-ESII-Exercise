from calculator import calculator

c = calculator()

def test_soma():
    assert (c.soma(4,5) == 9)

def test_sub():
    assert (c.sub(4,5) == -1)

def test_multi():
    assert (c.multi(4,5) == 20)

def test_div():
    assert(c.div(4.0,5.0) == 0.8)

def test_div_by_zero():
    assert(c.div(4,0) == "error, can't divide by zero")

def test_power():
    assert(c.power(4,5) == 1024)


