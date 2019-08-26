


#2 
import os
a = input("好きな色は？")
with open("p132.txt", "w", encoding="utf-8") as f:
    f.write(a)



#3
import csv
csv_list = [["Top Gun", "Risky Business", "Moinority Report"],["Titanicc", "The Rvenant", "Inception"],["training Day", "man on fire", "Flight"]]

with open("P132_2.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Moinority Report"])
    w.writerow(["Titanicc", "The Rvenant", "Inception"])
    w.writerow(["training Day", "man on fire", "Flight"])

import csv
csv_list = [["Top Gun", "Risky Business", "Moinority Report"],["Titanicc", "The Rvenant", "Inception"],["training Day", "man on fire", "Flight"]]
with open("csvfile.csv", "w") as f:    
    file_writer = csv.writer(f, delimiter=",")
    for csvroop in csv_list:        
        file_writer.writerow(csvroop)


#4

import csv
>>> csv_list2 = [["トップ・ガン", "リスキー・ビジネス", "マイノリティー・リポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレーニング・デイ", "マン・オン・ファイア", "フライト"]]
>>> with open("csvjp.csv", "w", encoding="cp932", newline='') as f:
	csv_writer = csv.writer(f, delimiter=",")
	for csvroop in csv_list2:
		csv_writer.writerow(csvroop)
