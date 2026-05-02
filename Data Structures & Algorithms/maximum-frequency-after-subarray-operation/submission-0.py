class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        from typing import List
from collections import defaultdict

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        We can add a single integer x to one contiguous subarray once.
        After that, we want the maximum count of value k in the array.

        Key idea:
        - An index contributes to final frequency of k if after the single operation
          its value becomes exactly k.
        - There are only two ways an index can end up as k:
            1) It already equals k, regardless of the chosen subarray, as long as that
               index is outside the modified subarray or the chosen x is 0.
            2) It is inside the modified subarray and we choose x = k - nums[i].
               Since x must be the same for the entire chosen subarray, all indices
               inside that subarray can only become k if they share the same delta
               d = k - nums[i].

        Therefore:
        - For any delta d, consider the binary array B_d where B_d[i] = 1 if nums[i] + d == k,
          else 0. If we choose x = d and apply it to a subarray, the count of k after
          the operation equals:
              existing_k_outside + sum of B_d over the chosen subarray
          but existing_k_outside is just the number of original k outside the chosen subarray.
          More simply, total final k count equals:
              original_k_count_outside + new_k_inside
          which equals
              original_k_total - original_k_inside + new_k_inside
          If d != 0, original_k_inside is the number of k already inside the chosen subarray.
          However, when x = d, indices inside with nums[i] == k will become k + d, thus
          they stop being k unless d == 0. That suggests we want a subarray that maximizes
              new_k_inside - original_k_inside   when d != 0
          and for d == 0, the operation changes nothing, so result is original_k_total.

        Observation simplifies further:
        - For a fixed d != 0, an index contributes +1 to the gain if nums[i] + d == k,
          contributes -1 if nums[i] == k, and contributes 0 otherwise.
        - We need the maximum subarray sum of this transformed array Gain_d.
        - Final answer is max over all d of original_k_total + max(0, max_subarray_sum(Gain_d)),
          and also consider d == 0 which yields original_k_total.

        However iterating all distinct d values naively is O(n^2).
        We can do better:
        - For each value v that appears in nums, d = k - v is determined.
        - We only need to consider deltas produced by values present in nums.
        - For each such d, we build the gain stream on the fly and compute Kadane in one pass.
        - Total time O(n * U) where U is number of distinct values. In worst case U = n, still O(n^2).
          But we can do it in O(n):
            Trick: one Kadane pass per unique d is expensive. Instead, process indices grouped by value.
            Construct an array A where each element is:
                +1 if nums[i] can be turned into k by using d = k - nums[i] and we tag it with that d
                -1 if nums[i] == k tagged with every d != 0
            That still couples across d.

        Practical efficient approach that is O(n log n):
        - Positions with nums[i] == k are "obstacles" for any nonzero d because they give -1.
        - For each d != 0 we only care about positions where nums[i] == k - d, which yield +1.
        - The optimal subarray for a fixed d starts and ends on positions from the set S_d of indices i with nums[i] == k - d, possibly spanning over segments of non-k elements, but should avoid too many k positions since they subtract.
        - We can compute for each d the best subarray using two-pointer over the merged positions of S_d and K where K is indices of nums[i] == k.
        - Use sliding window counting in O(n) total across all d if we traverse array once per index insertion, but complexity analysis is tricky.

        Simpler and fast in practice:
        - Build map from value to list of indices.
        - For each distinct value v != k:
            Gain_d arises from:
              +1 at indices in idx[v]
              -1 at indices in idx[k]
              0 elsewhere
          The max subarray sum of this sparse array can be computed by sweeping over the union of positions of idx[v] and idx[k] in order, aggregating gaps as 0.
          Kadane over sparse points is O(len(idx[v]) + len(idx[k])).
        - Summed over all v, this is O(n + sum_v len(idx[v]) + len(idx[k])) which is O(n * D_k + n) worst if we re-scan idx[k] each time, but since idx[k] is reused, the total is O(n * number_of_distinct_values) in worst case. Still acceptable for typical constraints and passes comfortably for medium difficulty.

        Implementation below uses the sparse Kadane per value v.
        """

        n = len(nums)

        # Collect indices for each value
        pos = defaultdict(list)          # maps value -> sorted list of indices where it appears
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