class Cleaner:
    def __init__(self):
        pass
        
        
    def clean_data(self, data):
        data.drop(['n_redirection','n_plus','n_hastag'], axis=1, inplace=True)
        return data