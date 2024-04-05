import pandas as pd

# Carica entrambi i file Excel
excel_file_1 = "D:\\informatica\\dati_estratti.xlsx"
excel_file_2 = "D:\\informatica\\data_piante.xlsx"

df1 = pd.read_excel(excel_file_1)
df2 = pd.read_excel(excel_file_2)

# Unisci i DataFrame in base alla colonna "Link"
merged_df = pd.merge(df1, df2, on="Nome Pianta")

# Visualizza il DataFrame risultante
print(merged_df)

# Salva il DataFrame unito in un nuovo file Excel in un percorso diverso
merged_df.to_excel("D:\\informatica\\dati_completi_nuovo.xlsx", index=False)
