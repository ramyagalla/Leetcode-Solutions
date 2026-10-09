class MyHashMap:

    def __init__(self):
        self.x=[]
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.x)):
           if self.x[i][0]==key:
            self.x[i][1]=value
            return 
        self.x.append([key,value])

    def get(self, key: int) -> int:
        for i in range(len(self.x)):
            if  self.x[i][0]==key:
               return self.x[i][1]
        return -1
    def remove(self, key: int) -> None:
        for i in range(len(self.x)):
            if self.x[i][0]==key:
               self.x.pop(i)
               return