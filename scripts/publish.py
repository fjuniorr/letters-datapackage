import os # para extrair o valor da variavel de ambiente DADOSMG_DEV contendo a chave da API CKAN
from dpkgckanmg.publish import publish
from dpkgckanmg.createResource import criarArquivo2
from dpkgckanmg.updateDataSet import dataSet

publish('/Users/fjunior/Local/cge/dados-mg/letters-datapackage/', os.environ['DADOSMG_DEV'])
