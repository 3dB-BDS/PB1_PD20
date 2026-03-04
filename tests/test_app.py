import app


def test_saskaitit_pozitivi():
    assert app.saskaitit(2, 3) == 5


def test_saskaitit_negativi():
    assert app.saskaitit(-4, -6) == -10


def test_saskaitit_ar_nulli():
    assert app.saskaitit(0, 7) == 7


def test_atnemt_pozitivi():
    assert app.atnemt(7, 3) == 4


def test_atnemt_negativi():
    assert app.atnemt(-4, -6) == 2


def test_atnemt_ar_nulli():
    assert app.atnemt(0, 7) == -7
