class Solution:
    # lenght-prefix encoding
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: # len + # + word - for every string in the list
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            j = s.find('#', i)
            print(j)
            length = int(s[i:j]) #because length is before # - j is position of #
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res