# Task-1
class Solution:
    def search(self, nums, target):
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = binarySearchLeft(nums, target)
        right = binarySearchRight(nums, target)

        if left <= right:
            return [left, right]
        else:
            return [-1, -1]


# Test
# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.search([4,9,10,13,17,17,19,21], -1))
#     print(solution.search([2, 4, 6, 8, 10, 14, 16], 16))
#     print(solution.search([], 0))




# Task-2

class Solution:
    def Search(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row-1
        while top <= bottom:
            target_row = (top + bottom) // 2
            if target > matrix[target_row][-1]:
                top = target_row + 1
            elif target < matrix[target_row][0]:
                bottom = target_row - 1
            else:
                break

        if not (top <= bottom):
            return False
        target_row = (top + bottom) // 2
        l, r = 0, col - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[target_row][mid]:
                l = mid + 1
            elif target < matrix[target_row][mid]:
                r = mid - 1
            else:
                return True
        return False


if __name__ == "__main__":
    Output1 = Solution().Search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], -1)
    print(Output1)
    Output2 = Solution().Search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 80)
    print(Output2)

