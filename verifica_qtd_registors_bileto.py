import os
import pandas as pd

def extrair_e_inserir_cpf(df):
    if df.shape[1] == 1:
        df_split = df[0].str.split("|", expand=True)
        df_split.insert(0, "CPF", df_split[0])
        df = df_split
    else:
        df.insert(0, "CPF", df[0])
    
    df["CPF"] = df["CPF"].astype(str).str.strip()
    return df

def verificar_cpf_registros(arquivo_excel, sheet_name=0):

    df = pd.read_excel(arquivo_excel, sheet_name=sheet_name, header=None)
    df = extrair_e_inserir_cpf(df)
    
    df = df[df["CPF"] != "00.000.000/0001-00"]
    
    contagem = df.groupby("CPF").size().reset_index(name="qtde")
    return contagem

def processar_arquivo(arquivo):
    print(f"\nProcessando arquivo: {os.path.basename(arquivo)}")
    try:
        contagem = verificar_cpf_registros(arquivo)
        cpfs_incompletos = contagem[contagem["qtde"] != 12]
        
        if cpfs_incompletos.empty:
            print("Sucesso: Todos os CPFs possuem 12 registros completos!")
        else:
            print("Atenção: Os seguintes CPFs não possuem 12 registros completos:")
            print(cpfs_incompletos)
    except Exception as e:
        print(f"Erro ao processar {os.path.basename(arquivo)}: {e}")

def main():
    caminho = r"xpto"
    
    if os.path.isdir(caminho):
        arquivos = [
            os.path.join(caminho, f)
            for f in os.listdir(caminho)
            if f.lower().endswith(('.xlsx', '.xls'))
        ]
        if not arquivos:
            print("Nenhum arquivo .xlsx ou .xls encontrado na pasta.")
        else:
            for arquivo in arquivos:
                processar_arquivo(arquivo)
    elif os.path.isfile(caminho):
        processar_arquivo(caminho)
    else:
        print(f"O caminho especificado não existe: {caminho}")

if __name__ == "__main__":
    main()
