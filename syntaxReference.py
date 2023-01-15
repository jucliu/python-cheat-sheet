# reverse for loop
import collections

prices = [1, 2, 3, 4]
n = len(prices)
for i in range(n - 2, -1, -1):
    print(prices[i])


# all() - The all() function returns True if all items in an iterable are true, otherwise it returns False.
# get defaultdict map values - tracker.values()
def isAnagram(s: str, t: str) -> bool:
    tracker = collections.defaultdict(int)
    for x in s: tracker[x] += 1
    for x in t: tracker[x] -= 1

    return all(x == 0 for x in tracker.values())
