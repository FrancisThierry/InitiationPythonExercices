from classification_fraude import ClassificationFraude
import pandas as pd

data = 'data/fraude_file.xlsx'
classification_fraude = ClassificationFraude(data)
classification_fraude.preprocess_data()
classification_fraude.train_model()

classification_fraude.show_data_info()
# Example of how to use the predict method
# Example new data point with Montant and Nb_Transactions_24h
new_data = pd.DataFrame({
    'Montant': [1000],
    'Nb_Transactions_24h': [1]
})
predictions = classification_fraude.predict(new_data)

result = "Frauduleux" if predictions[0] == 1 else "Non Frauduleux"
print(f"Predictions for new data: {result}")
# This will output whether the new data point is classified as frauduleux or not