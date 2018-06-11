import pymongo

client = pymongo.MongoClient()
db = client.test
sevenday = db.sevenday
embody = db.embody
#book_id = collection.insert(book)
#collection.update({'author' : 'qiye'}, {'$set' : {'text' : 'python book'}})
#collection.find_one()
#collection.remove({'author':'qiye'})
for day in sevenday.find():
    print(day)
for e in embody.find():
    print(e)