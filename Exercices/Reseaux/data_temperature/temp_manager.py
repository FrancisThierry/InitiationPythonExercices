class TempManager:
    def __init__(self, temperatures):
        self.__temperatures = temperatures
        
    def save_temperature(self, temperature):
        self.__temperatures.append(temperature)
        print(f"Température {temperature}°C enregistrée.")

   