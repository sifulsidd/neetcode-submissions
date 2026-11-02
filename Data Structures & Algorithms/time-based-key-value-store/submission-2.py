class TimeMap:

    def __init__(self):
        self.dic = {}
        self.arr = []
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        res = ""
        l, r = 0, len(self.dic[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.dic[key][m][0] <= timestamp:
                res = self.dic[key][m][1]
                l = m + 1
            else:
                r = m - 1
        return res
