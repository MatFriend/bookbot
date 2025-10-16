def sort_on(items):
    return items["num"]


def gen_report(dictionary):
    list = []
    for char in dictionary:
        list.append({"char": char, "num": dictionary[char]})
    list.sort(reverse=True, key=sort_on)
    return list

