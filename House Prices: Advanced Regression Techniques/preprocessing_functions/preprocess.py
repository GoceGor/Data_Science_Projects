import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

from IPython.display import clear_output



def text_to_numeric_one_category(train_data, test_data, label, category, action_list):
    cols = []
    vals = []
    label = label
    clear_output(wait = "True")
    print_important_info_object(train_data, test_data, category, label)
    if len(train_data[category].value_counts().index.values) != len(test_data[category].value_counts().index.values):
        print("Set of values for", category, "category not the same in the test and the train data set:")
        print("Given values in the train set:", train_data[category].value_counts().index.values)
        print("Given values in the test set:", test_data[category].value_counts().index.values)
        print("Manual conversion to numeric feature of the", category, "category is necessary")
        train_cpy = train_data.copy()
        while True:
            new_name = category + "Bin"
            num_cats = 0
            while True:
                num_cats = input("How many values for the new category do you want to have?")
                try:
                    num_cats = int(num_cats)
                    break
                except:
                    print("Invalid value, only integeres accepted!")
            train_cpy[new_name] = 1
            del cols[:]
            del vals[:]
            print("All the data is now initialized with the value of 1")
            for i in range(0,num_cats-1):
                cols.append(input("Type all the columns that will have the next value: (format - col1,col2,col3,....,coln)"))
                while True:
                    newvl = input("Type the value: (starting value is always 1)")
                    try:
                        vals.append(int(newvl))
                        break
                    except:
                        print("Value: \’", newvl, "\’ not recognized! Only integers are accepted!")
                        continue
                cols_list = list(cols[i].split(','))
                train_cpy.loc[(train_cpy[category].isin(cols_list)), new_name] = vals[i]
            #clear_output(wait=True)
            print("Data distribution after conversion to numeric the data:")
            print_important_info_numeric(train_cpy, new_name, label)
            while True:
                repeat = input("Type \'keep\' if you want to keep the data like this,\’repeat\’ if you want to repeat the process or \'drop\' to discard it after all:")
                if repeat == "keep":
                    train_data[new_name] = 1
                    test_data[new_name] = 1
                    action_list.append("Conversion to numeric method : Manual (neccessary method):")
                    action_list.append('\n')
                    to_be_filled = "New name : " + new_name
                    action_list.append(to_be_filled)
                    action_list.append('\n')
                    to_be_filled = "Number of values : " + str(len(cols)+1)
                    action_list.append(to_be_filled)
                    action_list.append('\n')
                    for j in range(len(cols)):
                        action_list.append(cols[j])
                        action_list.append(' : ')
                        action_list.append(vals[j])
                        action_list.append('\n')
                        cols_list = list(cols[j].split(','))
                        train_data.loc[(train_data[category].isin(cols_list)), new_name] = vals[j]
                        test_data.loc[(test_data[category].isin(cols_list)), new_name] = vals[j]
                    train_data.drop([category], axis = 1, inplace = True)
                    test_data.drop([category], axis = 1, inplace = True)
                    return train_data, test_data
                    #break
                elif repeat == "repeat":
                    break
                elif repeat == "drop":
                    action_list.append("Feature dropped during the conversion process, reason : ")
                    reason = input("Why are you dropping the feature?")
                    try:
                        action_list.append(reason)
                    except:
                        action_list.append("No reason given!")
                    train_data.drop([category], axis = 1, inplace = True)
                    test_data.drop([category], axis = 1, inplace = True)
                    return train_data, test_data
                else:
                    print("Action", repeat, "not recognized!")
                    continue

    else:
        while True:
            action = input("Do you want to manually label the data, or call the get_dummies method? (\"man\" = manual, \"dum\" = get_dummies)")
            if action == "dum":
                action_list.append("Binarization method : get_dummies bin")
                action_list.append('\n')
                train_data = pd.get_dummies(train_data, prefix=[category], columns=[category])
                test_data = pd.get_dummies(test_data, prefix=[category], columns=[category])
                return train_data, test_data
                break
            elif action == "man":
                print("Manual conversion to numeric of the", category, "category")
                train_cpy = train_data.copy()
                while True:
                    new_name = category + "Bin"
                    num_cats = 0
                    while True:
                        num_cats = input("How many values for the new category do you want to have?")
                        try:
                            num_cats = int(num_cats)
                            break
                        except:
                            print("Invalid value, only integeres accepted!")
                    train_cpy[new_name] = 1
                    del cols[:]
                    del vals[:]
                    print("All the data is now initialized with the value of 1")
                    for i in range(0,num_cats-1):
                        cols.append(input("Type all the columns that will have the next value: (format - col1,col2,col3,....,coln)"))
                        while True:
                            newvl = input("Type the value: (starting value is always 1)")
                            try:
                                vals.append(int(newvl))
                                break
                            except:
                                print("Value: \’", newvl, "\’ not recognized! Only integers are accepted!")
                                continue
                        cols_list = list(cols[i].split(','))
                        train_cpy.loc[(train_cpy[category].isin(cols_list)), new_name] = vals[i]
                    #clear_output(wait=True)
                    print("Data distribution after conversion of the data:")
                    print_important_info_numeric(train_cpy, new_name, label)
                    while True:
                        repeat = input("Type \'keep\' if you want to keep the data like this, \'repeat\' if you want to repeat the process, or \'drop\' if you want to drop the feature after all:")
                        if repeat == "keep":
                            train_data[new_name] = 1
                            test_data[new_name] = 1
                            action_list.append("Conversion method : Manual")
                            action_list.append('\n')
                            to_be_filled = "New name : " + new_name
                            action_list.append(to_be_filled)
                            action_list.append('\n')
                            to_be_filled = "Number of values : " + str(len(cols)+1)
                            action_list.append(to_be_filled)
                            action_list.append('\n')
                            for j in range(len(cols)):
                                action_list.append(cols[j])
                                action_list.append(' : ')
                                action_list.append(vals[j])
                                action_list.append('\n')
                                cols_list = list(cols[j].split(','))
                                train_data.loc[(train_data[category].isin(cols_list)), new_name] = vals[j]
                                test_data.loc[(test_data[category].isin(cols_list)), new_name] = vals[j]
                            train_data.drop([category], axis = 1, inplace = True)
                            test_data.drop([category], axis = 1, inplace = True)
                            return train_data, test_data
                            #break
                        elif repeat == "repeat":
                            break
                        elif repeat == "drop":
                            action_list.append("Feature dropped during the conversion process, reason : ")
                            reason = input("Why are you dropping the feature?")
                            try:
                                action_list.append(reason)
                            except:
                                action_list.append("No reason given!")
                            train_data.drop([category], axis = 1, inplace = True)
                            test_data.drop([category], axis = 1, inplace = True)
                            return train_data, test_data
                            #break
                        else:
                            print("Action", repeat, "not recognized!")
                            continue
                break
            else:
                print("Option \"", action, "\" not reognized, try again!")





