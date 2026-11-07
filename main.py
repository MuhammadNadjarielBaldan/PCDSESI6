
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("hasil_transformasi", exist_ok=True)

# 1. Membaca gambar asli
img = cv2.imread("harley.jpg")

if img is None:
    print("Gambar tidak ditemukan! Periksa nama file.")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

tinggi, lebar = img.shape[:2]

matriks = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

translation = cv2.warpAffine(
    img, matriks, (lebar, tinggi)
)

scaling_05 = cv2.resize(
    img, None, fx=0.5, fy=0.5
)

scaling_2 = cv2.resize(
    img, None, fx=2, fy=2
)


def rotasi_gambar(gambar, sudut):
    h, w = gambar.shape[:2]
    pusat = (w // 2, h // 2)

    matriks = cv2.getRotationMatrix2D(
        pusat, sudut, 1.0
    )

    cos = abs(matriks[0, 0])
    sin = abs(matriks[0, 1])

    lebar_baru = int(h * sin + w * cos)
    tinggi_baru = int(h * cos + w * sin)

    matriks[0, 2] += lebar_baru / 2 - pusat[0]
    matriks[1, 2] += tinggi_baru / 2 - pusat[1]

    return cv2.warpAffine(
        gambar, matriks, (lebar_baru, tinggi_baru)
    )

rotasi_45 = rotasi_gambar(img, 45)
rotasi_90 = rotasi_gambar(img, 90)
rotasi_180 = rotasi_gambar(img, 180)

horizontal_flip = cv2.flip(img, 1)
vertical_flip = cv2.flip(img, 0)

hasil = [
    (img, "Gambar Asli"),
    (translation, "Translation"),
    (scaling_05, "Scaling 0.5"),
    (scaling_2, "Scaling 2"),
    (rotasi_45, "Rotation 45"),
    (rotasi_90, "Rotation 90"),
    (rotasi_180, "Rotation 180"),
    (horizontal_flip, "Horizontal Flip"),
    (vertical_flip, "Vertical Flip")
]



# Menampilkan seluruh hasil transformasi
fig, axes = plt.subplots(
    3, 3,
    figsize=(16, 12),
    constrained_layout=True
)

for ax, (gambar, judul) in zip(axes.flat, hasil):
    ax.imshow(gambar)
    ax.set_title(judul, fontsize=13, pad=10)
    ax.axis("off")

# Menyimpan hasil gambar
plt.savefig(
    "hasil_transformasi/hasil_semua.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()

print("Semua transformasi berhasil dilakukan!")
print("Hasil tersimpan di folder hasil_transformasi.")


plt.show()

print("Semua transformasi berhasil dilakukan!")
print("Hasil tersimpan di folder hasil_transformasi.")
