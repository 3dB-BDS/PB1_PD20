import app


def test_saskaitit_pozitivi():
    assert app.saskaitit(2, 3) == 5


def test_saskaitit_negativi():
    assert app.saskaitit(-4, -6) == -10


def test_saskaitit_ar_nulli():
    assert app.saskaitit(0, 7) == -7 # intentional error for testing
