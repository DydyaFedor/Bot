import json


def load_data():
    content = ""
    with open('data.json', 'r', encoding='utf-8') as f:
        content = f.read()
    # print(content)
    test_data = json.loads(content)
    return test_data


def get_question(test_data, num):
    str1 = test_data[num]['question']+"\n"
    answers = test_data[num]['answers']
    num = 0
    for answer in answers:
        num += 1
        str1 += f" {num} - {answer[0]} \n"
    str1 += "Введите номер верного ответа:"
    return str1
    
def check_answer(test_data, num, answer_num):
    result = 0
    if num < len(test_data):
        answers = test_data[num]['answers']
        if answer_num >= 1 and answer_num <= len(answers):
            if answers[answer_num-1][1] == True:
                result = 1
    return result


if __name__ == '__main__':
    test_data = load_data()
    quest = test_data[0]
