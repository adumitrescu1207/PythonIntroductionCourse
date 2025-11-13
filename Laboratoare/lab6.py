import numpy as np
import pandas as pd
import csv

#1

# valori = np.random.randint(100, 1001, size=20)
# print("Lista inițială de valori întregi:")
# print(valori)

# valori_modificate = valori * 1.2
# print("Lista după creșterea fiecărui element cu 20%:")
# print(valori_modificate)

# suma = np.sum(valori_modificate)
# media = np.mean(valori_modificate)

# print(f"\nSuma valorilor modificate: {suma}")
# print(f"Media valorilor modificate: {media}")

#2

# tablou = np.random.rand(4, 3) * 10
# print("Tabloul original (float):")
# print(tablou)

# np.save("tablou_original.npy", tablou)
# print("\nTabloul original a fost salvat în 'tablou_original.npy'.")


# tablou[0, :] += 1
# print("\nTabloul după incrementarea primei linii cu 1:")
# print(tablou)

# tablou[:, 1] *= 2
# print("\nTabloul după dublarea valorilor de pe a doua coloană:")
# print(tablou)

# tablou[-1, :] *= -1
# print("\nTabloul după schimbarea semnului elementelor de pe ultima linie:")
# print(tablou)

# tablou[:, 2] = 0
# print("\nTabloul după înlocuirea valorilor de pe coloana 3 cu 0:")
# print(tablou)

# tablou_original = np.load("tablou_original.npy")
# print("\nTabloul original încărcat din fișier:")
# print(tablou_original)

# diferenta = tablou - tablou_original
# print("\nDiferența dintre tabloul modificat și tabloul original:")
# print(diferenta)

#3

nume_fisier = "inventar.csv"

date_articole = [
    ["DenumireArticol", "Stoc", "PretUnitar"],
    ["Minge Fotbal", 50, 30.0],        
    ["Rachetă Tenis", 10, 120.0],       
    ["Adidași Alergare", 25, 80.0],     
    ["Tricou Sport", 10, 20.0],        
    ["Echipament Înot", 5, 250.0],      
    ["Bicicletă MTB", 2, 1500.0]  
]

with open(nume_fisier, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(date_articole)

print(f"Fișierul '{nume_fisier}' a fost creat cu inventarul magazinului sportiv.")

df = pd.read_csv(nume_fisier)
print("\nPrimele 3 linii ale DataFrame-ului:")
print(df.head(3))
print("\nInformații despre primele 3 linii:")
print(df.head(3).info())

def valoare_stoc(stoc, pret_unitar):
    return stoc * pret_unitar

stoc_pret = df[["Stoc", "PretUnitar"]]

valoare_totala = stoc_pret.apply(lambda row: valoare_stoc(row["Stoc"], row["PretUnitar"]), axis=1).sum()
print(f"\nValoarea totală a tuturor articolelor din magazin: {valoare_totala}")

df_valoare_mare = df[stoc_pret.apply(lambda row: valoare_stoc(row["Stoc"], row["PretUnitar"]), axis=1) > 1000]
print("\nArticole cu valoarea stocului peste 1000:")
print(df_valoare_mare)

fisier_nou = "inventar_valoare_mare.csv"
df_valoare_mare.to_csv(fisier_nou, index=False)
print(f"\nDataFrame-ul cu articole de valoare mare a fost salvat în '{fisier_nou}'.")
