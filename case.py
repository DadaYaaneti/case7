# Case-study #7
# Developers:   Gorevoy (50%),
#               Bricheev (50%).

import random

with open("text.txt") as f:
    text = f.read()

text = " ".join(text.split("\n"))

words = []

for word in text.split(' '):
    flag = 1
    if word == "":
        flag = 0
    for s in word:
        if not (ord("а") <= ord(s.lower()) <= ord("я") or ord("A") <= ord(s.lower()) <= ord("Z") or s in ",.?!"):
            flag = 0
    if flag:
        words.append(word)

chains = {}
for i in range(len(words) - 1):
    if words[i] not in chains:
        chains[words[i]] = []
    else:
        chains[words[i]].append(words[i + 1])


first_words = {word for word in chains if "А" <= word[0] <= "Я" and word[-1] not in [".", "!", "?"]}
end_words = {word for word in chains if word[-1] in [".", "!", "?"]}


n = int(input("Введите количество предложений: "))
for i in range(n):
    s = random.choice(list(first_words))
    while not(s.split(" ")[-1] in end_words and 5 <= len(s.split(" ")) <= 20):
        try:
            s += " " + random.choice(chains[s.split(" ")[-1]])
        except Exception:
            s = random.choice(list(first_words))
    print(s)
