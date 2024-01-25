class AnagramGroups_merge_sort_method:
    @staticmethod
    def merge(s1, s2):
        tmp = []
        i = j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] < s2[j]:
                tmp.append(s1[i])
                i += 1
            else:
                tmp.append(s2[j])
                j += 1
        tmp.extend(s1[i:])
        tmp.extend(s2[j:])
        return tmp

    @staticmethod
    def merge_sort(s):
        if len(s) <= 1:
            return s
        mid = len(s) // 2
        s1 = AnagramGroups_merge_sort_method.merge_sort(s[:mid])
        s2 = AnagramGroups_merge_sort_method.merge_sort(s[mid:])
        return AnagramGroups_merge_sort_method.merge(s1, s2)

    @staticmethod
    def group_anagrams(strings):
        anagram_groups = {}
        for word in strings:
            sorted_word = ''.join(AnagramGroups_merge_sort_method.merge_sort(word))  # 使用归并排序，或者替换为 quick_sort(word) 使用快速排序
            anagram_groups.setdefault(sorted_word, []).append(word)
        return list(anagram_groups.values())


class AnagramGroups_quick_sort_method:
    @staticmethod
    def quick_sort(s):
        if len(s) <= 1:
            return s
        pivot = s[len(s) // 2]
        left = [x for x in s if x < pivot]
        middle = [x for x in s if x == pivot]
        right = [x for x in s if x > pivot]
        return AnagramGroups_quick_sort_method.quick_sort(left) + middle + AnagramGroups_quick_sort_method.quick_sort(right)

    @staticmethod
    def group_anagrams(strings):
        anagram_groups = {}
        for word in strings:
            sorted_word = ''.join(AnagramGroups_quick_sort_method.quick_sort(word))  # 使用快速排序
            anagram_groups.setdefault(sorted_word, []).append(word)
        return list(anagram_groups.values())

# Test
if __name__ == "__main__":
    strings = ["bucket", "bat", "mango", "tango", "ogtan", "tar","tab"]
    # Test for mergesort method
    anagram_groups1 = AnagramGroups_merge_sort_method.group_anagrams(strings)
    print(anagram_groups1)
    # Test for quicksort method
    anagram_groups2 = AnagramGroups_quick_sort_method.group_anagrams(strings)
    print(anagram_groups2)

    # Quick sort has a worst-case time complexity of O(n^2), best-case time complexity of O(log n), and an average-case time complexity of O(n log n).
    # Merge sort has a worst-case, best-case, and average-case time complexity of O(n log n).
    # In practical scenarios, when dealing with a small-scale problem of size n, the time complexity of quick sort is T(n) = n log n + c, where c is a constant. This means that the time complexity is not dominated by n^2.
    # Quick sort is usually an in-place sorting algorithm, requiring no extra space, while merge sort needs to allocate and deallocate auxiliary arrays.
    #  Consequently, due to the impact of constants, even though both algorithms have similar complexities, quick sort typically performs faster than merge sort in actual execution.

