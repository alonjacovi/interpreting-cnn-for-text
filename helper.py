from random import shuffle
import spacy

data_pos = []
data_neg = []
nlp = spacy.load("en_core_web_sm")

with open("rt-polarity.neg", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = [token.text for token in nlp(line.strip().lower()) if token.text != '']
        line = u' '.join(line)
        data_neg.append((1, line))
        print(1, line)

with open("rt-polarity.pos", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = [token.text for token in nlp(line.strip().lower()) if token.text != '']
        line = u' '.join(line)
        data_pos.append((2, line))
        print(2, line)

shuffle(data_pos)
shuffle(data_neg)

train = data_pos[:int(len(data_pos)*0.8)]
test = data_pos[int(len(data_pos)*0.8):]
train += data_neg[:int(len(data_neg)*0.8)]
test += data_neg[int(len(data_neg)*0.8):]

shuffle(train)
shuffle(test)

with open("mr_dataset/train.txt.tok", "w", encoding="utf-8") as f:
    with open("mr_dataset/train.cat", "w") as ff:
        for y,x in train:
            f.write(x)
            f.write('\n')
            ff.write(str(y))
            ff.write('\n')

with open("mr_dataset/test.txt.tok", "w", encoding="utf-8") as f:
    with open("mr_dataset/test.cat", "w") as ff:
        for y,x in test:
            f.write(x)
            f.write('\n')
            ff.write(str(y))
            ff.write('\n')