# Will have 3 modes : 
# "list", where it deals only with a given list of categories, or
# "auto", where it calls the function for all the object categories

def text_to_numeric(train_data, test_data, label, mode = "auto", categories = ["None"], logfile = "No file"):
    action_list = []
    if mode == "list":
        for category in categories:
            if category != "None":
                clear_output(wait = "True")
                print_important_info_object(train_data, test_data, category, label)
                while True:
                    action = input("1 - Convert to numeric\n2 - Drop the feature\n3 - Do nothing\n")
                    if action == "1":
                        action_list.append("Conversion process for the category : ")
                        action_list.append(str(category))
                        action_list.append("\n")
                        train_data, test_data = text_to_numeric_one_category(train_data, test_data, label, category, action_list)
                        break
                    elif action == "2":
                        confirm = input("Are you sure you want to drop the feature? \"yes\" - confirm, any other key to choose again?")
                        if confirm == 'yes':
                            action_list.append("Dropped the feature ")
                            action_list.append(str(category))
                            action_list.append(", reason: ")
                            reason = input("Why are you dropping the feature?")
                            try:
                                action_list.append(reason)
                            except:
                                action_list.append("No reason given!")
                            action_list.append('\n')
                            train_data.drop([category], axis = 1, inplace = True)
                            test_data.drop([category], axis = 1, inplace = True)
                            break
                        else:
                            continue
                    elif action == "3":
                        action_list.append(str(category))
                        action_list.append(" - No conversion done")
                        action_list.append("\n")
                        break
                    else:
                        print("Command \"", action, "\" not reognized, try again!")
                        continue
            else:
                print("List mode was chosen, but as an argument, an empty list was given!")
        #return train_data, test_data
    elif mode == "auto":
        categories = list(train_data.select_dtypes(include='object').columns)
        for category in categories:
            if category != "None":
                clear_output(wait = "True")
                print_important_info_object(train_data, test_data, category, label)
                while True:
                    action = input("1 - Convert to numeric\n2 - Drop the feature\n3 - Do nothing")
                    if action == "1":
                        action_list.append("Conversion process for the category : ")
                        action_list.append(str(category))
                        action_list.append("\n")
                        train_data, test_data = text_to_numeric_one_category(train_data, test_data, label, category, action_list)
                        break
                    elif action == "2":
                        confirm = input("Are you sure you want to drop the feature? \"yes\" - confirm, any other key to choose again?")
                        if confirm == 'yes':
                            action_list.append("Dropped the feature ")
                            action_list.append(str(category))
                            action_list.append(", reason: ")
                            reason = input("Why are you dropping the feature?")
                            try:
                                action_list.append(reason)
                            except:
                                action_list.append("No reason given!")
                            action_list.append('\n')
                            train_data.drop([category], axis = 1, inplace = True)
                            test_data.drop([category], axis = 1, inplace = True)
                            break
                        else:
                            continue
                    elif action == "3":
                        action_list.append(str(category))
                        action_list.append(" - No conversion done")
                        action_list.append("\n")
                        break
                    else:
                        print("Command \"", action, "\" not reognized, try again!")
                        continue
        #return train_data, test_data
    else:
        print("Mode \’", mode, "\’ not recognized, only \’auto\’ and \’list\’ are implemented!")
        #return train_data, test_data
    if logfile != "No file":  
        file = open(logfile, "w") 
        for action in action_list:
            file.write(str(action))
        file.close()
    return train_data, test_data



