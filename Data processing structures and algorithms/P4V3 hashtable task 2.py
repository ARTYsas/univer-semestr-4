#создание хеш-таблицы
def create_hash_table(file_name, table_size):
    hash_table = [[] for i in range(table_size)]
    with open(file_name, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                hash_value = hash_function(word, table_size)
                hash_table[hash_value].append(word)
    return hash_table

#непосредственно хеш-функция, определяющая "место" слова в таблице
def hash_function(word, table_size):
    hash_value = 0
    for letter in word:
        hash_value = (hash_value * 15 + ord(letter)) % table_size
    return hash_value

#поиск слова в хеш таблице
def search_hash_table(hash_table, word):
    hash_value = hash_function(word, len(hash_table))
    for w in hash_table[hash_value]:
        if w == word:
            return True
    return False

#удаление слова на определенную букву в хеш таблице
def delete_words_starting_with(hash_table, letter):
    new_hash_table = [[] for j in range(len(hash_table))]
    for i in range(len(hash_table)):
        for word in hash_table[i]:
            if word[0] != letter:
                new_hash_table[i].append(word)
    return new_hash_table

print("Введите название файла с .txt:")
file_name = input()
table_size = int(input("Введите размерность хеш-таблицы: "))
hash_table = create_hash_table(file_name, table_size)
print("Хеш-таблица слов из файла:")

for i in range(table_size):
    print(f"{i}: {hash_table[i]}")

word = input("Введите слово для поиска: ")

if search_hash_table(hash_table, word):
    print(f"Слово '{word}' найдено.")
else:
    print(f"Слово '{word}' не найдено.")

letter = input("Введите букву для удаления слов, начинающихся на нее: ")
hash_table = delete_words_starting_with(hash_table, letter)
print(f"Хеш-таблица после удаления слов, начинающихся на букву '{letter}':")

for i in range(table_size):
    print(f"{i}: {hash_table[i]}")
