from back_memento import BackMemento
from forward import Forward


class Browser:
    """Mengelola simulasi navigasi browser."""

    def __init__(self):
        self.current_page = None
        self.back_history = BackMemento()
        self.forward_history = Forward()

    def visit(self, halaman):
        """Mengunjungi halaman baru."""
        if self.current_page is not None:
            self.back_history.save_state(self.current_page)

        self.current_page = halaman
        self.forward_history = Forward()

        print("Mengunjungi:", self.current_page)

    def back(self):
        """Kembali ke halaman sebelumnya."""
        if self.back_history.is_empty():
            print("Tidak ada halaman sebelumnya.")
            return

        self.forward_history.save_state(self.current_page)
        self.current_page = self.back_history.back()

        print("Kembali ke:", self.current_page)

    def forward(self):
        """Maju ke halaman berikutnya."""
        if self.forward_history.is_empty():
            print("Tidak ada halaman berikutnya.")
            return

        self.back_history.save_state(self.current_page)
        self.current_page = self.forward_history.forward()

        print("Maju ke:", self.current_page)

    def show_current_page(self):
        """Menampilkan halaman saat ini."""
        print("Halaman saat ini:", self.current_page)

    def show_history(self):
        """Menampilkan riwayat Back dan Forward."""
        print("Riwayat Back:", self.back_history.history.display())
        print("Riwayat Forward:", self.forward_history.display())


if __name__ == "__main__":
    browser = Browser()

    print("=== SIMULASI NAVIGASI BROWSER ===")

    browser.visit("Google")
    browser.visit("YouTube")
    browser.visit("Facebook")

    print("\n=== PENGUJIAN BACK ===")
    browser.back()

    print("\n=== PENGUJIAN FORWARD ===")
    browser.forward()

    print("\n=== HALAMAN SAAT INI ===")
    browser.show_current_page()

    print("\n=== RIWAYAT BROWSER ===")
    browser.show_history()