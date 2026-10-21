def analyze_string():
    text = input("Enter a sentence: ")
    vowels = 0
    digits = 0
    spaces = 0
    for ch in text.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
    print("Characters:", len(text))
    print("Vowels:", vowels)
    print("Digits:", digits)
    print("Spaces:", spaces)
analyze_string()
