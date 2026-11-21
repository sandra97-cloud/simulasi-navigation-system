
class ArrayStack:
    """Kelas Stack menggunakan Array."""

    def __init__(self):
        self.data = []

    def push(self, item):
        """Menambahkan halaman ke Stack."""
        self.data.append(item)

    def pop(self):
        """Menghapus dan mengambil halaman paling atas."""
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        """Melihat halaman paling atas."""
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        """Memeriksa apakah Stack kosong."""
        return len(self.data) == 0

    def size(self):
        """Menghitung jumlah halaman."""
        return len(self.data)

    def display(self):
        """Menampilkan isi Stack."""
        return self.data.copy()

from array_stack import ArrayStack

# Membuat objek ArrayStack
stack = ArrayStack()

print("=== PENGUJIAN ARRAY STACK ===")

# 1. Pengujian push
print("\n1. Pengujian Push")
stack.push("Google")
stack.push("YouTube")
stack.push("Facebook")
print("Isi Stack:", stack.display())

# 2. Pengujian peek
print("\n2. Pengujian Peek")
print("Data paling atas:", stack.peek())

# 3. Pengujian pop
print("\n3. Pengujian Pop")
print("Data yang diambil:", stack.pop())
print("Isi Stack:", stack.display())

# 4. Pengujian is_empty
print("\n4. Pengujian Is Empty")
print("Apakah Stack kosong?", stack.is_empty())

# 5. Pengujian size
print("\n5. Pengujian Size")
print("Jumlah data:", stack.size())

# 6. Pengujian Stack kosong
print("\n6. Pengujian Stack Kosong")
stack.pop()
stack.pop()
print("Isi Stack:", stack.display())
print("Apakah Stack kosong?", stack.is_empty())
print("Jumlah data:", stack.size())

# 7. Pengujian pop saat kosong
print("\n7. Pengujian Pop Saat Kosong")
print("Hasil Pop:", stack.pop())

# 8. Pengujian peek saat kosong
print("\n8. Pengujian Peek Saat Kosong")
print("Hasil Peek:", stack.peek())