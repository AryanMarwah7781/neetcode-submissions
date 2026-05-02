class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        from typing import List
from collections import defaultdict

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Collect indices for each value
        pos = defaultdict(list)   # maps value -> sorted list of indices where it appears
        for i, v in enumerate(nums):
            pos[v].append(i)

        # Count original k frequency
        orig_k = len(pos.get(k, []))
        best = orig_k  # baseline with no-op or x = 0

        # If there are no k's positions we still need pos_k list for sparse merge
        pos_k = pos.get(k, [])

        # For each distinct value v different from k, compute best gain for d = k - v
        for v, idx_v in pos.items():
            if v == k:
                continue  # d = 0 case already covered

            # Merge-scan positions of idx_v as +1 and pos_k as -1, zeros elsewhere
            i = j = 0
            cur = 0
            best_gain = 0  # we can always choose empty window, meaning gain 0

            # Standard Kadane over sparse events:
            # events are sorted by index, each contributes +1 or -1, gaps have 0 so do nothing
            while i < len(idx_v) or j < len(pos_k):
                # Decide next event by smaller index
                nxt_is_v = False
                if j >= len(pos_k):
                    nxt_is_v = True
                elif i < len(idx_v) and idx_v[i] <= pos_k[j]:
                    nxt_is_v = True

                if nxt_is_v:
                    cur += 1     # +1 for making nums[idx_v[i]] reach k with x = k - v
                    i += 1
                else:
                    cur -= 1     # -1 because a k inside the subarray would be destroyed when d != 0
                    j += 1

                # Kadane update
                if cur < 0:
                    cur = 0
                else:
                    if cur > best_gain:
                        best_gain = cur

            # Update global best
            if orig_k + best_gain > best:
                best = orig_k + best_gain

        return best