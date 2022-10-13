x = input("Введите название файла ")
file = open(x+".txt","a")
while(True):
    i = input()
    if i =='0': break
    if not(i.isalpha())or len(i)<3:
        print("Данные не будут записанны")
        continue
    file.write(i+'\n')
file.close()
