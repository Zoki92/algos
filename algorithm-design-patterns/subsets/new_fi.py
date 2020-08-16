from typing import List


# def solution(A, K):
#     # write your code in Python 3.6
#     swap(0, 0, A, K)

#     return A


# def swap(original, current, arr, K):
#     target = (original + K) % len(arr)
#     print("target: ", target)
#     print("original: ", original)
#     print("current: ", current)
#     if target > current:
#         arr[current], arr[target] = arr[target], arr[current]
#         print("current arr: ", arr)
#         print("______________-")
#         swap(target, current, arr, K)


# print(solution([3, 8, 9, 7, 6], 3))


# this doesn't work for negative values
# def solution(A, K):
#     n = len(A)
#     reverse(A, n - K, n - 1)
#     reverse(A, 0, n - K - 1)
#     reverse(A, 0, n - 1)
#     return A


# def reverse(A, low, high):
#     while low < high:
#         swap(A, low, high)
#         low += 1
#         high -= 1

# O(n) in time, O(1) in space
def rotate(nums, k):
    if k is None or k <= 0:
        return
    if len(nums) == 1:
        return nums
    k, end = k % len(nums), len(nums) - 1
    # reverse the first n - k elements
    reverse(nums, 0, end - k)
    # reverse the rest
    reverse(nums, end - k + 1, end)
    # reverse the whole array
    reverse(nums, 0, end)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1


# rotate([3, 8, 9, 7, 6], 3)

# given integer number return longest binary gap
# longest binary gap is the zeroes between two ones
# def solution(N):
#     # write your code in Python 3.6
#     longest_binary_gap = 0
#     current_longest = 0
#     is_gap = False
#     while N:
#         remainder = N % 2
#         N //= 2

#         if remainder == 1:
#             is_gap = True
#             if current_longest > 0:
#                 longest_binary_gap = max(longest_binary_gap, current_longest)
#                 current_longest = 0

#         if remainder == 0 and is_gap:
#             current_longest += 1

#     return longest_binary_gap


# def solution(A):
#     if not A:
#         return 0
#     i, end = 0, len(A)
#     while i < end:
#         # print(A[i])
#         if i + 1 != A[i] and A[i] < end:
#             swap(A, i, A[i] - 1)
#         else:
#             i += 1

#     for i in range(len(A)):
#         if i + 1 != A[i]:
#             return i + 1

#     return 0


# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]


# def main():
#     print(solution([5, 1, 4, 2]))
#     print(solution([9, 4, 6, 3, 5, 7, 1, 2]))


# main()


""" missing element """

# def solution(A):
#     n = len(A) + 1
#     needed_sum_arr = n * (n + 1) // 2

#     sum_array = sum(A)

#     return needed_sum_arr - sum_array


"""smallest difference"""


# def solution(A):
#     # write your code in Python 3.6
#     if len(A) == 2:
#         return abs(A[0] - A[1])
#     sum_first_part = A[0]
#     sum_second_part = sum(A[1:])

#     diff = get_difference(sum_first_part, sum_second_part)

#     minimum = diff

#     for i in range(1, len(A)):
#         sum_first_part += A[i]
#         sum_second_part -= A[i]
#         diff = get_difference(sum_first_part, sum_second_part)
#         print("DIFF: ", diff)
#         minimum = min(minimum, diff)

#     return minimum


# def get_difference(first, second):
#     return abs(first - second)


# print(solution([-10, -20, -30, -40, 100]))


# def solution(X, A):
#     covered_time = [-1] * X  # Record the time, each position is covered
#     uncovered = X  # Record the number of uncovered position
#     for index in range(len(A)):
#         print(covered_time)
#         if covered_time[A[index] - 1] != -1:
#             # This position is already covered
#             pass
#         else:
#             # This position is to be covered
#             covered_time[A[index] - 1] = index
#             uncovered -= 1
#             if uncovered == 0:
#                 # All positions are covered
#                 return index
#     # Finally, some positions are not covered
#     return -1


# print(solution(2, [2, 2, 2, 2]))


""" max counters """
# def solution(N, A):
#     # write your code in Python 3.6
#     counter = [0] * N
#     max_element = 0
#     base = 0
#     for item in A:
#         if 1 <= item <= N:
#             counter[item-1] = max(counter[item-1], base) + 1
#             max_element = max(counter[item - 1], max_element)
#         elif item == N + 1:
#             base = max_element

