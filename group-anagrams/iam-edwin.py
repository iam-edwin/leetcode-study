from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map: Dict[str, List[str]] = {}  # type: ignore
        for str in strs:
            groupKey = self.makeGroupKey(str)
            if groupKey in map:
                map[groupKey].append(str)
            else:
                map[groupKey] = [str]

        return [value for value in map.values()]

    def makeGroupKey(self, str) -> str:
        map = {}
        for char in str:
            if char in map:
                map[char] = map[char] + 1
            else:
                map[char] = 1

        groupKey = ""

        for key, item in sorted(map.items()):
            groupKey += f"{key}{item}"

        return groupKey