def print_important_info_numeric(data, category, label):
    sns.regplot(data[category], data[label])
    stp = stats.pearsonr(data[category], data[label])
    str_title = "r = " + "{0:.2f}".format(stp[0]) + "," "p = " + "{0:.2f}".format(stp[1])
    plt.title(str_title)
    plt.show()


def print_important_info_object(train_data, test_data, category, label):
    sns.boxplot(x=category, y=label, data=train_data)
    plt.show()    
    pivot = train_data.pivot_table(index=category, values=label, aggfunc=np.median)
    print(pivot.sort_values(label,axis=0,ascending=False))
    print("Values inside the training set for", category, "feature:")
    print(train_data[category].value_counts())
    print("Values inside the test set for", category, "feature:")
    print(test_data[category].value_counts())


# First - Taking care of the missing values + Binarizes the categorical
# For each of the missing categories, check the datatype and fill using the next idea :
from scipy import stats

def handle_missing_data(train_data, test_data, label, mode = "auto", categories = [], logfile = "No file"):
    action_list = []
    missing_all_data = categories
    if mode == "list":
        if not missing_all_data:
            print("List mode was selected, but an empty list was given as an argument!")
            return train_data, test_data
    elif mode == "auto":
        missing_train = train_data.isnull().sum()
        missing_test = test_data.isnull().sum()
        missing_train_cats = missing_train[missing_train>0].index.values
        missing_test_cats = missing_test[missing_test>0].index.values
        missing_all_data = list(set().union(missing_train_cats, missing_test_cats))
    else:
        print("Mode \’", mode, "\’ not recognized, only auto and list are implemented")
        return
    message = "1 - Fill with median()\n2 - Fill with most frequent value\n3 - Fill with custom value\n4 - Delete the rows (only in the training set, the test set need to be delt with in a different way)\n5 - Drop the feature\n6 - Keep the data as it is"
    train_data_cpy = train_data.copy()
    for cat in missing_all_data:
        clear_output(wait=True)
        action_list.append('\n')
        action_list.append('\n')
        action_list.append("Handle missing data for the category: ")
        action_list.append(cat)
        action_list.append('\n')
        print("\nCategory (",missing_all_data.index(cat)+1,"/",len(missing_all_data),"),",cat,", data type -", train_data[cat].dtypes)
        print("Number of missing training data values - ", train_data[cat].isnull().sum())
        print("Percentage of missing training data values - ", train_data[cat].isnull().sum()/train_data[cat].isnull().count()*100, "%")
        print("\nNumber of missing test data values - ", test_data[cat].isnull().sum())
        print("Percentage of missing test data values - ", test_data[cat].isnull().sum()/test_data[cat].isnull().count()*100, "%")
        print("\nData before the processing:")
        if(train_data[cat].dtypes != 'object'):
            print_important_info_numeric(train_data, cat, label)
        else:
            print_important_info_object(train_data, test_data, cat, label)
        while(True):
            print("\n\n",message)
            action = input("Choose the action:")
            if(action == '1'):
                train_data_cpy = train_data.copy()
                train_data_cpy[cat].fillna(train_data_cpy[cat].median(), inplace = True)

                print("Data distribution after filling with median():")
                print_important_info_numeric(train_data_cpy, cat, label)
                confirm = input("Are you satisfied with the action\'s effect on the data? \"yes\" - confirm, any other key to choose again?")
                if confirm == 'yes':
                    action_list.append("Filling missing data strategy : Median")
                    action_list.append('\n')
                    action_list.append("Median value  for the training set:")
                    action_list.append(str(train_data[cat].median()))
                    action_list.append('\n')
                    action_list.append("Median value  for the test set:")
                    action_list.append(str(test_data[cat].median()))
                    action_list.append('\n')
                    train_data[cat].fillna(train_data[cat].median(), inplace = True)
                    test_data[cat].fillna(test_data[cat].median(), inplace = True)
                    break   
                else:
                    continue
            elif(action == '2'):
                train_data_cpy = train_data.copy()
                test_data_cpy = test_data.copy()
                train_data_cpy[cat].fillna(train_data_cpy[cat].value_counts().index[0], inplace = True)
                test_data_cpy[cat].fillna(test_data_cpy[cat].value_counts().index[0], inplace = True)

                print("Data distribution after filling with most frequent:")
                print_important_info_object(train_data_cpy, test_data_cpy, cat, label)
                confirm = input("Are you satisfied with the action\'s effect on the data? \"yes\" - confirm, any other key to choose again?")
                if confirm == 'yes':
                    action_list.append("Filling missing data strategy : Most frequent")
                    action_list.append('\n')
                    action_list.append("Most frequent value for the training set:")
                    action_list.append(str(train_data[cat].value_counts().index[0]))
                    action_list.append('\n')
                    action_list.append("Most frequent value for the test set:")
                    action_list.append(str(test_data[cat].value_counts().index[0]))
                    action_list.append('\n')
                    train_data[cat].fillna(train_data[cat].value_counts().index[0], inplace = True)
                    test_data[cat].fillna(test_data[cat].value_counts().index[0], inplace = True)
                    labelnext = input("Do you want to perform the data to numeric conversion now? \’yes\’ to do it, any other key to continue")
                    if labelnext == "yes":
                        train_data, test_data = text_to_numeric_one_category(train_data, test_data, label, cat, action_list)
                    else:
                        action_list.append("No conversion chosen!")
                        action_list.append('\n')
                    break   
                else:
                    continue
            elif(action == '3'):
                typep = 0
                value = 0
                while True:
                    typep = input("Select the datatype that you want to fill the missing values with: (float, int, text)")
                    if typep == 'float':
                        while True:
                            try:
                                value = float(input("Type in the value:"))
                                break
                            except:
                                print("Invalid value, try again!")
                        break
                    elif typep == 'int':
                        while True:
                            try:
                                value = int(input("Type in the value:"))
                                break
                            except:
                                print("Invalid value, try again!")
                        break
                    elif typep == 'text':
                        while True:
                            try:
                                value = input("Type in the value:")
                                break
                            except:
                                print("Invalid value, try again!")
                        break
                    else:
                        print("Invalid data type, try again!")

                train_data_cpy = train_data.copy()
                test_data_cpy = test_data.copy()
                train_data_cpy[cat].fillna(value, inplace = True)
                test_data_cpy[cat].fillna(value, inplace = True)

                print("Data distribution after filling with custom value:")
                if(typep == 'text'):
                    print_important_info_object(train_data_cpy, test_data_cpy, cat, label)
                else:
                    print_important_info_numeric(train_data_cpy, cat, label)

                confirm = input("Are you satisfied with the action\'s effect on the data, \"yes\" - confirm, any other key to choose again?")
                if confirm == 'yes':
                    to_be_filled = "Filling missing data strategy -> Fill missing data with value: " + str(value)
                    action_list.append(to_be_filled)
                    action_list.append('\n')
                    train_data[cat].fillna(value, inplace = True)
                    test_data[cat].fillna(value, inplace = True)
                    if(typep == 'text'):
                        labelnext = input("Do you want to perform the data to numeric conversion now? \’yes\’ to do it, any other key to continue")
                        if labelnext == "yes":
                            train_data, test_data = text_to_numeric_one_category(train_data, test_data, label, cat, action_list)
                        else:
                            action_list.append("No conversion chosen!")
                            action_list.append('\n')
                    break   
                else:
                    continue
            elif(action == '4'):
                action_list.append("Filling missing data strategy : Remove the rows in the training set!")
                action_list.append('\n')
                train_data.dropna(subset = [cat], inplace = True)
                print("Rows with missing values for the", cat, "feature have been deleted! Please not that there still might be missing data in the training set, that will need to be handled differently")
                input("Press any key to continue")
                break
                
            elif(action == '5'):
                confirm = input("Are you sure you want to drop the feature? \"yes\" - confirm, any other key to choose again?")
                if confirm == 'yes':
                    action_list.append("Dropped the feature, reason : ")
                    reason = input("Why are you dropping the feature?")
                    try:
                        action_list.append(reason)
                    except:
                        action_list.append("No reason given!")
                    action_list.append('\n')
                    train_data.drop([cat], axis = 1, inplace = True)
                    test_data.drop([cat], axis = 1, inplace = True)
                    break   
                else:
                    continue
            elif(action == '6'):
                confirm = input("Are you sure you want to leave the data as it is? \"yes\" - confirm, any other key to choose again?")
                if confirm == 'yes':
                    action_list.append("No action taken!")
                    action_list.append('\n')
                    break   
                else:
                    continue
            else:
                print("Action \'", action, "\' not recognized, try again")

        action = input("Do you want to stop the process handling missing data? \'stop\' to stop, any other key to continue")
        if action != "stop":
            continue
        else:
            break
    if logfile != "No file":  
        file = open(logfile, "w") 
        for action in action_list:
            file.write(str(action))
        file.close()
    return train_data, test_data
                
