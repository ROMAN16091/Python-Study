import re

text = 'abc\ndef\nelse'

# r'a.' - шукає символ 'a', після якого йде будь-який символ (крім нового рядка \n)
pattern = r'a.'
print(re.findall(pattern, text))  # ['ab'] – знайдено лише 'ab', оскільки '.' не захоплює '\n'

text = 'ab, a, abb, abc, aa'

# r'ab*'
# 'a' - літера 'a'
# 'b*' - символ 'b', який може зустрічатися 0 або більше разів (нуль також підходить)
pattern = r'ab*'
print(re.findall(pattern, text))  # ['ab', 'a', 'abb', 'ab'] – включає 'a', оскільки 'b*' може бути порожнім

# r'ab+'
# 'a' - літера 'a'
# 'b+' - символ 'b', який повинен зустрічатися хоча б 1 раз
pattern = r'ab+'
print(re.findall(pattern, text))  # ['ab', 'abb'] – 'a' без 'b' не підходить

text = 'colour colour'

# r'colou?r'
# 'colou' - літери 'colou'
# 'r' - літера 'r'
# '?' - попередній символ ('u') може зустрічатися 0 або 1 раз
pattern = r'colou?r'
print(re.findall(pattern, text))  # ['colour', 'colour'] – обидва слова підходять

# r'\d{3}'
# '\d' - будь-яка цифра (0-9)
# '{3}' - повторення рівно 3 рази підряд
pattern = r'\d{3}'
print(re.findall(pattern, '123 45 6789'))  # ['123', '678']

# r'\d{2,4}'
# '\d' - будь-яка цифра
# '{2,4}' - повторення від 2 до 4 разів підряд
pattern = r'\d{2,4}'
print(re.findall(pattern, '123 45 6789'))  # ['123', '45', '6789']

# r'[abc]'
# '[]' - набір символів
# 'abc' - будь-який символ з цього списку (a, b або c)
pattern = r'[abc]'
print(re.findall(pattern, 'apple pineapple cher*ry banana'))
# ['a', 'p', 'p', 'l', 'e', ..., 'a', 'a'] – вибирає лише 'a', 'b', 'c' з тексту

# r'\b\w*apple\w*\b'
# '\b' - межа слова
# '\w*' - 0 або більше буквено-цифрових символів перед 'apple'
# 'apple' - саме слово 'apple'
# '\w*' - 0 або більше буквено-цифрових символів після 'apple'
# '\b' - межа слова
pattern = r'\b\w*apple\w*\b'
print(re.findall(pattern, 'apple pineapple cherry banana'))  # ['apple', 'pineapple']

# r'[^abc]'
# '[^]' - виключаючий набір символів (усе, крім зазначених)
# 'abc' - символи, які НЕ повинні зустрічатися
pattern = r'[^abc]'
print(re.findall(pattern, 'apple pineapple cher*ry banana'))
# Усі символи, крім 'a', 'b', 'c'

text = 'abc 123 _ -'

# r'\d'
# '\d' - будь-яка цифра (0-9)
print(re.findall(r'\d', text))  # ['1', '2', '3']

# r'\w'
# '\w' - будь-яка літера, цифра або символ '_'
print(re.findall(r'\w', text))  # ['a', 'b', 'c', '1', '2', '3', '_']

# r'\s'
# '\s' - будь-який пробільний символ (пробіл, табуляція, новий рядок)
print(re.findall(r'\s', text))  # [' ', ' ']

# r'\D'
# '\D' - будь-який символ, крім цифри
print(re.findall(r'\D', text))  # ['a', 'b', 'c', ' ', '_', ' ']

# r'\W'
# '\W' - будь-який символ, крім букв, цифр і '_'
print(re.findall(r'\W', text))  # [' ', ' ', '-']

# r'\S '
# '\S' - будь-який непорожній символ
# ' ' - потім обов’язково пробіл
print(re.findall(r'\S ', text))  # ['c ', '3 ', '_ '] – символи перед пробілом

text = 'gray, grey'
pattern = r'gr(?:a|e)y'
print(re.findall(pattern,text))

text = 'cat dog mouse'
pattern = r'cat|dog|mouse'
print(re.findall(pattern,text))

text = 'Date: 2025-03-28'
pattern = r'(\d{4})-(\d{2})-(\d{2})'
find_match = re.search(pattern,text)
if find_match:
    year, month, day = find_match.groups()
    print(year)
    print(month)
    print(day)

text = 'Coord: 12.34, 56.78'
pattern = r'(\d+\.\d+),\s*(\d+\.\d+)'
find_match = re.search(pattern,text)
if find_match:
    lat, lon = find_match.groups()
    print(lat)
    print(lon)

text = 'Hello Name'
pattern = r'Hello'

if re.match(pattern,text):
    print('Рядок починається з Hello')

pattern = r'Name'
print(re.sub(pattern, 'Lastname', text))

pattern = r'\s'
print(re.sub(pattern, '-', text))

text = 'apple, cherry; orange. banana'
pattern = r'[,\.;]\s+'
print(re.split(pattern,text))

text = 'Hello\nhello\nHELLO'
pattern = r'hello'
print(re.findall(pattern, text, flags= re.IGNORECASE,))

text = 'Name hello\nLastname hello'
pattern = r'^\w+'
print(re.findall(pattern, text, flags= re.MULTILINE,))

text = 'abca\ndaef'
pattern = r'a.'
print(re.findall(pattern,text,flags= re.DOTALL))
pattern = re.compile(r"""
    ^       #Початок рядка
    ()
    """)

samples = [
    '+38 (067) 123-45-67'
    '0671234567'
    '+380671234567'
]