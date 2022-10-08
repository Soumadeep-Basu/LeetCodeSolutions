class TimeMap:

    def __init__(self):
        
        self.cache = {}
        
        
        self.returnValues = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.cache:
            time_dict = self.cache[key]
            time_dict[timestamp] = value
            
            self.cache[key].update(time_dict)
        else:
            new_dict = {}
            new_dict[timestamp] = value
        
            self.cache[key] = new_dict
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.cache:
            temp_result = self.cache[key]
        else: 
            return ""
        
        
        
        
        for i in range(timestamp, -1, -1):
            if i in temp_result:
                return temp_result[i]
                
        return ""

