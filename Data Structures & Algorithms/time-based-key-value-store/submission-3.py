class TimeMap:

    def __init__(self):
        self.dict1={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict1:
            temp_dict=self.dict1[key]
            temp_dict[timestamp]=value
            self.dict1[key]=temp_dict
        else:
            temp_dict={}
            temp_dict[timestamp]=value
            self.dict1[key]=temp_dict
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict1:
            return ""
        # now times is already in ascending order
        times = list(self.dict1[key].keys())

        # too early?
        if timestamp < times[0]:
            return ""
        # at or beyond the latest?
        if timestamp >= times[-1]:
            return self.dict1[key][times[-1]]

        # binary‐search for floor timestamp
        l, r = 0, len(times) - 1
        while l <= r:
            m = (l + r) // 2
            t = times[m]
            if t == timestamp:
                return self.dict1[key][t]
            elif t < timestamp:
                l = m + 1
            else:
                r = m - 1

        # r is now the index of the largest time < timestamp
        return self.dict1[key][times[r]]

                    


            
