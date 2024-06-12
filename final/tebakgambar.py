import pygame
import random
import sys

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)  # Warna abu tua
BLACK = (0, 0, 0)
SILVER = (222, 49, 99)


# init music
pygame.mixer.init()
main_sound = pygame.mixer.Sound("audio/FastFeelBananaPeel-320bit(chosic.com).mp3")
main_sound.set_volume(1)


# background music
pygame.mixer.music.load("audio/Spook2(chosic.com).mp3")
pygame.mixer.music.play(0, 0.0)
pygame.mixer.music.set_volume(0.03)

# Skor awal
skor = 0

# Jumlah kesempatan menebak
kesempatan = 5

# Jumlah gambar yang telah dijawab
jawaban_terjawab = 0

# Jumlah gambar yang harus dijawab sebelum game selesai
jumlah_gambar_terjawab_sebelum_selesai = 10

# Daftar gambar yang akan ditebak
gambar = [
    "kucing.jpeg",
    "ayam.jpeg",
    "katak.jpeg",
    "kambing.jpeg",
    "trex.jpeg",
    "kambing.jpeg",
    "jerapah.jpeg",
    "singa.jpeg",
    "harimau.jpeg",
]

# Inisialisasi jendela Pygame
lebar = 800
tinggi = 500
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Game Tebak Gambar")


# Font untuk teks
def buat_font(ukuran, warna):
    return (
        pygame.font.Font("C:/Users/ASUS/Desktop/final/Hello Avocado.ttf", ukuran),
        warna,
    )


def buat_fontt(size, color):
    return pygame.font.Font("King Kids.otf", size), color


font_menu_utama, warna_menu_utama = buat_font(58, WHITE)
font_menu, warna_menu = buat_font(32, WHITE)
font_selama_permainan, warna_selama_permainan = buat_fontt(20, BLACK)
font_support, warna_support = buat_fontt(20, WHITE)
font_kredit, warna_kredit = buat_font(24, WHITE)


# Fungsi untuk mengacak gambar
def acak_gambar():
    return random.choice(gambar)


# Fungsi untuk menampilkan teks
def tampilkan_teks(teks, x, y, font, warna):
    teks_surface = font.render(teks, True, warna)
    teks_rect = teks_surface.get_rect()
    teks_rect.centerx = x  # Mengatur posisi horizontal di tengah
    teks_rect.centery = y  # Mengatur posisi vertikal di tengah
    layar.blit(teks_surface, teks_rect)


