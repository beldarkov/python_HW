def count_vowels(word):
    vowels = "aeiouyаяуюоеёэиы"
    count = 0
    for letter in word:
        if letter in vowels.lower():
            count += 1
    return count

def check_rhythm(poem):
    words = poem.split() 
    counts = [count_vowels(word) for word in words]  
    return "Парам пам-пам" if len(set(counts)) == 1 else "Пам парам"

str = "пара-ра-рам рам-пам-папам па-ра-па-дам "
print(check_rhythm(str))
