class TimeEntry:
    def __init__(self, value: str, timestamp: int):
        self.value = value
        self.timestamp = timestamp


class TimeMap:

    def __init__(self):
        self.timeHashMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeHashMap:
            self.timeHashMap[key] = []
        self.timeHashMap[key].append(TimeEntry(value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeHashMap:
            return ""
        
        entries = self.timeHashMap[key]
        lo, hi = 0, len(entries) - 1
        found = ""
            
        while lo <= hi:
                mid = (lo + hi) // 2
                if entries[mid].timestamp <= timestamp:
                    found = entries[mid].value
                    lo = mid + 1
                else:
                    hi = mid - 1
            
        return found


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)