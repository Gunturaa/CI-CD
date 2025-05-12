def tambah(a, b):
    return a + b

def greet(nama):
    return f"Hello, {nama}! Welcome to CI/CD."

if __name__ == "__main__":
    hasil = tambah(5, 3)
    sapaan = greet("Guntur")

    print(f"Hasil tambah: {hasil}")
    print(sapaan)
