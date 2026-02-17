class Solution:
    def readBinaryWatch(self, turnedOn):
        result = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count("1") + bin(m).count("1")) == turnedOn:
                    result.append(f"{h}:{m if m>=10 else f"0{m}"}")
        return result