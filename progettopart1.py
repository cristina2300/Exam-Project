

import pandas as pd
from progettopart2 import *

class Registry:
    def __init__(self):
        self.__datad = pd.read_csv('disease_evidences.tsv.gz', sep= '\t')
        self.__datag = pd.read_csv('gene_evidences.tsv.gz', sep = '\t')
        self.__operations = ['Metadata', 'Semantics', 'Genes', 'Diseases', 'List of sentences of genes related to COVID-19',
                            'List of sentences of diseases related to COVID-19', 'Top 10 associations',
                            'Disease list related to a gene symbol or ID', 'Gene list related to a disease name or ID']
        self.__hyperlinks  = ['Meta', 'Sem', 'Genes', 'Diseases', 'inputg', 'SG', 'inputd', 'SD', 'Top', 'GetoDis', 'DistoGe' ]
        

    def registry(self):
        return self.__operations

    def links(self):
        return self.__hyperlinks
    def metadata(self): 
        return DataCollection(self.__datad, self.__datag).shape()
    def semantics(self): #2
        return DataCollection(self.__datad, self.__datag).get_label()
    def genes(self): #3
        return Detection(self.__datag).genesymbol_detect()
    def inputg(self):
        return Inputg(self.__datag).list_genes()
    def inputd(self):
        return Inputd(self.__datad).list_diseases()
    def sentenceg(self): #4 
        return Sentence(self.__datag)
    def diseases(self): #5
        return Detection(self.__datad).diseasename_detect()
    def sentenced(self): #6 
        return Sentence(self.__datad)
    def top10(self): #7
        return TopTen(self.__datad, self.__datag).top_ten()
    def genetod(self): #8 
        return AssociationList(self.__datag, self.__datad)
    def diseasetog(self): #9 
        return AssociationList(self.__datag, self.__datad)