#     for i in range(N):
#         counter[i] = max(counter[i], base)
#     return counter


""" missing integer """
# def solution(A):
#     # write your code in Python 3.6
#     occurences = [False] * (len(A))

#     for num in A:
#         if 0 < num <= len(A):
#             occurences[num - 1] = True


#     for ind, val in enumerate(occurences):
#         if val == False:
#             return ind + 1

#     return len(A) + 1

""" is permutation """

# def solution(A):
#     occurences = [0] * (len(A) + 1)

#     for num in A:
#         if num > len(A) or occurences[num] == 1:
#             return 0
#         occurences[num] = 1

#     return 1


""" counting divs """

# def solution(A, B, K):
#     # write your code in Python 3.6
#         """
#     6 11 2 entries
#     11 / 2 = 5 - total number of ways 11 is evenly divisible by 2.
#     (6 - 1) / 2 = 2 - number of ways ints < 6 are evenly divisible by 2 (to exclude from total).
#     5 - 2 = 3 - subtract the excluded count from the total to get our result.
#     """
#     return B // K - (A - 1) // K

# def solution(S, P, Q):
#     result = []


#     for i in range(len(P)):
#         slice = S[P[i]: Q[i] + 1]
#         min = 4
#         if 'A' in slice:
#             min = 1
#         elif 'C' in slice:
#             min = 2
#         elif 'G' in slice:
#             min = 3

#         result.append(min)
#     return result

# solution("CAGCCTA". [2,5,0], [4, 5, 6])


# import math


# def solution(A):
#     pref = prefix_sum(A)
#     min_mean = math.inf
#     min_idx_from = 0
#     for i in range(len(A)):
#         for j in range(i + 1, min(i + 3, len(A))):
#             print("J: ", j)

#             mean = (pref[j + 1] - pref[i]) / (j - i + 1)
#             print("mean: ", mean)
#             if mean < min_mean:
#                 min_mean = mean
#                 min_idx_from = i
#         print("____")
#     return min_idx_from


# def prefix_sum(A):
#     n = len(A)
#     P = [0] * (n + 1)
#     for k in range(1, n + 1):
#         P[k] = P[k - 1] + A[k - 1]
#     return P


# solution([4, 2, 2, 5, 1, 5, 8])


""" 
passing cars
def solution(A):
    pairs = 0
    zero_counts = 0
    # count the number of zeros in the list
    # for each successive 1 in the list numbers of pairs will be
    # incremented by the number of zeros discovered before that 1
    for i in range(len(A)):
        if A[i] == 0:
            zero_counts += 1
        elif A[i] == 1:
            # if one is discovered then pairs is incremented by the numbers
            # of zeros we have had before that
            pairs += zero_counts
            if pairs > 1000000000:
                return -1
    return pairs
"""


"""
this is the max product of three
def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])



solution([-3, 1, 2, -2, 5, 6])"""


# from bisect import bisect_right


# def number_of_disc_intersections(A):
#     pairs = 0

#     # create an array of tuples, each containing the start and end indices of a disk
#     # some indices may be less than 0 or greater than len(A), this is fine!
#     # sort the array by the first entry of each tuple: the disk start indices
#     intervals = sorted([(i - A[i], i + A[i]) for i in range(len(A))])

#     # create an array of starting indices using tuples in intervals
#     starts = [i[0] for i in intervals]

#     # for each disk in order of the *starting* position of the disk, not the centre
#     for i in range(len(starts)):

#         # find the end position of that disk from the array of tuples
#         disk_end = intervals[i][1]

#         # find the index of the rightmost value less than or equal to the interval-end
#         # this finds the number of disks that have started before disk i ends
#         count = bisect_right(starts, disk_end)

#         # subtract current position to exclude previous matches
#         # this bit seemed 'magic' to me, so I think of it like this...
#         # for disk i, i disks that start to the left have already been dealt with
#         # subtract i from count to prevent double counting
#         # subtract one more to prevent counting the disk itsself
#         count -= i + 1
#         pairs += count
#         if pairs > 10000000:
#             return -1
#     return pairs


""" contains triangle
def solution(A):
    if len(A) < 3:
        return
    A.sort()
    for i in range(len(A) - 2):
        if A[i] + A[i+1] > A[i + 2]:
            return 1
    
    return 0
"""


