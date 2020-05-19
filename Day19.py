class StockSpanner:

    def __init__(self):
        self.a = []
        

    def next(self, price: int) -> int:
        count = 1
        while len(self.a) > 0 and price >= self.a[-1][0]:
            count += self.a.pop()[1]
        self.a.append((price,count))
        
        return count