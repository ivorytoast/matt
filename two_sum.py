from typing import List

# [2, 7, 11, 15] and given a target like 9, return the 2 numbers that equal 9 in the list
# Guaranteed that there will be exactly 1 solution and only 1 solution

# In the WORST CASE scenario, what is the total number of items it would have to look at
# log(n) halves every time
# [1,2,3], t = length of this array
# O(t)


# log(n) (ie: Binary search)
# [1,2,3,4,5,6,7,8,9,10]
# [1,2,3,4]
# [3,4]
# 3


# O(1) => HashMap (Dictionaries)
# Value -> Apply a Hash Function -> Store it in the place where the hash belongs
# [1 -> "banana", "apple", 45, 47, etc...]
# O(n)


# O(n * log(n))
# Merge sort
# For each item in the array, it does a sort function that is O(log(n))
# [2,1,3,5,4]


# O(n!) -> Traveling Salesman
# Given a starting point and endpoint, what are ALL the possible routes the salesman could take


# O(1)
# O(log(n))
# O(n)
# O(n * log(n))
# O(n^2)
# O(n!)


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for index_i, value_i in enumerate(nums):
    #         for index_j, value_j in enumerate(nums):
    #             if index_j != index_i:
    #                 if value_i + value_j == target:
    #                     return [index_i, index_j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for idx, val in enumerate(nums):
            diffs[target - val] = idx
        for idx, val in enumerate(nums):
            if val in diffs:
                print(f"Found the difference {val}")
                return [idx, diffs[val]]


if __name__ == '__main__':
    solution = Solution()
                        # [7, 2, -2, -6]
    print(solution.twoSum([2, 7, 11, 15], 9)) # True
    print(solution.twoSum([2, 1, 11, 15], 9)) # False
    # print(solution.twoSum([7, 2, 13, 18], 15))
