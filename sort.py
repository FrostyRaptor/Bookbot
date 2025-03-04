def sort_on(d):
    return d["num"]

def sort_dict(dict):
    sorted_lst = []

    for char in dict:
        sorted_lst.append({"char": char, "num": dict[char]})
 
    sorted_lst.sort(reverse=True, key=sort_on)
    return sorted_lst