
def test_greeting():
    name = "Анна"
    age = 25

    output = f"Привет, {name}! Тебе {age} лет."
    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)


def test_rectangle():
    a = 10
    b = 20

    perimeter = a * 2 + b * 2
    assert perimeter == 60

    area = a * b
    assert area == 200


def test_circle():
    import math
    r = 23

    area = math.pi * r ** 2
    assert area == 1661.9025137490005
    print(area)

    length = (math.pi * r) * 2
    assert length == 144.51326206513048
    print(length)

def test_random_list():
    import random

    l = random.sample(range(1, 101), 10)
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    unique_l = set(l)
    l = list(unique_l)
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():

    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    dict(zip(first, second))

    d = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5
    }

    assert isinstance(d, dict)
    assert len(d) == 5
    print(d)