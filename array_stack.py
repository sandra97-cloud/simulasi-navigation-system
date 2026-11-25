class ArrayStack:
    """Kelas Stack menggunakan Array."""

    def __init__(self):
        self.data = []

    def push(self, item):
        """Menambahkan data di bagian belakang."""
        self.data.append(item)

    def pop(self):
        """Menghapus data paling belakang."""
        if self.is_empty():
            return None
        return self.data.pop()

    def insert_at(self, index, item):
        """Menambahkan data pada posisi tertentu."""
        if index < 0 or index > self.size():
            return False
        self.data.insert(index, item)
        return True

    def remove_at(self, index):
        """Menghapus data pada posisi tertentu."""
        if index < 0 or index >= self.size():
            return None
        return self.data.pop(index)

    def peek(self):
        """Melihat data paling atas."""
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def display(self):
        return self.data.copy()
