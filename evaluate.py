import csv
import example_nlu as en

rows = []


def readData():
    ii = [5, 6, 7, 8]
    jj = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    kk = [1, 2]

    for i in ii:
        for j in jj:
            for k in kk:
                try:
                    if j < 10:
                        with open(f'./data/dialog-0{i}-0{j}-0{k}.tsv', 'r') as read_obj:
                            csv_reader = csv.reader(read_obj, delimiter='\t')
                            for row in csv_reader:
                                if 'user' in row[0]:
                                    rows.append(row[1])
                    else:
                        with open(f'./data/dialog-0{i}-{j}-0{k}.tsv', 'r') as read_obj:
                            csv_reader = csv.reader(read_obj, delimiter='\t')
                            for row in csv_reader:
                                if 'user' in row[0]:
                                    rows.append(row[1])
                except:
                    pass

if __name__ == "__main__":
    readData()
    #l = en.predict('Kup cztery wody')
    #print(l)

    good = 0

    for r in rows:
        l = en.predict(str(r))
        if l != []:
            good += 1

    print(f'Accuracy: {good/len(rows)*100}%')

en.predict('rock and stone')