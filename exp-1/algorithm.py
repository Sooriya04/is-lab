from collections import Counter
def enc(text, shift):
    result = ''
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def dec(text, shift):
    return enc(text, -shift)

def brute_force(text):
    for sh in range(26):
        print(f"Shift : {sh} Result : {dec(text, sh)}")

def freq_analysis(text):
    letter = [ch.lower() for ch in text if ch.isalpha()]
    freq = Counter(letter)
    most_common = freq.most_common(1)[0][0]
    guessed_shift = (ord(most_common) - ord('e')) % 26
    return guessed_shift
