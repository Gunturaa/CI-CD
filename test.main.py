from main import tambah, greet

def test_tambah():
    assert tambah(2, 3) == 5
    assert tambah(-1, 1) == 0
    assert tambah(0, 0) == 0
    assert tambah(10, 5) == 15

def test_greet():
    assert greet("Guntur") == "Hello, Guntur! Welcome to CI/CD."
    assert greet("World") == "Hello, World! Welcome to CI/CD."
