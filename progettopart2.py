import pandas as pd 

diseasedata = pd.read_csv('disease_evidences.tsv.gz',sep = '\t')
disease_evidences = pd.DataFrame(diseasedata)

genedata = pd.read_csv('gene_evidences.tsv.gz', sep = '\t')
gene_evidences = pd.DataFrame(genedata)


#PARTE 2 

class DataCollection:         #punto 1 e punto 2
    def __init__(self, dataframe1, dataframe2):
        self._dataframe1 = dataframe1
        self._dataframe2 = dataframe2
    
    def shape(self):
        l = [self._dataframe1.shape , self._dataframe2.shape]
        return l
    
    def get_label(self):
        a = list(self._dataframe1.columns.values)
        b = list(self._dataframe2.columns.values)
      
        return a, b




class Detection:
  def __init__(self, dataframe):
    self._dataframe = dataframe
    

  def genesymbol_detect(self):
    l = []
    dfg = pd.DataFrame(gene_evidences['gene_symbol'])
    dfs = dfg.gene_symbol.sort_values()
    for e in dfs:
        if e not in l:
            l.append(e)
  
    return (f"there are {len(l)} different genes with symbols {l}")
  
    
  def diseasename_detect(self):
    l1 = []
    dfd = pd.DataFrame(disease_evidences['disease_name'])
    dfsd = dfd.disease_name.sort_values()
    for e in dfsd:
        if e not in l1:
            l1.append(e)
    
    return (f"there are {len(l1)} different diseases with names {l1}")



class Inputg:
   def __init__(self, datag):
        self.__datag = datag

   def list_genes(self):
        genes = self.__datag['gene_symbol']
        list_genes = genes.drop_duplicates.tolist()
        return list_genes


       
class Inputd:
    def __init__(self,datad):
        self.__datad = datad

   def list_diseases(self):
        diseases = self.__datad['disease_name']
        list_diseases = diseases.drop_duplicates.tolist()
        return list_diseases
    


class Sentence:
    def __init__ (self, dataframe,n): 
        self._n = n
        self._dataframe = dataframe
  

    def find_sentenced(self):
        disease_list = []
        dataframe = self._dataframe[['sentence', 'diseaseid', 'disease_name']].astype(str)
  
        diseases = dataframe.disease_name.values.tolist()
        diseaseid= dataframe.diseaseid.values.tolist()
    
  
        if n in diseases or n in diseaseid :
       
            for row in dataframe.itertuples():
                if row.disease_name == n or row.diseaseid == n:
                    disease_list.append(row.sentence)
    
        return sentence_list
  
    def find_sentenceg(self):
        gene_list = []
        dataframe = self._dataframe[['sentence', 'geneid', 'gene_symbol']].astype(str)
        genes = dataframe.gene_symbol.values.tolist()
        geneid =  dataframe.geneid.values.tolist()
        
        if n in genes or n in geneid :
           
            for row in dataframe.itertuples():
                if row.gene_symbol == n or row.geneid == n:
                    gene_list.append(row.sentence)
        
        return gene_list
     
class TopTen:
    def __init__(self, datag, datad):
        self._datag = datag
        self._datad = datad
    
    def top_ten(self):
        result = pd.DataFrame.merge(self._datag, self._datad)
        grouped = result.groupby(by = ["geneid","gene_symbol", "diseaseid", "disease_name"]).size().reset_index(name = 'counts').sort_values('counts', ascending = False)
        final_sorted = grouped.iloc[0:10, :]
        return final_sorted
        
     
class AssociationList:
    def __init__(self, datag, datad, inputs):
        self._datag = datag
        self._datad = datad
        self._inputs = inputs
        
    def association(self):
        result = pd.DataFrame.merge(self._datag, self._datad)
        
       
        stringresult = result[['geneid','diseaseid','gene_symbol', 'disease_name']].astype(str)
        id_list = stringresult.geneid.values.tolist()
        symbol_list = stringresult.gene_symbol.values.tolist()
        id_disease = stringresult.diseaseid.values.tolist()
        diseasename = stringresult.disease_name.values.tolist()
        disease_list = []
        gene_list = []
        disease = bool()
       
        if inputs in id_list or inputs in symbol_list :
            for row in stringresult.itertuples():
                
                if row.gene_symbol == inputs or row.geneid == inputs :
                    disease = False
                    if row.disease_name not in disease_list:
                        disease_list.append(row.disease_name)
             
         
    
        elif inputs in id_disease or inputs in diseasename:
            for row in stringresult.itertuples():
            
                if row.disease_name == inputs or row.diseaseid == inputs:
                    disease = True
                    if row.gene_symbol not in gene_list:
                      
                        gene_list.append(row.gene_symbol)
         
        
        
        if disease:
            final_list = gene_list
        else:
            final_list = disease_list
        return final_list
        
    
       
               





