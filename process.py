import datetime

def process_data():

    file1 = open('ethusdt.txt', 'r')
    file2 = open('btcusdt.txt', 'r')
    fileresult = open("result.txt", "w")


    lines1 = file1.readlines()
    lines2 = file2.readlines()

    file1.close()
    file2.close()
    data1 = {}
    data2 = {}
    min_time = int(lines1[0].split(' ')[1])
    first_time = True
    for i in range(len(lines1)):
        price1, time1 = lines1[i].split(' ')
        price1 = float(price1)
        time1 = time1
        price2, time2 = lines2[i].split(' ')
        price2 = float(price2)
        time2 = time2
        data1[time1] =price1
        data2[time2] = price2
    for index, time1 in enumerate(data1.keys()):
        if index == len(list(data1.keys()))-1:
            break
        timestamp1 = datetime.datetime.fromtimestamp(float(f"{time1[: -4]}.{time1[-4 :]}"))
        prices1 = list(data1.values())

        koof = prices1[index]/prices1[index+1]
        timestamp2_culc = (timestamp1+datetime.timedelta(minutes=5))
        for index2, time2 in enumerate(data2.keys()):
            timestamp2 = datetime.datetime.fromtimestamp(float(f"{time2[: -4]}.{time2[-4 :]}"))
            if timestamp2 > timestamp2_culc:

                break
        if first_time:
            first_time = False
            for i in range(0, index2-1):
                fileresult.write(f"{lines2[i]}")
        index2 = index2 - 1
        if index2 == len(list(data2.keys()))-2:
            break
        prices2 = list(data2.values())
        price2_culc = prices2[index2]*koof
        fileresult.write(f'{lines2[index2][:-1]} {prices2[index2+1]- price2_culc}\n')

    fileresult.close()
