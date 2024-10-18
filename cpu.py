import psutil

def analyze_cpu_frequency():
    cpu_freq = psutil.cpu_freq()

    current_freq = cpu_freq.current 
    max_freq = cpu_freq.max 

    print("==== CPU Frequency Analysis ====")
    print(f"Поточна частота: {current_freq} MHz")
    print(f"Вихідна (максимальна) частота: {max_freq} MHz")

    if current_freq < max_freq:
        print("\nВисновок: Поточна частота процесора нижче номінальної. Процесор, ймовірно, працює в економному режимі (idle або power-saving).")
    elif current_freq == max_freq:
        print("\nВисновок: Поточна частота відповідає номінальній. Процесор працює на максимальній продуктивності.")
    else:
        print("\nВисновок: Поточна частота перевищує номінальну, можливо, увімкнений режим Turbo Boost або інша технологія для підвищення продуктивності.")
    
    print("===============================")

analyze_cpu_frequency()
