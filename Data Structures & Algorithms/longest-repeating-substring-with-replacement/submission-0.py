class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dict1 = {}
        max_ss = 0
        mostf = 0

        for r in range(len(s)):
            # 1) count s[r]
            if s[r] not in dict1:
                dict1[s[r]] = 1
            else:
                dict1[s[r]] += 1
            mostf = max(mostf, dict1[s[r]])  # track highest freq

            # 2) window size & validity check
            window_size = r - l + 1
            if window_size - mostf <= k:
                max_ss = max(max_ss, window_size)
            else:
                # 3) shrink from left
                dict1[s[l]] -= 1
                l += 1

        return max_ss
