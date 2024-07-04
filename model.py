import pandas as pd
import numpy as np
import random
import string

class DecoderEncoderDatabases:
    """
    The main utility of this class is to create objects that encode sensible data from databases so we can use them with an enterprise LLM.
    Also, provide functionality to decode what we previously encode.
    Input:
        - dataframe: It should be cleaned so the class only replace with random values the columns with non-numerical information.
    """
    def __init__(self, dataframe:pd.DataFrame):
        self.encoded_dataframe, self.mappings = self.__replace_non_numerical_values(dataframe)


    def __generate_random_string(self, length=8):
        """Generate a random string of fixed length."""
        letters = string.ascii_letters
        return ''.join(random.choices(letters, k=length))

    def __replace_non_numerical_values(self, dataframe):
        """
        Map the original dataframe and replace its values for random ones
        """
        mappings = {}
        
        for column in dataframe.columns:
            if df[column].dtype != object:
                continue
            unique_values = dataframe[column].unique()
            
            random_strings = np.array([self.__generate_random_string() for _ in unique_values])
            
            mapping = dict(zip(unique_values, random_strings))
            mappings[column] = mapping
            
            dataframe[column] = dataframe[column].map(mapping)
            
        return dataframe, mappings


if __name__ == '__main__':
    data = {
    'user_id': ['123', '223', '149', '1038'],
    'name': ['Kevin', 'Lautaro', 'Matias', 'Cata'],
    'email': ['kevin1010@gmail.com', 'LautiXD@gmail.com', 'mborot@gmail.com', 'cmia@gmail.com'],
    'notes': [10, 5, 7, 2],
    'gender': ['male', 'male', 'male', 'female'],
    'fav_subject': ['math', 'math', 'history', 'biology']
    }
  
    df = pd.DataFrame(data)
    encoded_decoder_app = DecoderEncoderDatabases(dataframe = df)

    print(encoded_decoder_app.encoded_dataframe.head())
    print(encoded_decoder_app.mappings)


    
