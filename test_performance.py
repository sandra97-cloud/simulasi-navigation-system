import matplotlib.pyplot as plt
import time
import tracemalloc
import csv

from array_stack import ArrayStack

JUMLAH_DATA = [100, 500, 1000]
JUMLAH_PENGULANGAN = 100


def buat_stack(n):
    """Membuat Stack berisi n data."""
    stack = ArrayStack()

    for i in range(n):
        stack.push(i)

    return stack


def lakukan_operasi(stack, operasi, posisi):
    """Menjalankan operasi penambahan atau penghapusan."""
    n = stack.size()

    if operasi == "Penambahan":
        if posisi == "Depan":
            indeks = 0
        elif posisi == "Tengah":
            indeks = n // 2
        else:
            indeks = n

        stack.insert_at(indeks, -1)

    else:
        if posisi == "Depan":
            indeks = 0
        elif posisi == "Tengah":
            indeks = n // 2
        else:
            indeks = n - 1

        stack.remove_at(indeks)


def ukur_waktu(n, operasi, posisi):
    """Mengukur rata-rata waktu satu operasi."""
    total_waktu = 0

    for _ in range(JUMLAH_PENGULANGAN):
        stack = buat_stack(n)

        mulai = time.perf_counter()
        lakukan_operasi(stack, operasi, posisi)
        selesai = time.perf_counter()

        total_waktu += selesai - mulai

    return total_waktu / JUMLAH_PENGULANGAN


def ukur_memori(n, operasi, posisi):
    """Mengukur memori puncak selama pembuatan Stack dan operasi."""
    tracemalloc.start()

    stack = buat_stack(n)
    lakukan_operasi(stack, operasi, posisi)

    _, memori_puncak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return memori_puncak / 1024


def jalankan_pengujian():
    hasil = []

    for n in JUMLAH_DATA:
        for operasi in ["Penambahan", "Penghapusan"]:
            for posisi in ["Depan", "Tengah", "Belakang"]:

                waktu = ukur_waktu(n, operasi, posisi)
                memori = ukur_memori(n, operasi, posisi)

                if operasi == "Penambahan":
                    jumlah_akhir = n + 1

                    if posisi == "Depan":
                        indeks = 0
                    elif posisi == "Tengah":
                        indeks = n // 2
                    else:
                        indeks = n

                else:
                    jumlah_akhir = n - 1

                    if posisi == "Depan":
                        indeks = 0
                    elif posisi == "Tengah":
                        indeks = n // 2
                    else:
                        indeks = n - 1

                data = {
                    "Jumlah Data Awal": n,
                    "Operasi": operasi,
                    "Posisi": posisi,
                    "Indeks": indeks,
                    "Jumlah Data Setelah Operasi": jumlah_akhir,
                    "Waktu (detik)": waktu,
                    "Memori (KB)": memori
                }

                hasil.append(data)

                print("\n----------------------------------------")
                print("PENGUJIAN", operasi.upper())
                print("----------------------------------------")
                print("Jumlah data awal       :", n)
                print("Posisi                 :", posisi)
                print("Indeks                 :", indeks)
                print("Jumlah data setelahnya :", jumlah_akhir)
                print(f"Waktu eksekusi         : {waktu:.9f} detik")
                print(f"Penggunaan memori      : {memori:.2f} KB")

    # Menyimpan hasil ke file CSV
    with open("hasil_pengujian.csv", "w", newline="",
              encoding="utf-8-sig") as file:
        kolom = hasil[0].keys()
        writer = csv.DictWriter(file, fieldnames=kolom)
        writer.writeheader()
        writer.writerows(hasil)

    print("\n========================================")
    print("PENGUJIAN SELESAI")
    print("Total skenario:", len(hasil))
    print("Hasil disimpan di hasil_pengujian.csv")
    print("========================================")

    return hasil


def tampilkan_grafik(hasil):
    jumlah_data = [100, 500, 1000]
    posisi = ["Depan", "Tengah", "Belakang"]

    # GRAFIK 1: PERBANDINGAN WAKTU EKSEKUSI
    fig, axes = plt.subplots(1, 3, figsize=(13, 5))

    for ax, n in zip(axes, jumlah_data):
        tambah = [
            next(d["Waktu (detik)"] * 1_000_000 for d in hasil
                 if d["Jumlah Data Awal"] == n
                 and d["Operasi"] == "Penambahan"
                 and d["Posisi"] == p)
            for p in posisi
        ]

        hapus = [
            next(d["Waktu (detik)"] * 1_000_000 for d in hasil
                 if d["Jumlah Data Awal"] == n
                 and d["Operasi"] == "Penghapusan"
                 and d["Posisi"] == p)
            for p in posisi
        ]

        x = range(3)
        lebar = 0.35

        ax.bar(
            [i - lebar / 2 for i in x],
            tambah,
            lebar,
            label="Penambahan"
        )

        ax.bar(
            [i + lebar / 2 for i in x],
            hapus,
            lebar,
            label="Penghapusan"
        )

        ax.set_xticks(list(x), posisi)
        ax.set_title(f"{n} Data")
        ax.set_ylabel("Waktu (mikrodetik)")
        ax.legend()
        ax.grid(axis="y", alpha=0.3)

    fig.suptitle("Grafik Perbandingan Waktu Eksekusi")
    fig.tight_layout()

    # Menyimpan gambar grafik waktu
    plt.savefig("grafik_waktu.png", dpi=300, bbox_inches="tight")
    print("Grafik waktu disimpan di grafik_waktu.png")

    plt.show()
    plt.close(fig)

    # GRAFIK 2: PERBANDINGAN PENGGUNAAN MEMORI
    fig, axes = plt.subplots(1, 3, figsize=(13, 5))

    for ax, n in zip(axes, jumlah_data):
        tambah = [
            next(d["Memori (KB)"] for d in hasil
                 if d["Jumlah Data Awal"] == n
                 and d["Operasi"] == "Penambahan"
                 and d["Posisi"] == p)
            for p in posisi
        ]

        hapus = [
            next(d["Memori (KB)"] for d in hasil
                 if d["Jumlah Data Awal"] == n
                 and d["Operasi"] == "Penghapusan"
                 and d["Posisi"] == p)
            for p in posisi
        ]

        x = range(3)
        lebar = 0.35

        ax.bar(
            [i - lebar / 2 for i in x],
            tambah,
            lebar,
            label="Penambahan"
        )

        ax.bar(
            [i + lebar / 2 for i in x],
            hapus,
            lebar,
            label="Penghapusan"
        )

        ax.set_xticks(list(x), posisi)
        ax.set_title(f"{n} Data")
        ax.set_ylabel("Memori (KB)")
        ax.legend()
        ax.grid(axis="y", alpha=0.3)

    fig.suptitle("Grafik Perbandingan Penggunaan Memori")
    fig.tight_layout()

    # Menyimpan gambar grafik memori
    plt.savefig("grafik_memori.png", dpi=300, bbox_inches="tight")
    print("Grafik memori disimpan di grafik_memori.png")

    plt.show()
    plt.close(fig)


# PROGRAM UTAMA
if __name__ == "__main__":
    hasil = jalankan_pengujian()
    tampilkan_grafik(hasil)