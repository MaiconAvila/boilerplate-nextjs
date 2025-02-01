import os

def remove_zone_identifier_files(root_dir):
    # Percorre todas as pastas e arquivos na árvore de diretório
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(':Zone.Identifier'):
                # Monta o caminho completo do arquivo
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)  # Remove o arquivo
                    print(f"Removido: {file_path}")
                except OSError as e:
                    print(f"Erro ao remover {file_path}: {e}")

if __name__ == "__main__":
    # Define o diretório raiz do seu projeto
    project_dir = '.'  # Altere isso para o caminho do seu projeto
    remove_zone_identifier_files(project_dir)