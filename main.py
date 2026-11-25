import pandas as pd


LicitacaoGov = pd.read_csv(
    '201301_EmpenhosRelacionados.csv',
    encoding='latin-1', sep=';', low_memory=False)

print(LicitacaoGov)  # Print the number of rows
