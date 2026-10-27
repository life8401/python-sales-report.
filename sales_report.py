prodazhbi = [15, 35, 50, 20, 40]

obshto = sum(prodazhbi)
broi = len(prodazhbi)
sredna_stoinost = obshto / broi
nai_golyama = max(prodazhbi)
nai_malka = min(prodazhbi)

print("Отчет за продажбите")
print("--------------------")
print("Обща сума:", obshto, "евро")
print("Брой продажби:", broi)
print("Средна стойност:", sredna_stoinost, "евро")
print("Най-голяма продажба:", nai_golyama, "евро")
print("Най-малка продажба:", nai_malka, "евро")
