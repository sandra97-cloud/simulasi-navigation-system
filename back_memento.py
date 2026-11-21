
from array_stack import ArrayStack


class Memento:
    """Menyimpan kondisi halaman browser."""

    def __init__(self, halaman):
        self.halaman = halaman

    def get_state(self):
        return self.halaman


class BackMemento:
    """Mengelola riwayat halaman untuk fitur Back."""

    def __init__(self):
        self.history = ArrayStack()

    def save_state(self, halaman):
        """Menyimpan halaman ke riwayat."""
        memento = Memento(halaman)
        self.history.push(memento)

    def back(self):
        """Mengembalikan halaman sebelumnya."""
        if self.history.is_empty():
            return None

        memento = self.history.pop()
        return memento.get_state()

    def is_empty(self):
        return self.history.is_empty()
