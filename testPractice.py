st = "Hello World!"

print(st[::-1])

ls = ["Shaek", 2, 3, 1.1, 0.0001, "Darko"]

print(ls)
ls.insert(0, "Shaek")
print(ls)
del ls[0]
print(ls)

tup = ("Tuple1", 2, 3, 1.1, 0.0001, "Tuple2")

print(tup)

days = {
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
    "Saturday": "Holiday",
    "Sunday": {"Hangover": 1, "Undertow": 2, "Birria": "Yeah"},
}

for day in days:
    print(day + ":" + str(days[day]))

for index, day in enumerate(days):
    print(str(index) + ":" + day)
