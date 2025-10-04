import re


def find_words_with_n(text):
    pattern = r'\b\w*[nN]\w*\b'
    return re.findall(pattern, text)


def find_words_with_many_consonants(text):
    words = re.findall(r'\b[a-zA-Zа-яА-ЯїЇєЄіІґҐ]+\b', text)
    result = []
    
    for word in words:
        consonants = re.findall(r'[^aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ]', word)
        if len(consonants) > 5:
            result.append(word)
    
    return result


def find_words_starting_with_vowel(text):
    pattern = r'\b[aeiouAEIOU]\w*\b'
    return re.findall(pattern, text)


def extract_email_domains(text):
    pattern = r'\b[\w.+-]+@([\w.-]+\.\w+)\b'
    domains = re.findall(pattern, text)
    return domains

    
def validate_password(password):
    if not re.match(r'^.{12,20}$', password):
        return False, "Довжина має бути від 12 до 20 символів"
    
    if re.search(r'\s', password):
        return False, "Пароль не повинен містити пробілів"
    
    digits = re.findall(r'\d', password)
    if len(digits) < 2:
        return False, f"Пароль має містити хоча б 2 цифри (знайдено: {len(digits)})"

    uppercase = re.findall(r'[A-Z]', password)
    if len(uppercase) < 1:
        return False, f"Пароль має містити мінімум 1 велику літеру (знайдено: {len(uppercase)})"
    
    special_chars = re.findall(r'[_?*$@\-!&#]', password)
    if len(special_chars) < 2:
        return False, f"Пароль має містити більше 2 спеціальних символів (знайдено: {len(special_chars)})"
    
    if not re.match(r'^[a-zA-Z0-9_?*$@\-!&#]+$', password):
        return False, "Пароль містить недозволені символи"
    
    return True, "Пароль відповідає всім вимогам"



if __name__ == "__main__":
    print("=" * 70)
    print("ЗАВДАННЯ 1: Слова з літерою 'n'")
    print("=" * 70)
    text1 = "The sun shines brightly in the morning and evening"
    result1 = find_words_with_n(text1)
    print(f"Текст: {text1}")
    print(f"Результат: {result1}\n")
    
    print("=" * 70)
    print("ЗАВДАННЯ 2: Слова з більше 5 приголосних")
    print("=" * 70)
    text2 = "Programming operation transcripts complexity rhythm onslaught"
    result2 = find_words_with_many_consonants(text2)
    print(f"Текст: {text2}")
    print(f"Результат: {result2}\n")
    
    print("=" * 70)
    print("ЗАВДАННЯ 3: Слова, що починаються на голосну")
    print("=" * 70)
    text3 = "An apple and an orange are excellent fruits for a healthy diet"
    result3 = find_words_starting_with_vowel(text3)
    print(f"Текст: {text3}")
    print(f"Результат: {result3}\n")
    
    print("=" * 70)
    print("ЗАВДАННЯ 4: Витягнути домени з email-адрес")
    print("=" * 70)
    text4 = "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz"
    result4 = extract_email_domains(text4)
    print(f"Текст: {text4}")
    print(f"Результат: {result4}\n")
    
    print("=" * 70)
    print("ЗАВДАННЯ 5: Перевірка паролів")
    print("=" * 70)
    
    test_passwords = [
        "MyPass123@Word",      # Валідний
        "Short1@A",            # Закороткий
        "MyPassword123@Word",  # Забагато символів (>20)
        "MyPass 123@Word",     # Містить пробіл
        "MyPassWord@Test",     # Немає цифр
        "mypass123@word",      # Немає великих літер
        "MyPass1@Word",        # Тільки 1 цифра
        "MyPass12@@Word",        
        "MyPassWord123",       # Немає спеціальних символів
        "ABcd12@#$%ef",        # Недозволений спецсимвол (%)
        "ValidPass12@#",       # Валідний
        "StrongPW99!&#",       # Валідний
    ]
    
    for pwd in test_passwords:
        is_valid, message = validate_password(pwd)
        status = "✓ ВАЛІДНИЙ" if is_valid else "✗ НЕВАЛІДНИЙ"
        print(f"{status}: '{pwd}'")
        print(f"  → {message}\n")