def porterStem1b(data):
    vowels = {"a", "e", "i", "o", "u"}
    for i in range(len(data)):
        if data[i][-3:] == "eed": #or data[i][-5:] == "eedly":
            for x in range(len(data[i][:-3])):
                if data[i][x] in vowels and data[i][x+1] not in vowels:
                    data[i] = data[i][:-1]
        elif data[i][-5:] == "eedly":
            for x in range(len(data[i][:-5])):
                if data[i][x] in vowels and data[i][x+1] not in vowels:
                    data[i] = data[i][:-3]
    return data

print(porterStem1b("free"))