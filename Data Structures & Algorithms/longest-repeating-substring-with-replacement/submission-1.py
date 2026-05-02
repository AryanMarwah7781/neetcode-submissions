from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0:
            return 0

        # 1) Build per-letter buckets: positions where each letter appears
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        best = 0

        # 2) For each target letter, run two pointers over its positions
        for ch, arr in pos.items():
            l = 0
            # arr = sorted indices where ch appears (already in order)
            for r in range(len(arr)):
                # Tighten left until the span needs ≤ k replacements
                # gaps = (span length) - (# of target letters inside)
                # span length between arr[l]..arr[r] is arr[r] - arr[l] + 1
                # # of target letters inside is (r - l + 1)
                while l <= r:
                    span_len = arr[r] - arr[l] + 1
                    count_ch = (r - l + 1)
                    gaps = span_len - count_ch
                    if gaps <= k:
                        break
                    l += 1  # too many non-ch inside; move left up

                # leftover replacements after filling internal gaps
                rem = k - gaps
                # We can extend at most 'rem' more characters beyond the span,
                # bounded by the string ends.
                cand = min(n, span_len + rem)
                if cand > best:
                    best = cand

        return best
