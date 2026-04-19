def is_palindrome(text: str) -> bool:
    plain_text = text.lower().replace(" ","")
    length = len(plain_text)

    for i in range(length // 2):
        if plain_text[i] != plain_text[-1 - i]:
            return False
        
    return True

print(is_palindrome("madam"))        # True
print(is_palindrome("RaceCar"))      # True
print(is_palindrome("hello"))        # False
print(is_palindrome("nurses run"))   # True