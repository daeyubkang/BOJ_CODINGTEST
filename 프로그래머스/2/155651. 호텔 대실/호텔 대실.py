def solution(book_time):
    answer = 1
    arr1 = []

    for i in book_time:
        arr1.append([int(i[0].split(":")[0]) * 60 + int(i[0].split(":")[1]),
                     int(i[1].split(":")[0]) * 60 + int(i[1].split(":")[1])])

    arr1 = sorted(arr1, key=lambda x: x[0])

    rooms = [arr1[0][1] + 10]

    for i in range(1, len(arr1)):
        start = arr1[i][0]
        end = arr1[i][1] + 10

        flag = True

        for j in rooms:
            if start >= j:
                rooms.remove(j)
                break

        rooms.append(end)
        rooms.sort()

    answer = len(rooms)

    return answer
