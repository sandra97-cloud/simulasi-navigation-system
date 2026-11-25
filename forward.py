from array_stack import ArrayStack


class Forward:
    """Mengelola riwayat halaman untuk fitur Forward."""

    def __init__(self):
        self.history = ArrayStack()

    def save_state(self, halaman):
        """Menyimpan halaman ke riwayat Forward."""
        self.history.push(halaman)

    def forward(self):
        """Mengambil halaman berikutnya."""
        if self.history.is_empty():
            return None

        return self.history.pop()

    def is_empty(self):
        """Memeriksa apakah riwayat Forward kosong."""
        return self.history.is_empty()

    def display(self):
        """Menampilkan isi riwayat Forward."""
        return self.history.display()


if __name__ == "__main__":
    forward = Forward()

    forward.save_state("Google")
    forward.save_state("YouTube")
    forward.save_state("Facebook")

    print("=== PENGUJIAN FORWARD ===")
    print("Isi riwayat:", forward.display())
    print("Halaman berikutnya:", forward.forward())
    print("Halaman berikutnya:", forward.forward())
    print("Sisa riwayat:", forward.display())
