# Advanced Programming Project
## *progettopart1.py*
Progettopart1.py is the first file with the code containing part1 of the project and it is connected with part2 (*progettopart2.py*).

It contains a one class only named **Registry** which contains all of the operations that can be performed on the datasets contained in part2.

We used 2 different datasets:

- [disease evidences](https://github.com/anuzzolese/genomics-unibo/blob/master/2020-2021/project/dataset/disease_evidences.tsv.gz)
- [gene evidences](https://github.com/anuzzolese/genomics-unibo/blob/master/2020-2021/project/dataset/gene_evidences.tsv.gz)

We used Pandas in order to read the data in a dataframe format and to also use specific functions and methods.

In the code of *progettopart1.py* we first import everything (*) from the file *progettopart2* corresponding to part2 and then we also import pandas as pd. 

Afterwards we defined the class and all the possible operations carried out on the sets; each function is associated to a specific operation of part2.


## *progettopart2.py*
Progettopart2.py contains 5 different classes. 

Each one has: the mandatory function *__init__()*, which is called constructor and can take multiple arguments; and additional specific functions. 

The 5 classes are:

1. **DataCollection**: this class has the two datasets as input, contains two operations which are *shape()* and *get_label()* both returning lists.

- ***shape()***: can be used to return the number of rows and columns of the datasets by means of a built-in-function (*.shape*). 
- ***get_label()***: returns a list of the column labels of the datasets again by means of a built-in-function (*.columns.values*).

2. **Detection**: this class takes only one dataset as input, it contains two methods:

- ***genesymbol_detect()***: it takes in input the gene dataset. It returns a string containing the number of all different genes present in the dataset and lists them in sorted order. 

In order to do that, we created a new dataframe dfg, which was then sorted to dfs. Starting from the empty list l, we then appended to l the genes in dfs through a for loop.

- ***diseasename_detect()***: it refers to the disease dataset instead, and it returns a string containing the number of different diseases present in the dataset, listing their names in a sorted manner.

This function works in the same way as the previous one.

3. **Sentence**: this class takes a dataframe and an input n from the user. It performs 2 different operations:

- ***findsentence_d()***: this function, given a disease name (*disease_name*) or disease ID (*diseasesid*) in input by the user, returns a list of the sentences related to that disease.
- ***findsentence_g()***: this function, given a gene name (*gene_symbol*) or gene ID (*geneid*) in input by the user, returns a list of the sentences related to that gene. 

In both cases we used *.values.tolist()*, which converts a dataframe’s column into a list. 

We also used *.itertuples()* to iterate over the dataframe rows as tuples.

All of the values in the dataframe are transformed in a string format to avoid type errors, because the input from the user will be a string type object.

4. **TopTen**: this class takes in input both datasets (*datag*, *datad*) and the method *top_ten()*.

- ***top_ten()***: it returns a new dataframe containing 4 columns and 10 rows, corresponding to the 10 most abundant associations between genes and diseases.

We used *groupby()*, which groups the data according to the categories and applies the functions, and it also helps to aggregate data efficiently. 

We also used a Pandas built-in-function *.iloc[: , :]* to slice by position from first row to the tenth.

5. **AssociationList**: this class merges the two datasets (datag, datad) and performs one operation through the method association().

- ***association()***: it takes the user input (*inputs*) and looks for its presence in the lists of id (*id_lists*) and names of both diseases and genes (*symbol_list*).

If the input is in one of the lists, it iterates with *.itertuples()* over the rows of the merged dataset (stringresult) looking for a row corresponding to the input in one of the 4 columns. 

*Stringresult* comes from the merged dataset *result*, which was then converted into a string format thanks to *.astype(***str***)*.

If the match is found in a disease name or ID, the corresponding gene symbol is appended to the list *gene_list* (if not already present).

If the match is found in a gene symbol or ID, the corresponding disease name is appended to the list *disease_list* (if not already present). 

At the end *final_list* is chosen and returned to the user.

## *progettopart3.py*
Progettopart3.py is the last file of the code that imports part1 (Registry). 

Part3 aims to present all of the operations (as hyperlinks) that can be performed on the datasets. 

The operations are enabled by render template that connects the HTML pages to the hyperlinks in part1. In this way it is indirectly connected to part2. 

1. **/**:
Shows the nine possible operations that can be selected.

2. **/Meta**:
Shows the output of *DataCollection(datag, datad).shape()*

3. **/Sem**:
Shows the output of *DataCollection(datag, datad).get_label()*

4. **/Genes**:
Shows the output of *Detection(datag).genesymbol_detect()*

5. **/SG**:
Shows the output of *Sentence(datag).findsentence_g()*

6. **/Diseases**:
Shows the output of *Detection(datad).diseasename_detect()*

7. **/SD**:
Shows output of *Sentence(datad).findsentence_d()*

8. **/Top**:
Shows output of *TopTen(datag, datad).top_ten()*

9. **/GetoDis**:
Shows the output of *AssociationList(datag).association()*

10. **/DistoGe**:
Shows the output of *AssociationList(datad).association()*

The folder html contains all the HTML pages:

- [1homepage.html](https://github.com/cristina2300/Exam-Project/blob/main/html/1homepage.html)
- [2metadata.html](https://github.com/cristina2300/Exam-Project/blob/main/html/2metadata.html)
- [3semantics.html](https://github.com/cristina2300/Exam-Project/blob/main/html/3semantics.html)
- [4genes.html](https://github.com/cristina2300/Exam-Project/blob/main/html/4genes.html)
- [5genesentences.html](https://github.com/cristina2300/Exam-Project/blob/main/html/5genesentences.html)
- [6diseases.html](https://github.com/cristina2300/Exam-Project/blob/main/html/6diseases.html)
- [7diseasesentences.html](https://github.com/cristina2300/Exam-Project/blob/main/html/7diseasesentences.html)
- [8top10.html](https://github.com/cristina2300/Exam-Project/blob/main/html/8top10.html)
- [9genetodisease.html](https://github.com/cristina2300/Exam-Project/blob/main/html/9genetodisease.html)
- [10diseasetogene.html](https://github.com/cristina2300/Exam-Project/blob/main/html/10diseasetogene.html)

Each of them is composed of:
- ***Text-decoration properties:*** used to set the text color, line and style.
- ***Headings:*** titles or  subtitles displayed on the webpage.
- ***Buttons:*** connecting Homepage and Secondary pages together.
- ***Footer:*** contains names of the contributors.



*Presented and designed by Genomics’ second year students:*

*Ashley Claire Lipparini,* 

*Beatrice Ferretti,*

*Cristina Ilie,*

*Silia Gnesini.*


