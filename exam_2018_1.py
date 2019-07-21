class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getItemPrice(self):
        return self.price

class BucketItem:
    def __init__(self, item, num):
        self.item = item
        self.num = num

    def getPrice(self):
        bucketPrice = self.num * self.item.getItemPrice()
        return bucketPrice

class Bucket:
    def __init__(self, BucketItemCollection):
        self.BucketItemCollection = BucketItemCollection

    def GetPrice(self):
        totalPrice = 0
        for b in self.BucketItemCollection:
            totalPrice = totalPrice + b.getPrice()
        return totalPrice

item1 = Item('Bread', 20)
item2 = Item('Butter', 70)
item3 = Item('Cheese', 50)

bucketItem1 = BucketItem(item1, 7)
bucketItem2 = BucketItem(item2, 3)
bucketItem3 = BucketItem(item3, 24)

bucket = Bucket((bucketItem1, bucketItem2, bucketItem3))

totalBucketPrice = bucket.GetPrice()
print(totalBucketPrice)

