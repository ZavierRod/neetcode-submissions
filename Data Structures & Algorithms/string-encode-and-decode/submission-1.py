class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        encoded = []

        for s in strs:
            codes = []
            for c in s:
                codes.append(str(ord(c)))

            encoded.append(",".join(codes))

        return ".".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        ans = []

        for word in s.split("."):
            decoded_word = ""

            if word != "":
                for code in word.split(","):
                    decoded_word += chr(int(code))

            ans.append(decoded_word)

        return ans