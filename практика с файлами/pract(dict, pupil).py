pupils = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'sha',
        'Group': 43,
        'physics': 10,
        'informatics': 6,
        'history': 5,
    },
    {
        'firstname': 'asha',
        'Group': 44,
        'physics': 4,
        'informatics': 2,
        'history': 5,

    },
]

average = 0
count = 0
for i in pupils:
    for j in i:
        if j != 'Group' and j != 'firstname':
            count += 1
            average += i[j]
    average /= count
    count = 0
    i['average'] = average
    average = 0
for i in pupils:
    if i['average'] > 4:
        print(i['firstname'])