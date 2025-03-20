import os
os.system('cls')
print("\n")

import pandas as pd

def filter_prohibited_out_of_competition(data):
    """Atfiltrēt vielas, kas aizliegtas ārpus sacensībām."""
    filtered_data = data[data['Aizliegts ārpus sacensībām'] == 'Jā']
    return filtered_data

def filter_prohibited_in_competition(data):
    """Atfiltrēt vielas, kas aizliegtas sacensību laikā."""
    filtered_data = data[data['Aizliegts sacensību laikā'] == 'Jā']
    return filtered_data

def search_by_name(data, name):
    """Meklēt vielu pēc nosaukuma un parādīt tās īpašības."""
    results = data[data['medicine_name'].str.contains(name, case=False, na=False)]
    return results

def show_sports_with_prohibition(data, competition_type):
    """Parādīt sporta veidus, kuros ir aizliegumi noteiktā laikā."""
    if competition_type == "in":
        prohibited_sports = data[data['Aizliegts sacensību laikā'] == 'Jā']['Sporta veidi, kuros aizliegts sacensību laikā']
    elif competition_type == "out":
        prohibited_sports = data[data['Aizliegts ārpus sacensībām'] == 'Jā']['Sporta veidi, kuros aizliegts ārpus sacensībām']

    return prohibited_sports

def save_to_file(data, file_name):
    """Saglabāt rezultātus jaunā failā."""
    data.to_csv(file_name, index=False)
    print(f"Data has been saved to {file_name}")

def main():
    data = pd.read_csv("Antidopings.csv")

   

    while True:
        print("\nIzvēlaties opciju:")
        print("1.Vielas aizliegtas ārpus sacensībām")
        print("2.Vielas aizliegtas sacensību laikā")
        print("3.Meklēt vielu pēc nosaukuma")
        print("4.Sporta veidi, aizliegts sacensību laikā")
        print("5.Sporta veidi, aizliegts ārpus sacensībām")
        print("6.Izeja")

       
        choice = input("Izvēlaties opciju no 1-6: ")

        if choice == '1':
            filtered_data = filter_prohibited_out_of_competition(data)
            print(filtered_data)
            save_choice = input("Vai vēlaties saglabāt datus jaunā failā? (Y/N): ")
            if save_choice.lower() == 'y':
                save_to_file(filtered_data, "Antidopings.csv")

        elif choice == '2':
            filtered_data = filter_prohibited_in_competition(data)
            print(filtered_data)
            save_choice = input("Vai vēlaties saglabāt datus jaunā failā? (Jā/Nē): ")

            if save_choice.lower() == 'jā':
                save_to_file(filtered_data, "aizliegtas_sacensību_laikā.csv")

        elif choice == '3':
            name = input("Ievadiet vielas nosaukumu: ")
            results = search_by_name(data, name)
            print(results)

        elif choice == '4':
            sports = show_sports_with_prohibition(data, "in")
            print(sports)

        elif choice == '5':
            sports = show_sports_with_prohibition(data, "out")
            print(sports)

        elif choice == '6':
            print("Iznākšana no programmas.")
            break
        
        else:
            print("Nederīga izvēle. Lūdzu, izvēlieties no saraksta.")

   

if __name__ == "__main__":
    main()