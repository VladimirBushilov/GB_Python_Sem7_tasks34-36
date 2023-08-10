def count_vowels(word):
    vowels = 'aeiouаеёиоуыэюя'
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

def check_rhythm(poem):
    phrases = poem.split(' ')
    
    for phrase in phrases:
        words = phrase.split('-')
        
        vowel_counts = [count_vowels(word) for word in words]
        
        if len(set(vowel_counts)) > 1:
            return 'Пам парам'
    
    return 'Парам пам-пам'

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)