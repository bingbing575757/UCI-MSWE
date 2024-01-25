#Task-1
import random
class ChainHashMap:
    def __init__(self, cap = 11, p = 109345121):
        # Initializes the ChainHashMap with optional parameters cap and p for table size and prime number.
        self._table = cap*[None]
        self._n = 0
        self._prime = p
        self._scale = 1 + random.randrange(p-1)
        self._shift = random.randrange(p)

    def hash_function(self, k):
        # Computes the hash value for the given key using ASCII values, scale, and shift.
        ascii_sum = sum(ord(char) for char in k)
        return (ascii_sum*self._scale + self._shift) % self._prime % len(self._table)

    def size(self):
        # returns the size of the elements, i.e., the number of keys.
        total_size = 0
        for bucket in self._table:
            if bucket is not None:
                total_size += len(bucket)
        return total_size

    def insert(self, k):
        # inserts string x to the HashTable in the index returned by hash(x)
        index = self.hash_function(k)

        if self._table[index] is None:
            self._table[index] = []

        for item in self._table[index]:
            if item == k:
                return

        self._table[index].append(k)
        self._n += 1



hash_map2 = ChainHashMap()
try:
    with open("pride-and-prejudice.txt", mode="rt", encoding="utf-8") as file:
        for line in file:
            word = ""
            for c in line:
                if c.isalpha() or c.isdigit():
                    word += c.lower()
                elif word:
                    sorted_word = ''.join(sorted(word))
                    hash_map2.insert(sorted_word)
                    word = ""
except FileNotFoundError:
    print("Failed to open file.")

print(hash_map2.size())
# if __name__ == "__main__":
#
#     hash_map = ChainHashMap()
#     hash_map.insert("China")
#     hash_map.insert("US")
#
#     print(hash_map._table)
#     print(hash_map.size())


# Task-2

# class HashTable:
#     def __init__(self, size):
#         self.table_size = size
#         self.table = [[] for _ in range(size)]
#
#     def hash(self, key):
#         hash_value = 0
#         for c in key:
#             hash_value += ord(c)
#         return hash_value % self.table_size
#
#     def insert(self, key):
#         index = self.hash(key)
#         for item in self.table[index]:
#             if item == key:
#                 return
#         self.table[index].append(key)
#
#     def size(self):
#         count = 0
#         for item in self.table:
#             count += len(item)
#         return count
#
# if __name__ == "__main__":
#     hash_map1 = HashTable(2**4)
#     hash_map1.insert("China")
#     hash_map1.insert("US")
#
#     print(hash_map1.table)
#     print(hash_map1.size())
#
#
#
# hash_map2 = HashTable(2**4)
# try:
#     with open("pride-and-prejudice.txt", mode="rt", encoding="utf-8") as file:
#         for line in file:
#             word = ""
#             for c in line:
#                 if c.isalpha() or c.isdigit():
#                     word += c.lower()
#                 elif word:
#                     sorted_word = ''.join(sorted(word))
#                     hash_map2.insert(sorted_word)
#                     word = ""
# except FileNotFoundError:
#     print("Failed to open file.")
#
# print(hash_map2.size())







# def test2():
#     print("----------test2-----------")
#     hash_table = HashTable(2 ** 16)
#     try:
#         with open("pride-and-prejudice.txt", mode="rt", encoding="utf-8") as file:
#             for line in file:
#                 word = ""
#                 for c in line:
#                     if c.isalpha() or c.isdigit():
#                         word += c.lower()
#                     elif word:
#                         sorted_word = ''.join(sorted(word))
#                         hash_table.insert(sorted_word)
#                         word = ""
#     except FileNotFoundError:
#         print("Failed to open file.")
#         return
#
#     print(hash_table.size())


# hash_table = HashTable(2 ** 16)
# try:
#     with open("pride-and-prejudice.txt", mode="rt", encoding="utf-8") as file:
#         for line in file:
#             word = ""
#             for c in line:
#                 if c.isalpha() or c.isdigit():
#                     word += c.lower()
#                 elif word:
#                     sorted_word = ''.join(sorted(word))
#                     hash_table.insert(sorted_word)
#                     word = ""
# except FileNotFoundError:
#     print("Failed to open file.")
#
# print(hash_table.size())







