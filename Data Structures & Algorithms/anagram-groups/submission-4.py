class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_words={}
        for word in strs:
            temp=''.join(sorted(word))
            print(type(temp))
            if temp in dict_words:
                list1=dict_words[temp]
                list1.append(word)
                dict_words[temp]=list1
            else:
                list1=[word]
                dict_words[temp]=list1
        list_final=[]
        for k,v in dict_words.items():
            list_final.append(v)
        return list_final


        