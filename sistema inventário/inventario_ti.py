import sqlite3
import csv
from datetime import datetime

class InventarioTI:
    def __init__(self, db_name="inventario_ti.db"):
        self.db_name = db_name
        self.inicializar_banco()

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def inicializar_banco(self):
        """Cria a tabela de equipamentos se ela não existir."""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                numero_serie TEXT UNIQUE NOT NULL,
                status TEXT NOT NULL,
                localizacao TEXT,
                responsavel TEXT,
                data_cadastro TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def adicionar_equipamento(self, tipo, marca, modelo, numero_serie, status, localizacao, responsavel):
        """Cadastra um novo equipamento no sistema."""
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO equipamentos (tipo, marca, modelo, numero_serie, status, localizacao, responsavel, data_cadastro)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (tipo, marca, modelo, numero_serie, status, localizacao, responsavel, data_atual))
            conn.commit()
            print(f"\n[SUCESSO] Equipamento '{marca} {modelo}' cadastrado com sucesso!")
        except sqlite3.IntegrityError:
            print(f"\n[ERRO] Já existe um equipamento cadastrado com o Número de Série: {numero_serie}")
        finally:
            conn.close()

    def listar_equipamentos(self):
        """Retorna e exibe todos os equipamentos cadastrados."""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipamentos")
        equipamentos = cursor.fetchall()
        conn.close()
        return equipamentos

    def buscar_equipamento(self, termo_busca):
        """Busca equipamentos por número de série, tipo ou responsável."""
        conn = self.conectar()
        cursor = conn.cursor()
        query = """
            SELECT * FROM equipamentos 
            WHERE numero_serie LIKE ? OR tipo LIKE ? OR responsavel LIKE ?
        """
        busca = f"%{termo_busca}%"
        cursor.execute(query, (busca, busca, busca))
        resultados = cursor.fetchall()
        conn.close()
        return resultados

    def atualizar_equipamento(self, id_equipamento, novos_dados):
        """
        Atualiza as informações de um equipamento.
        novos_dados deve ser um dicionário com os campos a serem atualizados.
        """
        conn = self.conectar()
        cursor = conn.cursor()
        
        campos = []
        valores = []
        for chave, valor in novos_dados.items():
            if valor: # Apenas atualiza se o usuário digitou algo
                campos.append(f"{chave} = ?")
                valores.append(valor)
        
        if not campos:
            print("\n[AVISO] Nenhuma alteração foi feita.")
            conn.close()
            return

        valores.append(id_equipamento)
        query = f"UPDATE equipamentos SET {', '.join(campos)} WHERE id = ?"
        
        cursor.execute(query, tuple(valores))
        conn.commit()
        if cursor.rowcount > 0:
            print("\n[SUCESSO] Equipamento atualizado com sucesso!")
        else:
            print("\n[ERRO] Equipamento não encontrado.")
        conn.close()

    def excluir_equipamento(self, id_equipamento):
        """Remove um equipamento permanentemente do banco de dados."""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipamentos WHERE id = ?", (id_equipamento,))
        conn.commit()
        if cursor.rowcount > 0:
            print("\n[SUCESSO] Equipamento excluído com sucesso!")
        else:
            print("\n[ERRO] Equipamento não encontrado.")
        conn.close()

    def exportar_para_csv(self, nome_arquivo="inventario_ti.csv"):
        """Exporta todos os dados do banco para um arquivo CSV."""
        equipamentos = self.listar_equipamentos()
        if not equipamentos:
            print("\n[AVISO] Não há dados para exportar.")
            return

        colunas = ["ID", "Tipo", "Marca", "Modelo", "Nº Série", "Status", "Localização", "Responsável", "Data de Cadastro"]
        
        try:
            with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(colunas)
                writer.writerows(equipamentos)
            print(f"\n[SUCESSO] Inventário exportado com sucesso para '{nome_arquivo}'!")
        except Exception as e:
            print(f"\n[ERRO] Falha ao exportar arquivo: {e}")


# --- Interface de Linha de Comando (CLI) ---

