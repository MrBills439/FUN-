import time
import sys

def print_lyrics():
    lyrics = [
        "They say money can't buy happiness",
        "But I still wanna get it",
        "I rather cry in a private jet",
        "Than to be smiling in the trenches",
        "Even the girl wey you love go follow another man",
        "When there is no money ahh",
        "She gat me worried now",
        "'Cause only me got me ahh",
        "",
        "So, I do my thing my way",
        "Mi o dẹ le fọ laye",
        "Nobody go follow me feel my pain",
        "I keep asking",
        "Igbawo lowo ma de?",
        "",
        "So many oppressions on Instagram",
        "And me I no fit risk my life",
        "'Cause if person go do ritual",
        "Iro ooo. Ese kese loma paa",
        "Even my niggas wey don make am now",
        "If I call on them dem go fall my hand",
        "And me I no fit reason am",
        "Kilode ooo make we no dey get kwata",
        "",
        "So, I do my thing my way",
        "Mi o dẹ le fọ laye",
        "Nobody go follow me feel my pain",
        "I keep asking",
        "Igbawo lowo ma de?",
    ]

    # Adjust delays between lines (in seconds) as you prefer
    delays = [
        0.5, 0.4, 0.5, 0.5, 0.7, 0.5, 0.5, 0.6,
        1.0,
        0.7, 0.5, 0.6, 0.4, 1.2,
        1.0,
        0.6, 0.5, 0.7, 0.8, 0.6, 0.7, 0.6, 0.8, 1.0,
        0.7, 0.5, 0.6, 0.4, 1.2
    ]

    print("My Way — Hotkid\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # typing speed per char
        print()
        # after the line, pause
        if i < len(delays):
            time.sleep(delays[i])

if __name__ == "__main__":
    print_lyrics()
