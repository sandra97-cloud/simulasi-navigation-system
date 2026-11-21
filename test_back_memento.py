
from back_memento import BackMemento

back = BackMemento()
print("\n5. Pengujian Back Saat Kosong")
print("Halaman sebelumnya:", back.back())
print("Hasil:", back.back())
print("Apakah kosong?", back.is_empty())