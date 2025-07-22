
# carregar dados da planilha
caminho =  'C:/dados/base_inicial.xlsx'

df1 = pd.read_excel(caminho, sheet_name='Relatório de Vendas')
df2 = pd.read_excel(caminho, sheet_name='Relatório de Vendas1')

print('----- Primeiro Relatório -----')
print(df1.head())