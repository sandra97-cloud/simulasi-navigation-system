from forward import Forward

forward = Forward()

print("=== PENGUJIAN FORWARD ===")

print("\n1. Pengujian Save State")
forward.save_state("Google")
forward.save_state("YouTube")
forward.save_state("Facebook")
print("Isi riwayat:", forward.display())

print("\n2. Pengujian Forward")
print("Halaman berikutnya:", forward.forward())
print("Halaman berikutnya:", forward.forward())

print("\n3. Pengujian Is Empty")
print("Apakah kosong?", forward.is_empty())

print("\n4. Pengujian Size")
print("Jumlah data:", forward.history.size())

print("\n5. Pengujian Forward Saat Kosong")
print("Hasil:", forward.forward())
