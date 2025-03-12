# This is a sample Python script.
from decrypte_message import decrypt_xor


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Utilisation
    # Exemple d'utilisation :
    #file_path = "C:\Users\G-STORES\PycharmProjects\python_projet\fichier_chiffre\GROUPES\Groupe1_L1\Groupe1_L1\FICHIERS CRYTES\PB.txt"  # Remplacez par le chemin de votre fichier chiffré
    file_path = './fichier_chiffre/GROUPES/Groupe1_L1/Groupe1_L1/FICHIERS CRYTES/PA.txt'  # Remplacez par le chemin de votre fichier chiffré
    decrypt_xor(file_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
