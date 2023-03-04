import json
data = []
quest1 = {}
quest1["quest"] = "Что такое ёжик?"
Answers = [
    ["птица", False],
    ["человек", False],
    ["млекопитающее", True]
]
quest1["answers"] = Answers
data.append(quest1)
jsonstring  = json.dumps(data,ensure_ascii=False)
print(jsonstring)
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(jsonstring)
