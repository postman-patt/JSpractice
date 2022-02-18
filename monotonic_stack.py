
# 402. Remove K Digits - leetcode

# Monotonic Stack combined with a greedy approach to find lowest or greatest values
# Basics: Loop through string and add each element to stack - Pop element is greater or less than top value on the stack


def removeKdigits(num, k):

    stack = []
    count = 0

    for i in range(len(num)):

        while len(stack) != 0 and (int(num[i]) < int(stack[len(stack) - 1])) and count < k:
            stack.pop()
            count += 1

        stack.append(num[i])

    while count < k:
        stack.pop()
        count += 1

    if len(stack) == 0:
        return '0'
    else:
        return str(int(''.join(stack)))


print(
    removeKdigits('112', 1))
