phone_book = {'Denis': 81002223456, 'Max': 82003334567, 'Kolya': [2354, 5646]}
print(f"create dictionary - {phone_book}, {type(phone_book)}")
# print("value type of 'Kolya' -", type(phone_book['Kolya']))

# item = phone_book["Denis"]
# print("take element by key 'Denis': ", item, " type is ", type(item))
# item = phone_book.get('Kamila', "there is no such item")
# print("take not existing element by key 'Kamila': ", item)

# phone_book["Denis"] = 83004445678
# print("change item 'Denis' -", phone_book["Denis"])
# phone_book['Anton'] = 84005556789
# print("add new item -", phone_book)
phone_book.update({'Sasha': 85006667890,
                  'Alex': 86007778901})
print("add set of items -", phone_book)