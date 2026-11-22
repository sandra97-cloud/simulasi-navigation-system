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
