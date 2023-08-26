
def data_collection(data1, data2, data3):
    with open('notes.csv', 'a+') as file:
        file.write(f"{data1}, {data2}, {data3}\n")
