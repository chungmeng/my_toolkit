from collections import defaultdict
from copy import deepcopy
import pandas as pd
import numpy as np

def groupby_sample(df, col, size=10, replace=False):
    '''
    Sample evenly across Groups
    Args:
        df : Dataframe
        col : Groupby Column name
        size : Sample size pre Group
        replace : Replace after sample (default: False)
    Returns
        Sampled Dataframe
    '''   
    fn = lambda obj: obj.loc[np.random.choice(obj.index, size, replace),:]
    df = df.groupby(col, as_index=False).apply(fn)
    print('Resultant DF:\n', df[col].value_counts())
    return df

def groupby_items(df, group_by='', item_cols=[]):
    '''
    Return Items in Grouped By Column
    Args:
        df : Dataframe
        group_by : (str) Group By Column Name
        item_cols : (lis) List of Item Column Names
    Returns:
        Dictionary with Keys as Group By Values 
    '''
    return df.groupby(group_by)[item_cols].apply(lambda g: g.values.tolist()).to_dict()

def expand_row(df, expand_by='Img_No', uid='UniqueKey'):
    '''
    Expand Dataframe Rows based on List Values
    Args:
        df : Dataframe
        expand_by : Column containing a list for expansion
        uid : Original Unique Identifier
    Returns:
        Expanded Dataframe

    UniqueKey Img_No          =>         UniqueKey Row_ID
    --------- -----                      --------- -----
    'A'       [1, 2]                      'A'       'A_[1]'
    'B'       [1]                         'A'       'A_[2]'
    'C'       [1, 2, 3]                   'B'       'B_[1]'
                                          'C'       'C_[1]'
                                          'C'       'C_[2]'
                                          'C'       'C_[3]'
    '''  
    data=[]
    for row in df.to_dict(orient='records'):
        for n in row[expand_by]:
            dic=deepcopy(row)
            dic['Row_ID']=dic[uid]+'_[{}]'.format(n)
            dic[expand_by]=n
            data.append(dic)
    return pd.DataFrame(data)