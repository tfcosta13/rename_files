import os
def rename_files ():
    #(1) Obter os nomes dos arquivos em uma pasta
    file_list = os.listdir(r"C:\Users\Avell 1513\Desktop\python\rename_files\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\Avell 1513\Desktop\python\rename_files\prank")

    #(2) Renomear cada arquivo
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None,  "1234567890"))
        os.rename(file_name, file_name.translate(None,  "1234567890"))
    os.chdir(saved_path)

rename_files()
