import tkinter as tk
import random

# Olası renkler
COLORS = ["#FF6347", "#4682B4", "#FFD700", "#32CD32"]

# Body parts ve emojiler
BODY_PARTS = {
    "Sağ El": "🖐️",
    "Sol El": "🖐️",
    "Sağ Ayak": "🦶",
    "Sol Ayak": "🦶"
}

# Sayaç için süre (saniye cinsinden)
SPIN_INTERVAL = 60


# Spinner fonksiyonu
def spin():
    # Rastgele bir renk ve body part seç
    hex_color = random.choice(COLORS)
    body_part, emoji = random.choice(list(BODY_PARTS.items()))

    # Emoji ve yazıyı güncelle
    emoji_label.config(text=emoji)
    result_label.config(text=body_part)

    # Arka plan rengini değiştir
    root.configure(bg=hex_color)
    emoji_label.configure(bg=hex_color)
    result_label.configure(bg=hex_color)
    countdown_label.configure(bg=hex_color)

    start_countdown(SPIN_INTERVAL)


# Sayaç fonksiyonu
def start_countdown(seconds):
    def update():
        nonlocal seconds
        if seconds > 0:
            countdown_label.config(text=f"Yeni Çevirme: {seconds} saniye")
            seconds -= 1
            root.after(1000, update)
        else:
            spin()

    update()


# Ana pencere
root = tk.Tk()
root.title("Twister Spinner")
root.geometry("400x400")

# Emoji etiketi (büyük boyutlu)
emoji_label = tk.Label(root, text="", font=("Helvetica", 100))
emoji_label.pack(pady=20)

# Sonuç etiketi (body part yazısı)
result_label = tk.Label(root, text="", font=("Helvetica", 32))
result_label.pack()

# Sayaç etiketi
countdown_label = tk.Label(root, text="", font=("Helvetica", 18))
countdown_label.pack(pady=20)

# İlk çevirme işlemi
spin()

# Uygulamayı çalıştır
root.mainloop()