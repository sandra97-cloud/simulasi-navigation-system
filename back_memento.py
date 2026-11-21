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

if __name__ == "__main__":
    back = BackMemento()

    back.save_state("Halaman 1")
    back.save_state("Halaman 2")
    back.save_state("Halaman 3")

    print("Halaman sebelumnya:", back.back())
    print("Halaman sebelumnya:", back.back())
    print("Jumlah riwayat tersisa:", back.history.size())