""" brackets

def solution(S):
    # write your code in Python 3.6
    hash_map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    for char in S:
        if char in hash_map:
            stack.append(char)
        else:
            if len(stack) == 0:
                return 0
            if hash_map[stack[-1]] == char:
                stack.pop()
    
    if len(stack) != 0:
        return 0
    return 1
"""


""" fish
def solution(A, B):
    # write your code in Python 3.6
    final = 0
    stack = []
    for i in range(len(A)):
        if B[i] == 0:
            while len(stack) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                final += 1
        else:
            stack.append(A[i])
    final += len(stack)
    return final
"""


"""
stone wall challenge
def solution(H):
    # write your code in Python 3.6
    block_count = 0
    stack = []
    
    for height in H:
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()
        if len(stack) != 0 and stack[-1] == height:
            pass
        else:
            block_count += 1
            stack.append(height)
    return block_count
"""
"""
candidate last idx


def solution(A):
    candidate = ''
    candidate_count = 0
    
    for num in A:
        if candidate == '':
            candidate = num
            candidate_count += 1
        else:
            if num != candidate:
                candidate_count -= 1
                if candidate_count == 0:
                    candidate = ''
            else:
                candidate_count += 1
    
    if candidate_count == 0:
        return -1
    
    count = 0
    last_idx = 0
    for idx, val in enumerate(A):
        if val == candidate:
            count += 1
            last_idx = idx
    if count > len(A) // 2:
        return last_idx
    return -1

"""

""" equi leader
def solution(A):
    # write your code in Python 3.6
    candidate = ""
    candidate_count = 0
    
    for num in A:
        if candidate == "":
            candidate = num
            candidate_count += 1
        else:
            if candidate != num:
                candidate_count -= 1
                if candidate_count == 0:
                    candidate = ""
            else:
                candidate_count += 1
    
    leader_count = len([number for number in A if candidate == number])
    if leader_count <= len(A) // 2:
        return 0

    equi_leaders = 0
    leader_count_current = 0
    for i in range(len(A)):
        if A[i] == candidate:
            leader_count_current += 1
        if leader_count_current  > (i + 1) // 2 and leader_count - leader_count_current  > (len(A) - i - 1) // 2:
            equi_leaders += 1
    return equi_leaders
"""

"""
max slice sum
import math
def solution(A):
    # write your code in Python 3.6
    max_ending = max_slice = -math.inf
    for num in A:

        max_ending = max(num, max_ending + num)
        max_slice = max(max_slice, max_ending)
    
    return max_slice
"""
""" max profit
def solution(A):
max_profit, min_day = 0, 200000

for num in A:
    min_day = min(min_day, num)
    max_profit = max(max_profit, num - min_day)
return max_profit
"""

"""Given four digits calculate valid times that canbe displayed on 
a digital clock 00:00, latest 23:59
"""


# import itertools


# def solution(A, B, C, D):
#     A = [A, B, C, D]
#     return num_possible(A)


# def num_possible(A):
#     unique = set()
#     print(itertools.permutations(A))
#     for h1, h2, m1, m2 in itertools.permutations(A):
#         if 0 <= 10 * h1 + h2 < 24 and 0 <= 10 * m1 + m2 < 60:
#             unique.add((h1, h2, m1, m2))
#     return len(unique)


# print(solution(0, 0, 0, 0))


# import heapq


# import heapq

""" Find largest sibling, sibling is just shuffled digits"""

# def solution(N):
#     if 0 <= N <= 11:
#         return N
#     max_heap = extract_numbers(str(N))
#     result = 0
#     while len(max_heap) > 0:
#         num = -heapq.heappop(max_heap)
#         result = result * 10 + num
#         if result > 100000000:
#             return -1
#     return result


# def extract_numbers(N):
#     nums = []
#     for num in N:
#         heapq.heappush(nums, -(int(num)))
#     return nums


# print(solution(100000000))


def print_max(N):
    count = [0 for _ in range(10)]
    string = str(N)
    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] + 1

    result = 0
    multiplier = 1

    for i in range(10):
        while count[i] > 0:
            result = result + (i * multiplier)
            count[i] -= 1
            multiplier *= 10

    return result


print(print_max(552))
