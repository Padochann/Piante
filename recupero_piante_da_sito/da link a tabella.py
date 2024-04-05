import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# Leggi il file Excel con i link
excel_file = "D:\\informatica\\data_piante_link_img.xlsx"
plant_data = pd.read_excel(excel_file)

# Lista per memorizzare i dati estratti da ogni link
extracted_data = []
i = 0
# Itera attraverso ogni link nel DataFrame
for index, row in plant_data.iterrows():
    link = row["Link"]

    # Fai una richiesta GET al link
    response = requests.get(link)
    i += 1
    # Verifica se la richiesta ha avuto successo
    if response.status_code == 200:
        print(i)
        # Parsing del contenuto HTML della pagina
        soup = BeautifulSoup(response.content, "html.parser")

        # Trova la tabella desiderata (modifica questo passaggio in base alla struttura della tua pagina)
        table = soup.find("table", class_="specficationTable")

        # Estrai i dati dalla tabella se è stata trovata
        if table:
            # Inizializza un dizionario per memorizzare i dati estratti
            extracted_data_row = {}

            # Trova tutte le righe della tabella
            rows = table.find_all("tr")

            # Itera attraverso le righe
            for row in rows:
                # Estrai il testo dal primo elemento <th> e dal primo elemento <td> di ogni riga
                th_element = row.find("th")
                td_element = row.find("td")
                if th_element and td_element:
                    key = th_element.text.strip()
                    value = td_element.text.strip()
                    extracted_data_row[key] = value

            # Aggiungi i dati estratti dalla tabella alla lista
            extracted_data.append(extracted_data_row)

            # Trova l'elemento immagine con la classe "icon_difficulty_medium"
            img_element = soup.find("img", class_="icon_difficulty_medium")

            # Estrai l'URL dell'immagine se presente
            if img_element:
                img_url = img_element.get("src")
                extracted_data_row["Immagine"] = img_url

                # Estrai il livello di difficoltà dall'URL dell'immagine
                difficulty_level = re.search(r"icon_difficulty_(\w+)", img_url)
                if difficulty_level:
                    extracted_data_row["Difficoltà"] = difficulty_level.group(1)
                    extracted_data_row["Difficoltà"]+= ".png"
                else:
                    extracted_data_row["Difficoltà"] = "N/D"
            else:
                print(f"Nessuna immagine trovata nella pagina: {link}")

        else:
            print(f"Nessuna tabella trovata nella pagina: {link}")
    else:
        print(f"Errore nella richiesta GET al link: {link}")

# Converti i dati estratti in un DataFrame pandas
extracted_df = pd.DataFrame(extracted_data)

# Aggiungi il link come colonna nel DataFrame
extracted_df["Link"] = plant_data["Link"]

# Riordina le colonne del DataFrame per avere prima il link
extracted_df = extracted_df[
    ["Link"] + [col for col in extracted_df.columns if col != "Link"]
]

# Visualizza il DataFrame (opzionale)
print(extracted_df)

# Salva il DataFrame in un file Excel (opzionale)
extracted_df.to_excel("D:\\informatica\\dati_estratti.xlsx", index=False)

print("Salvato con successo.")
