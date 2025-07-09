import openpyxl
import pathlib

PATH = pathlib.Path(__file__).parent / "workbook.xlsx"

# Carrega o workbook existente
workbook = openpyxl.load_workbook(PATH)

# Nome para a planilha
sheet_name = "Teste"

# Selecionou a planilha
worksheet = workbook[sheet_name]

for row in worksheet.iter_rows():
    for cell in row:
        print(cell.value)

print(worksheet["A1"].value)  # Acessa o valor da célula A1
print(worksheet["B2"].value)  # Acessa o valor da célula B2
print(worksheet["C3"].value)  # Acessa o valor da célula C3
worksheet["A1"] = "Novo Valor"  # Modifica o valor da célula A1
print(worksheet["A1"].value)  # Verifica o novo valor da célula
