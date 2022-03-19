import pandas as pd
import numpy as np

class DataPreprocessor:
    
    @classmethod    
    def emp_length_converter(cls, df, column):
        df[column] = df[column].str.replace('\+ years', '')
        df[column] = df[column].str.replace('< 1 year', str(0))
        df[column] = df[column].str.replace(' years', '')
        df[column] = df[column].str.replace(' year', '')
        df[column] = pd.to_numeric(df[column])
        df[column].fillna(value = 0, inplace = True)
        return df
    
    @classmethod
    def date_columns(cls, df, column):
        today_date = pd.to_datetime('2020-08-01')
        df[column] = pd.to_datetime(df[column], format = "%b-%y")
        df['mths_since_' + column] = round(pd.to_numeric((today_date - df[column]) / np.timedelta64(1, 'M')))
        df['mths_since_' + column] = df['mths_since_' + column].apply(lambda x: df['mths_since_' + column].max() if x < 0 else x)
        df.drop(columns = [column], inplace = True)        
        return df
    
    @classmethod
    def loan_term_converter(cls, df, column):
        df[column] = pd.to_numeric(df[column].str.replace(' months', ''))
        return df
    
    @classmethod
    def dummy_creation(cls, df, columns_list):
        df_dummies = []
        for col in columns_list:
            df_dummies.append(pd.get_dummies(df[col], prefix = col, prefix_sep = ':'))
        df_dummies = pd.concat(df_dummies, axis = 1)
        df = pd.concat([df, df_dummies], axis = 1)
        return df
    
    @classmethod
    def fillout_missing_categorical_features(cls, df):
        grade_list = ['grade:A', 'grade:B', 'grade:C', 'grade:D', 'grade:E', 'grade:F', 'grade:G']
        home_ownership_list = ['home_ownership:MORTGAGE', 'home_ownership:NONE', 'home_ownership:OTHER', 'home_ownership:OWN', 'home_ownership:RENT']
        verification_list = ['verification_status:Not Verified', 'verification_status:Source Verified', 'verification_status:Verified']
        purpose_list = ['purpose:car', 'purpose:credit_card', 'purpose:debt_consolidation', 'purpose:educational', 'purpose:home_improvement', 'purpose:house', 'purpose:major_purchase', 'purpose:medical', 'purpose:moving', 'purpose:other', 'purpose:renewable_energy', 'purpose:small_business', 'purpose:vacation', 'purpose:wedding']
        categorical_feature_list = grade_list + home_ownership_list + verification_list + purpose_list

        n = len(df)
        col_names = df.columns
        for feature_name in categorical_feature_list:
            if feature_name not in col_names:
                df[feature_name] = np.zeros(n)

        return df

    @classmethod
    def data_cleansing(cls, df):
        print('emp_length: ', df['emp_length'].values)
        df = cls.emp_length_converter(df, 'emp_length')
        df['emp_length'].unique()
        print('emp_length: ', df['emp_length'].values)


        df = cls.date_columns(df, 'earliest_cr_line')
        df = cls.date_columns(df, 'issue_d')
        df = cls.date_columns(df, 'last_pymnt_d')
        df = cls.date_columns(df, 'last_credit_pull_d')
        print(df['mths_since_earliest_cr_line'].describe()) # 값이 하나라서 std는 NaN임
        print(df['mths_since_issue_d'].describe())
        print(df['mths_since_last_pymnt_d'].describe())
        print(df['mths_since_last_credit_pull_d'].describe())        


        print('term: ', df['term'].values)
        df = cls.loan_term_converter(df, 'term')
        print('term: ', df['term'].values)


        df = cls.dummy_creation(df, ['grade', 'home_ownership', 'verification_status', 'purpose'])

        df = cls.fillout_missing_categorical_features(df)

        return df
    

