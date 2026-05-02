class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # Hashmap with the char and the count
        maxHeap = []
        for char, count in count.items():
            maxHeap.append([(-count), char]) # neg count because default ==> min
        heapq.heapify(maxHeap) # heapifies based on the first index

        string = ""
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            count, char = heapq.heappop(maxHeap)
            string += char
            count += 1 # decrease by one because negative

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count != 0:
                prev = [count, char]
        return string
