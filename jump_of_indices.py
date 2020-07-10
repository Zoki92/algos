def hasSingleCycle(array):
    i = 0
    helper = []
    while i not in helper:
        helper.append(i)
        i = getNextIdx(i, array)
    return len(helper) == len(array) and i == 0


def hasSingleCycle2(array):
    num_visited = 0
    current_idx = 0
    while num_visited < len(array):
        if num_visited > 0 and current_idx == 0:
            return False
        num_visited += 1
        current_idx = getNextIdx(current_idx, array)
    return current_idx == 0

def getNextIdx(current_idx, array):
    jump = array[current_idx]
    next_idx = (current_idx + jump) % len(array)
    print(f"Current index: {current_idx}, Jump: {jump}. Next index: {next_idx}.")
    return next_idx if next_idx >= 0 else next_idx + len(array)


print(hasSingleCycle([1, 2, 3, 4, -2, 3, 7, 8, 1]))
print(hasSingleCycle2([1, 2, 3, 4, -2, 3, 7, 8, 1]))