# Fungsi untuk memulai game
def main():
    main_sound.play()
    global skor, kesempatan, jawaban_terjawab

    gambar_sekarang = acak_gambar()
    input_teks = ""
    jawaban_benar = False

    while kesempatan > 0 and jawaban_terjawab < jumlah_gambar_terjawab_sebelum_selesai:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_RETURN:
                    tebakan = input_teks.lower()
                    if tebakan == gambar_sekarang[:-5]:
                        skor += 9
                        jawaban_terjawab += 1
                        jawaban_benar = True
                    else:
                        kesempatan -= 1

                    gambar_sekarang = acak_gambar()
                    input_teks = ""

                elif event.key == pygame.K_BACKSPACE:
                    input_teks = input_teks[:-1]
                else:
                    input_teks += event.unicode

        layar.fill((0, 0, 0))

        gambar_path = "C:/Users/ASUS/Desktop/final/gambar/" + gambar_sekarang
        tebak_gambar = pygame.image.load(gambar_path)
        layar.blit(tebak_gambar, (lebar // 20 - 40, tinggi // 10 - 100))

        tampilkan_teks("Tebak Gambar:", lebar // 2, 50, font_menu, BLACK)
        jarak_dari_atas = 20
        jarak_dari_kanan = 100

        tampilkan_teks(
            "Skor: " + str(skor),
            lebar - jarak_dari_kanan,
            jarak_dari_atas,
            font_selama_permainan,
            BLACK,
        )
        tampilkan_teks(
            "Kesempatan: " + str(kesempatan),
            lebar - jarak_dari_kanan,
            jarak_dari_atas + 30,
            font_selama_permainan,
            BLACK,
        )
        tampilkan_teks(
            "Jawaban Terjawab: "
            + str(jawaban_terjawab)
            + "/"
            + str(jumlah_gambar_terjawab_sebelum_selesai),
            lebar - jarak_dari_kanan - 20,
            jarak_dari_atas + 60,
            font_selama_permainan,
            BLACK,
        )

        if jawaban_benar:
            penjelasan = (
                "Jawaban Benar! Ini adalah " + gambar_sekarang[:-5].capitalize()
            )
            tampilkan_teks(penjelasan, lebar // 2, 350, font_selama_permainan, BLACK)
            pygame.time.delay(1000)

            if skor % 10 == 0:
                skor += 10
            else:
                skor += 1

            jawaban_benar = False

        input_box = pygame.Rect(lebar // 2 - 100, tinggi // 2 + -190, 200, 40)
        pygame.draw.rect(layar, GRAY, input_box)
        tampilkan_teks(
            input_teks, input_box.centerx, input_box.centery, font_menu, WHITE
        )

        pygame.display.flip()
        pygame.time.delay(100)

    if jawaban_terjawab == jumlah_gambar_terjawab_sebelum_selesai:
        layar.fill((0, 0, 255))
        background = pygame.image.load("C:/Users/ASUS/Desktop/final/gambar/hewan.jpg")
        background = pygame.transform.scale(background, (lebar, tinggi))
        tampilkan_teks("Game Selesai!", lebar // 2, tinggi // 2 - 50, font_menu, WHITE)
        tampilkan_teks(
            "Skor Akhir: " + str(skor), lebar // 2, tinggi // 2 + 50, font_menu, WHITE
        )
        tampilkan_teks(
            "Tekan 'C' untuk melanjutkan atau 'Q' untuk keluar.",
            lebar // 2,
            tinggi // 2 + 100,
            font_menu,
            WHITE,
        )
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        skor = 0
                        kesempatan = 5
                        jawaban_terjawab = 0
                        main()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()


# Fungsi untuk menampilkan menu utama
def main_menu():
    background = pygame.image.load("C:/Users/ASUS/Desktop/final/gambar/hewan2.jpg")
    background = pygame.transform.scale(background, (lebar, tinggi))

    while True:
        layar.fill((0, 0, 255))
        layar.blit(background, (0, 0))
        tampilkan_teks(
            "Game Tebak Gambar Hewan", lebar // 2, tinggi // 7, font_menu_utama, SILVER
        )
        tampilkan_teks("1. Play Game", lebar // 4.9, tinggi // 1.3, font_menu, BLACK)
        tampilkan_teks("2. Support", lebar // 2.2, tinggi // 1.2, font_menu, BLACK)
        tampilkan_teks("3. About us", lebar // 1.5, tinggi // 1.3, font_menu, BLACK)
        tampilkan_teks("4. Exit", lebar // 1.2, tinggi // 1.2, font_menu, BLACK)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main()
                elif event.key == pygame.K_2:
                    support()
                    # Tambahkan kode untuk menu Options di sini
                    pass
                elif event.key == pygame.K_3:
                    about_us()
                elif event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()


# Fungsi untuk menampilkan petunjuk
def support():
    while True:
        layar.fill((0, 32, 92))
        tampilkan_teks(
            "Ada yang bisa di bantu?", lebar // 2, tinggi // 6, font_menu_utama, WHITE
        )
        tampilkan_teks(
            "Sebelum bermain baca dulu opsi di bawah ini:",
            lebar // 2,
            tinggi // 2 - 50,
            font_support,
            WHITE,
        )
        tampilkan_teks(
            "1. Tekan tombol 1, untuk memulai game.",
            lebar // 2,
            tinggi // 2,
            font_support,
            WHITE,
        )
        tampilkan_teks(
            "2. Tekan tombol 2, untuk menu bantuan/ jika tidak tau cara memainkan gamenya ",
            lebar // 2,
            tinggi // 2 + 50,
            font_support,
            WHITE,
        )
        tampilkan_teks(
            "3. Tekan tombol 3, untuk informasi pembuat game",
            lebar // 2,
            tinggi // 2 + 100,
            font_support,
            WHITE,
        )
        tampilkan_teks(
            "4. Tekan tombol 4, untuk menutup permainan",
            lebar // 2,
            tinggi // 2 + 150,
            font_support,
            WHITE,
        )
        tampilkan_teks(
            "Tekan 'M' untuk kembali ke Menu Utama.",
            lebar // 2,
            tinggi - 30,
            font_menu,
            WHITE,
        )
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    main_menu()


# Untuk menampilkan nama kelompok
def about_us():
    while True:
        layar.fill((0, 128, 128))
        tampilkan_teks(
            "Terimakasih Telah Memainkan Game Kami",
            lebar // 2,
            tinggi // 8,
            font_menu,
            BLACK,
        )
        tampilkan_teks("Kelompok 7:", lebar // 2, tinggi // 2 - 50, font_kredit, BLACK)
        tampilkan_teks(
            "1. Muhammad Ardianyah", lebar // 2, tinggi // 2, font_kredit, BLACK
        )
        tampilkan_teks(
            "2. Nurfadilah", lebar // 2, tinggi // 2 + 50, font_kredit, BLACK
        )
        tampilkan_teks(
            "3. Muhammad Rizal Setyawan",
            lebar // 2,
            tinggi // 2 + 100,
            font_kredit,
            BLACK,
        )
        tampilkan_teks(
            "4. Fandi Septian", lebar // 2, tinggi // 2 + 150, font_kredit, BLACK
        )
        tampilkan_teks(
            "Tekan 'M' untuk kembali ke Menu Utama.",
            lebar // 2,
            tinggi - 30,
            font_menu,
            BLACK,
        )
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    main_menu()


main_menu()
