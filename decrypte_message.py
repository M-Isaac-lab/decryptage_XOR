import os

def decrypt_xor(file_path, key_length=6, output_file="decrypted.txt"):
    """
    Déchiffre un fichier chiffré avec XOR en utilisant xortool.
    :param file_path: Chemin du fichier chiffré.
    :param key_length: Longueur de la clé (6 par défaut).
    :param output_file: Fichier de sortie pour le texte déchiffré.
    """
    # Utilisation de xortool pour analyser le fichier
    print("🔍 Analyse du fichier avec xortool...")
    os.system(f"xortool -l {key_length} -c 20 {file_path}")

    # Xortool génère des fichiers dans le répertoire 'xortool_out'
    # Le fichier le plus probable est 'xortool_out/0.out'
    probable_file = "./xortool_out/0.out"

    if os.path.exists(probable_file):
        print(f"Fichier déchiffré trouvé : {probable_file}")
        with open(probable_file, "rb") as f:
            decrypted_data = f.read()

        # Sauvegarde du résultat dans un fichier de sortie
        with open(output_file, "wb") as f:
            f.write(decrypted_data)
        print(f"Texte déchiffré sauvegardé dans : {output_file}")
    else:
        print("Aucun fichier déchiffré trouvé.")