def exibir_tabela(equipamentos):
    """Auxiliar para formatar a exibição dos dados no terminal."""
    if not equipamentos:
        print("\nNenhum equipamento encontrado.")
        return
    
    template = "{:<5} | {:<15} | {:<15} | {:<15} | {:<15} | {:<12} | {:<15} | {:<15}"
    print("-" * 120)
    print(template.format("ID", "Tipo", "Marca", "Modelo", "Nº Série", "Status", "Localização", "Responsável"))
    print("-" * 120)
    for eq in equipamentos:
        # eq[0]=ID, eq[1]=Tipo, eq[2]=Marca, eq[3]=Modelo, eq[4]=Nº Série, eq[5]=Status, eq[6]=Local, eq[7]=Responsável
        print(template.format(eq[0], eq[1][:15], eq[2][:15], eq[3][:15], eq[4][:15], eq[5][:12], str(eq[6])[:15], str(eq[7])[:15]))
    print("-" * 120)

def menu_principal():
    sistema = InventarioTI()
    
    while True:
        print("\n" + "="*45)
        print("  SISTEMA DE INVENTÁRIO DE EQUIPAMENTOS DE TI  ")
        print("="*45)
        print("1. Cadastrar Novo Equipamento")
        print("2. Listar Todos os Equipamentos")
        print("3. Buscar Equipamento (Nº Série, Tipo, Responsável)")
        print("4. Atualizar Equipamento")
        print("5. Excluir Equipamento")
        print("6. Exportar Inventário para CSV")
        print("7. Sair")
        print("="*45)
        
        opcao = input("Escolha uma opção (1-7): ").strip()
        
        if opcao == "1":
            print("\n--- CADASTRO DE EQUIPAMENTO ---")
            tipo = input("Tipo (ex: Notebook, Monitor, Switch): ").strip()
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            numero_serie = input("Número de Série (Único): ").strip()
            status = input("Status (Disponível, Em uso, Manutenção, Descartado): ").strip()
            localizacao = input("Localização/Setor: ").strip()
            responsavel = input("Responsável (Nome do funcionário ou TI): ").strip()
            
            if not (tipo and marca and modelo and numero_serie and status):
                print("\n[ERRO] Campos obrigatórios (Tipo, Marca, Modelo, Nº Série, Status) não podem ficar vazios.")
                continue
                
            sistema.adicionar_equipamento(tipo, marca, modelo, numero_serie, status, localizacao, responsavel)
            
        elif opcao == "2":
            print("\n--- TODOS OS EQUIPAMENTOS CADASTRADOS ---")
            equipamentos = sistema.listar_equipamentos()
            exibir_tabela(equipamentos)
            
        elif opcao == "3":
            print("\n--- BUSCA DE EQUIPAMENTOS ---")
            termo = input("Digite o termo de busca (Nº Série, Tipo ou Responsável): ").strip()
            if termo:
                resultados = sistema.buscar_equipamento(termo)
                exibir_tabela(resultados)
            else:
                print("[AVISO] Busca cancelada. Digite algo para pesquisar.")
                
        elif opcao == "4":
            print("\n--- ATUALIZAÇÃO DE EQUIPAMENTO ---")
            id_eq = input("Digite o ID do equipamento que deseja atualizar: ").strip()
            if not id_eq.isdigit():
                print("[ERRO] ID inválido.")
                continue
            
            print("\nDeixe em branco os campos que NÃO deseja alterar:")
            novos_dados = {
                "tipo": input("Novo Tipo: ").strip(),
                "marca": input("Nova Marca: ").strip(),
                "modelo": input("Novo Modelo: ").strip(),
                "numero_serie": input("Novo Número de Série: ").strip(),
                "status": input("Novo Status (Disponível, Em uso, Manutenção): ").strip(),
                "localizacao": input("Nova Localização: ").strip(),
                "responsavel": input("Novo Responsável: ").strip()
            }
            # Remove chaves vazias para não atualizar campos não informados
            novos_dados = {k: v for k, v in novos_dados.items() if v}
            
            sistema.atualizar_equipamento(int(id_eq), novos_dados)
            
        elif opcao == "5":
            print("\n--- EXCLUSÃO DE EQUIPAMENTO ---")
            id_eq = input("Digite o ID do equipamento que deseja EXCLUIR: ").strip()
            if not id_eq.isdigit():
                print("[ERRO] ID inválido.")
                continue
            
            confirmar = input(f"Tem certeza que deseja excluir o equipamento ID {id_eq}? (S/N): ").strip().upper()
            if confirmar == "S":
                sistema.excluir_equipamento(int(id_eq))
            else:
                print("\nExclusão cancelada.")
                
        elif opcao == "6":
            sistema.exportar_para_csv()
            
        elif opcao == "7":
            print("\nEncerrando o sistema de inventário. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()

