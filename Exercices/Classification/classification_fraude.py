import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
class ClassificationFraude:
    def __init__(self, data):
        self.xlSource = data
        self.dataFrame = None
        self.model = LogisticRegression()
        self.X_train = None
        self.X_test = None  
        self.y_train = None
        self.y_test = None

    def preprocess_data(self):
        # Implement preprocessing steps here
        self.dataFrame = pd.read_excel(self.xlSource)
        self.dataFrame.dropna(inplace=True)
        
    def show_data_info(self):
        # Display basic information about the DataFrame
        print(self.dataFrame.info())
        print(self.dataFrame.describe())
        print(self.dataFrame.head(5))
        

    def train_model(self):
        # Implement model training here
        X = self.dataFrame[['Montant', 'Nb_Transactions_24h']]
        y = self.dataFrame['Frauduleux']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(self.X_train, self.y_train)
   

    def predict(self, new_data):
        # Implement prediction logic here
        return self.model.predict(new_data)