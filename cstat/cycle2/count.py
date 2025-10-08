text="asdkfhljJHJLHLKH??? hey there! How's it going?"

vowels=0
consonants=0
qmarks=0

words=len(text.split())

for i in text:
    if i.lower() in 'aeiou':
        vowels+=1
    elif i.isalpha():
        consonants+=1
    elif i=='?':
        qmarks+=1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Question Marks:", qmarks)
print("Words:", words)