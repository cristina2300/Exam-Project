

import pandas as pd
from progettopart2 import *

class Registry:
    def __init__(self):
        self._datad = pd.read_csv('disease_evidences.tsv', sep= '\t')
        self._datag = pd.read_csv('gene_evidences.tsv', sep = '\t')
        self._operations = ['Metadata', 'Semantics', 'Genes', 'Diseases', 'List of sentences of genes related to COVID-19',
                            'List of sentences of diseases related to COVID-19', 'Top 10 associations',
                            'Disease list related to a gene symbol or ID', 'Gene list related to a disease name or ID']
        self._hyperlinks  = ['Meta', 'Sem', 'Genes', 'Diseases', 'SG', 'SD', 'Top', 'GetoDis', 'DistoGe' ]
        
        
        
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
        def sentenceg(self): #4 
            return Sentence(self.__datag).find_sentenceg()
        def diseases(self): #5
            return Detection(self.__datad).diseasename_detect()
        def sentenced(self): #6 
            return Sentence(self.__datad).find_sentenced()
        def top10(self): #7
            return TopTen(self.__datad, self.__datag).top_ten()
        def genetod(self): #8 
            return AssociationList(self.__datag, self.__datad).association()
        def diseasetog(self): #9 
            return AssociationList(self.__datag, self.__datad).association()
