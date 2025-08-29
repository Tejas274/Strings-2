class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        anagram_dict = {}
        result = []

        # anagram dict
        for i in range(len(p)):
            if p[i] in anagram_dict:
                anagram_dict[p[i]] += 1
            else:
                anagram_dict[p[i]] = 1

        temp = ""
        items_matched = 0

        for i in range(len(s)):
            temp_item = s[i]
            temp += temp_item
            # adding character
            if temp_item in anagram_dict:
                anagram_dict[temp_item] -= 1
                if anagram_dict[temp_item] == 0:
                    items_matched += 1

            if i > len(p) - 1:
                # removal of character
                temp_removal = temp[0]
                if temp_removal in anagram_dict:
                    anagram_dict[temp_removal] += 1
                    if anagram_dict[temp_removal] == 1:
                        items_matched -= 1
                temp = temp[1:]

            if items_matched == len(anagram_dict):
                result.append(i - len(p) + 1)

        return result