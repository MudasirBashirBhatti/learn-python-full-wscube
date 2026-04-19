
def count_vowels(text:str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for c in text:
        if c in vowels:
            count += 1
    return count

print(count_vowels("The quick brown fox jumps over the lazy dog"))