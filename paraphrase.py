def paraphrase(str):
    str.split
def run(text):
    text = text.lower()
    words = text.split()
    d = {}
    for i in range(len(words)):
        if words[i] not in d:
            d[words[i]] = 1
        else:
            d[words[i]] += 1

    status = "strong"

    for v in d.values():
        if v > 1:
            status = "weak"
    return status



print(run("this is my IS name"))