from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        code = ""

        for word in strs:
            code += f"{chr(len(word))}{word}"

        return code

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str: str) -> List[str]:
        list = []
        index = 0

        while index < len(str):
            length = ord(str[index])
            list.append(str[index + 1 : index + 1 + length])
            index += length + 1

        return list
