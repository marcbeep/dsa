"""
Given changes to stock price over a period as an
array of distinct integers, count the no. of spikes
in the stock price (K-Spikes).

- There are K elements from indices (0, i-1) that are
less than the price[i]
- There are at least K elements from indices (i+1, n-1)
that are less than the price[i]

Input: price=[1,2,8,5,3,4], K=2
Output: 2

Input: price=[7,2,3,9,7,4], K=3
Output: 0 (3 elements lower than 9 but only 2 lower than 9 on right)
"""

"""
Approach 1 - Naive: Check every element in price array if K-Spike or not

Time complexity - 
The main loop runs in O(N) time.
With the 2 inner loops, the first runs from 0 to i-1. 
Worst case, it runs i times for each i. This is O(N^2).
With the second inner loop, it runs from i+1 to N-1,
it also has a worst case of O(N^2). Therefore TC is O(N^2).

Space complexity - O(1)

Note: A more efficient algorithm can be done with Fenwick Trees.
"""


def kspikes(prices, K):
    N = len(prices)
    spikes = 0

    for i in range(N):
        smaller_before = 0
        smaller_after = 0

        for j in range(i):
            if prices[j] < prices[i]:
                smaller_before += 1

        for j in range(i + 1, N):
            if prices[j] < prices[i]:
                smaller_after += 1

        if smaller_before == K and smaller_after == K:
            spikes += 1

    return spikes


prices = [7, 2, 3, 9, 7, 4]
K = 3
spike_count = kspikes(prices, K)
print(f"Number of k-spikes: {spike_count}")
