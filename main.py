import time

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def animate_text(text, speed):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()  # Print newline after the text

def sing_song():
    lyrics = [
        ("Nobody got you the way I do", 0.6),
        ("Whatever demons you're fighting through", 0.6),
        ("When you need somebody to turn to", 0.6),
        ("Nobody got you the way I do", 0.6),
        ("Nobody, nobody, nobody", 0.07),
        ("Got you the way I do", 0.07),
        ("Nobody, nobody, nobody", 0.07),
        ("Nobody got you the way I do", 0.6)
    ]

    delays = [0.2, 2.2, 6.8, 10.0, 12.6, 14.7]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        delay = delays[i % len(delays)]
        sing_lyric(lyric, delay, speed)

# Call the function to sing the song
sing_song()
