class Solution:
    # lenght-prefix encoding
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the delimiter
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res