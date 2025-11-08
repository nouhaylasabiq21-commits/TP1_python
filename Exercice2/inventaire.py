from article import Article

a1 = Article("A001", "Clavier", 25.5, 10)
a2 = Article("A002", "Souris", 15.0, 20)
a3 = Article("A003", "Ecran", 150.0, 5)

articles = [a1, a2, a3]

for a in articles:
    print(a)

total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d inventaire : {total:.2f} dh")
