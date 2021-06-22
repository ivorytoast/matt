#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.

# [1,2,3] + 1 = [1,2,4]
# [1,9,9] + 1 = [2,0,0]
# [9,9] + 1   = [1,0,0]


def tony_plus_one(nums):

    carry = 1

    for i in reversed(range(len(nums))):
        digit = nums[i]
        sum = digit + carry
        first_digit = int(sum / 10)
        second_digit = int(sum % 10)

        carry = first_digit
        nums[i] = second_digit

    # list.insert(position, value)
    if carry == 1:
        my_list = []
        my_list.append(carry)
        for i in range(len(nums)):
            my_list.append(nums[i])
        nums = my_list

    return nums


def plus_one(nums):
    # Code here
    arrayLength = len(nums)
    #Use case when last digit is not 9
    if nums[arrayLength - 1] != 9:
        nums[arrayLength - 1] += 1
    #Use case when last digit is 9
    else:
        arrayIndex = arrayLength - 1
        while arrayIndex > 0 and nums[arrayIndex] == 9:
            nums[arrayIndex] = 0
            arrayIndex -= 1
        #Check to see if at starting index then shift right
        if arrayIndex == 0 and nums[arrayIndex] == 9:
            nums[arrayIndex] = 0
            tempList = []
            tempList.append(1)
            for i in range(len(nums)):
                tempList.append(nums[i])
            nums = tempList
        else:
            nums[arrayIndex] += 1
    return nums


if __name__ == '__main__':
    print(plus_one([9,9,8,9]))