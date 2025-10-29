
file_path = 'sampletext.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

num_words     = len(text.split())
num_sentences = text.count('.') + text.count('!') + text.count('?')

num_upper = 0
num_lower = 0
num_special = 0

for char in text:
    if char.isupper():
        num_upper += 1
    elif char.islower():
        num_lower += 1
    else:
        if not char.isalnum() and not char.isspace():
            num_special += 1

print("The inputted text is:\n\n",text)

print("\n\nNumber of words            :", num_words)
print("Number of sentences        :", num_sentences)
print("Number of uppercase letters:", num_upper)
print("Number of lowercase letters:", num_lower)
print("Number of special chars    :", num_special)
