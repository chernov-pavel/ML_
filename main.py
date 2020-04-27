import numpy as np
import pandas as pnd

def getPopularName(fullNameList):
    nameList = map(lambda o: o[o.index(',')+1:].replace('Mr.','').replace('Mrs.', '').replace('Miss.', '').strip(), fullNameList)
    index = pnd.Index(nameList).value_counts()
    print(index)
    
    


if __name__ == '__main__':
    data = pnd.read_csv('data\\titanic.csv', index_col='PassengerId')
    sexList = data['Sex']
    maleList = list(filter(lambda o: o == 'male', sexList))
    femaleList = list(filter(lambda o: o == 'female', sexList))
    print(len(maleList), len(femaleList))
    total_people = len(data.index)
    survived_count = len(list(filter(lambda o: o == 1, data['Survived'])))
    print(np.round(survived_count/total_people * 100, 2))
    one_class_passangers = len(list(filter(lambda o: o == 1, data['Pclass'])))
    print(np.round(one_class_passangers/total_people * 100, 2))
    print(np.round(data['Age'].mean(), 2))
    print(np.round(data['Age'].median(), 2))
    print(np.round(data['SibSp'].corr(data['Parch']), 2))
    name_sex_data = data[['Name', 'Sex']]
    name_sex_data_female = name_sex_data[name_sex_data['Sex']=='female']
    names = name_sex_data_female['Name']
    print(getPopularName(names))
