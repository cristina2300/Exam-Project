# Advanced Programming Project
## *progettopart1.py*
Progettopart1.py is the first file with the code containing part1 of the project and it is connected with part2 (*progettopart2.py*).

It contains a one class only named **Registry** which contains all of the operations that can be performed on the datasets contained in part2.

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


