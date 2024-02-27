from harv19 import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Roy"]:
        assert hello(name) == f"hello, {name}"