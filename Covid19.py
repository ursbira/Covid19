# Código em Python 3.9.6
# Versão 1: 15/07/2021                Última alteração 15/07/2021 18:24
#                 Após ter criado uma versão que lia os arquivos iniciais liberado pelo governo
#                 para treinar as habilidades com pandas, matplotlib numpy, PySimpleGUI e sqlit3
#                 decidi fazer esta nova versão para testar os aprimoramentos e também por que
#                 a versão anterior não lê mais o formato que o governo passou a liberar.
#                 Nesta versão não vou gravar em sqlit3, apenas tratar com dataframes e gerar
#                 os gráficos.
# Arquivo:  Baixar arquivo do site https://covid.saude.gov.br/
#                 Em 15/07/2021 baixa quatro arquivos .csv
import pandas as pd
import os
import locale

# Atribui o local da máquina ao locale
locale.setlocale(locale.LC_ALL, '')

# Formata os valores antes com o ponto como separador de milhar com o
# (grouping=True), a vírgula como decimal, o %10.2f defini o tamanho
# como 10 para tabular alinhado e o .2f para ficar com 2 casas decimais
# apesar de já ter usado o round antes deixei para ficar como exemplo.
vlr_transf = 21745986.17
vlr_transf_str = locale.format_string('%10.2f', vlr_transf, grouping=True)
      

pasta_atual = os.getcwd()
pasta_dados= 'dados'
pasta_relatorios = 'relatorios'
hist_painel_covidbr = 'HIST_PAINEL_COVIDBR_2021_Parte2_14jul2021.csv'
arquivo_entrada = os.path.join(pasta_atual, pasta_dados, hist_painel_covidbr)
arquivo_agrupar_regiao = os.path.join(pasta_atual, pasta_relatorios, 'agrupar_regiao.xlsx')
print(arquivo_entrada)
print(arquivo_agrupar_regiao)
df = pd.read_csv(arquivo_entrada, delimiter =';', encoding='utf-8')
# df = pd.DataFrame(lidos)
# print(df['semanaEpi'])
agrupar_regiao = df.groupby('regiao').mean()
print(agrupar_regiao)
# Salvar o arquivo em excel xlsx
writer = pd.ExcelWriter(arquivo_agrupar_regiao, engine='openpyxl')
# Cria a guia
agrupar_regiao.to_excel(writer, sheet_name='agrupar_região')
# Salva a planilha xslx
writer.save()