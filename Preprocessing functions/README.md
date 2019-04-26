# Preprocessing functions

## 1 Motivation

I started to work on data science projects as an electrical engineer, with very little experience in the field of data preprocessing. One of the biggest challenges however, if not the biggest, was dealing with missing data, and textual data that needed to be transformed into numeric. After reading extensively on these 2 issues, and exploring the Kaggle kernels in search for ideas on how to deal with them, I came up with a couple of approaches that can be encountered in majority of the cases, and as an engineer, decided to make the process as *"automatic"* as possible by writing functions that would do all the tedious work while providing an *interactive* approach that would also help me to get familiar with the dataset and how different transformations might affect it. 

The functions I developed are meant for regression problems with a lot of missing and textual data, where it is necessary to convert all the features to numeric, and not to have any missing data *(in most of the cases, scikit-learn models for linear regression, svm, etc...)*. 

## 2 Functions

The library consists of 2 main functions, namely:

1. *handle*_*missing*_*data*, and
2. *text*_*to*_*numeric*

and two helper functions for plotting the the data before and after the handling process. Both of the main functions are *interactive* and the user should make choices on how to process the missing data or convert them to numeric. Every time a change is made, the "new" feature is plotted against the label, and the user can choose whether to keep the changes, or try to transform the data in a different way. Once the changes were accepted by the user, the old feature is dropped, and the new one is kept in the dataset instead. Both of the main function can also work in two modes:

* *"auto"* - which takes all the features that fulfill the criteria (all the features with missing data, or all the features with non-numeric data) and performs one-by-one the functions for each of them, or,
* *"list"* - that takes a list of features (or just one) and performs the functions for those features.

By default, the *"auto"* mode is chosen.

Functions can also take as arguments the path and the name of the file where the user want the function to write all the changes that it made (this is optional and by default, it does not log data, unless a log file path is given).


### 2.1 Missing data 

*handle*_*missing*_*data* takes the as input the training data, test data and the name of the label and outputs the the training and test data after the process has finished.   

It first plots the data against the label and provides some useful information, like the median price for each of the categories (in case of categorical features), or the Pearson correlation coefficient in case of continuous numeric features. It then allows the *user* to *impute* the features with missing data by applying one of the next approaches:

1. **Filling missing data with median values for that feature** - (in case of continuous numeric features),
2. **Fill with the most frequent value for the feature** - (in case of categorical features)
3. **Fill with custom value** - (in cases where missing data should be treated as a special case)
4. **Deleting the rows from the train set** - (only useful in cases where the missing data is only in the training set)
5. **Dropping the feature** - (When there is just no hope)

After the *user* made the choice, the function will plot the imputed data feature against the label again, and ask the *user* whether she/he is satisfied with the results. If not, the whole process will be repeated (taking the original data as the starting point), until a strategy that works is found. 

Since the user had the chance to get to know the data a bit better while imputing the missing data, for non-numeric features, the user is given the option of immediately performing the conversion to numeric data, by calling the *text*_*to*_*numeric* function for that one particular feature.

### 2.2 Conversion to numeric data

*text*_*to*_*numeric* was made for 2 purposes:

* Conversion of textual to numeric features,
* Reducing the number of possible values for categorical features (both numeric and non-numeric)

It can be done in 2 possible ways, one of them being the *binarization* of the data (making a new *one-hot-encoded* feature for each of the possible values), and the other one being the manual conversion. 
In case of manual conversion, a new feature is created, and all the data is given a *starting value*. After that, all the other values should be given by the *user*, as well as the categories in the original set, to which these values correspond. To make it easier to explain, I will give an _**example**_:

oooooooooooooooooooooooooooooooooooooooooooooooooooooooo

*Conversion of an ordinal textual feature with possible values of : "Bad, Average and Good". The user wants to convert this to a new feature that would be numeric and where those instances that have the value of *"Bad"* will now have the value of 1, *"Average"* maps to 2, and *"Good"* to 3.*

The user would first give the number of possible values that the new feature should have (3 in this case). Then, the user will be prompted to put input the *starting value*, that will be given to every instance in the new feature (*for example*: 1). Lastly, the user will be prompted to input each of the new values, and to which categories it corresponds. In this case it would mean first choosing *"Average"* and assigning it the value of 2, and lastly choosing *"Good"* and assigning the value 3 to it.

oooooooooooooooooooooooooooooooooooooooooooooooooooooooo


*text*_*to*_*numeric* works very similar to the function for handling missing data. Given a set of features that are categorical, it first allows the user to choose between converting to numeric or dropping the feature immediately. If the user chose to convert the feature to numeric, the function for converting one feature to numeric is called (*Note* - even though the function is called *text*_*to*_**numeric**, it an also be used for features that are already numeric, but some *clustering* of the data is required).

In case the number of different values for the feature is the same in the training and the test data, the user gets to choose between manually performing the conversion, or just calling the *get*_*dummies* function (that makes a new feature for each of the possible values, and assigns the one-hot encoded values, indicating whether the data had that value in the original data set or not). If *get*_*dummies* function was called for datasets with different number of values present in the train and test set, it would cause the two sets to become of different dimensions (*number of features*), and would therefore make the model incapable of predicting on the test set.

In the other case, manual conversion is necessary. It creates a new feature with the same name as the original, just with the sufix *"_Bin"* appended to it. The user then performs the conversion following the example that was given above, and at the end, the new feature is kept in the data set, while the old one is dropped.

## 3 Conclusion

I hope that this short description was useful. Give the functions a try, and feel free to use them and change per wish. Any kind of feedback, especially the negative feedback, is more then welcome. 

