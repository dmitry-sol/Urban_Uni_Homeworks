# module_9_6
# Генераторы

def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j:j + i + 1]


result = all_variants('abc')
for k in result:
    print(k)
