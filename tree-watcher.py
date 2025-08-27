import os

#Ściezka startowa
root_dir = r"D:\GG Draft\BigData"
# Plik wyjściowy
output_file = os.path.join(root_dir, "bigdata_structure.txt")

with open(output_file, "w", encoding="utf-8") as f:
    for foldername, subfolders, filenames in os.walk(root_dir):
        # Wypisz folder
        level = foldername.replace(root_dir,'').count(os.sep)
        indent = ' ' * 4 * level
        f.write(f"{indent}{os.path.basename(foldername)}/\n")

        #Wypisz pliki w folderze
        sub_indent = ' ' * 4 * (level + 1)
        for filename in filenames:
            f.write(f"{sub_indent}{filename}\n")

print(f"Struktura folderów zapisana do pliku: {output_file}")