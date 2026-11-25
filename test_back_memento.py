from back_memento import BackMemento

back = BackMemento()

print("=== PENGUJIAN BACK MEMENTO ===")

print("\n1. Pengujian Back Saat Kosong")
print("Halaman sebelumnya:", back.back())
print("Apakah kosong?", back.is_empty())