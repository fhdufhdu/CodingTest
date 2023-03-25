from sys import stdin, stdout

read = stdin.readline
write = stdout.write

"""
1. 단어 순서로
2. 모든 단어가 되어 있으면 그냥 모든 알파벳
"""

n = int(read().rstrip())
data = [read().rstrip() for _ in range(n)]

quick = {}
result = ["" for _ in range(n)]

# for i, menu in enumerate(data):
#     words = menu.split(" ")
#     is_set = False
#     for j, word in enumerate(words):
#         first_letter = word[0]
#         if first_letter in quick: continue
#         quick[first_letter.upper()] = True
#         quick[first_letter.lower()] = True
#         words[j] = f"[{first_letter}]{word[1:]}"
#         is_set = True
#         break
#     result[i] = " ".join(words) if is_set else ""

# for i, menu in enumerate(data):
#     if result[i] != "": continue
#     is_set = False
#     for j, letter in enumerate(menu):
#         if letter == ' ': continue
#         if letter in quick: continue
#         quick[letter.upper()] = True
#         quick[letter.lower()] = True
#         is_set = True
#         break
#     result[i] = f"{menu[:j]}[{letter}]{menu[j+1:]}" if is_set else menu

for i, menu in enumerate(data):
    words = menu.split(" ")
    is_set = False
    for j, word in enumerate(words):
        first_letter = word[0]
        if first_letter in quick: continue
        quick[first_letter.upper()] = True
        quick[first_letter.lower()] = True
        words[j] = f"[{first_letter}]{word[1:]}"
        is_set = True
        break
    result[i] = " ".join(words) if is_set else ""

    if result[i] != "": continue
    is_set = False
    for j, letter in enumerate(menu):
        if letter == ' ': continue
        if letter in quick: continue
        quick[letter.upper()] = True
        quick[letter.lower()] = True
        is_set = True
        break
    result[i] = f"{menu[:j]}[{letter}]{menu[j+1:]}" if is_set else menu

write("\n".join(result))