from data import question_data
from question_model import Question

question_bank = []
for item in question_data:
    item_text = item["text"]
    item_answer = item["answer"]
    question_bank.append(Question(item_text, item_answer))

