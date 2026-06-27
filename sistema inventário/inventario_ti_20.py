import sqlite3
import csv
from datetime import datetime

class InventarioTI:
    def __init__(self, db_name="inventario_ti.db"):
        self.db_name = db_name
        self.inicializar_banco()

    def conectar(self):
        conn = sqlite3.connect(self.db_name)
        # Habilita o suporte a chaves estrangeiras no SQLite
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def inicializar_banco(self):
        """Cria as tabelas de equipamentos e histórico se não existirem."""
        conn = self.conectar()
        cursor = conn.cursor()
        
        # Tabela de Equipamentos
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
        
        # Nova Tabela: Histórico de Movimentações
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico_movimentacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                equipamento_id INTEGER,
                status_anterior TEXT,
                status_novo TEXT,
                localizacao_anterior TEXT,
                localizacao_nova TEXT,
                responsavel_anterior TEXT,
                responsavel_novo TEXT,
                data_movimentacao TEXT NOT NULL,
                observacao TEXT,
                FOREIGN KEY (equipamento_id) REFERENCES equipamentos(id) ON DELETE CASCADE
            )
        """)
        
        conn.commit()
        conn.close()

    def adicionar_equipamento(self, tipo, marca, modelo, numero_serie, status, localizacao, responsavel):
        """Cadastra um novo equipamento e gera o histórico inicial."""
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            
            # 1. Insere o equipamento
            cursor.execute("""
                INSERT INTO equipamentos (tipo, marca, modelo, numero_serie, status, localizacao, responsavel, data_cadastro)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (tipo, marca, modelo, numero_serie, status, localizacao, responsavel, data_atual))
            
            equipamento_id = cursor.lastrowid
            
            # 2. Registra a movimentação inicial (Cadastro)
            cursor.execute("""
                INSERT INTO historico_movimentacao (
                    equipamento_id, status_anterior, status_novo, 
                    localizacao_anterior, localizacao_nova, 
                    responsavel_anterior, responsavel_novo, 
                    data_movimentacao, observacao
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (equipamento_id, "-", status, "-", localizacao, "-", responsavel, data_atual, "Cadastro Inicial"))
            
            conn.commit()
            print(f"\n[SUCESSO] Equipamento '{marca} {modelo}' cadastrado e registrado no histórico!")
        except sqlite3.IntegrityError:
            print(f"\n[ERRO] Já existe um equipamento cadastrado com o Número de Série: {numero_serie}")
        finally:
            conn.close()

    def listar_equipamentos(self):
        """Retorna todos os equipamentos cadastrados."""
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
        """Atualiza o equipamento e gera um registro de histórico se houver mudanças."""
        conn = self.conectar()
        cursor = conn.cursor()
        
        # 1. Busca o estado atual do equipamento antes de atualizar
        cursor.execute("SELECT status, localizacao, responsavel FROM equipamentos WHERE id = ?", (id_equipamento,))
        atual = cursor.fetchone()
        
        if not atual:
            print("\n[ERRO] Equipamento não encontrado.")
            conn.close()
            return
            
        old_status, old_local, old_resp = atual
        
        # 2. Prepara os novos dados
        campos = []
        valores = []
        for chave, valor in novos_dados.items():
            campos.append(f"{chave} = ?")
            valores.append(valor)
            
        if not campos:
            print("\n[AVISO] Nenhuma alteração foi feita.")
            conn.close()
            return

        valores.append(id_equipamento)
        query = f"UPDATE equipamentos SET {', '.join(campos)} WHERE id = ?"
        
        # 3. Executa a atualização do equipamento
        cursor.execute(query, tuple(valores))
        
        # 4. Verifica se houve mudança em campos rastreáveis para salvar no histórico
        new_status = novos_dados.get("status", old_status)
        new_local = novos_dados.get("localizacao", old_local)
        new_resp = novos_dados.get("responsavel", old_resp)
        
        if (new_status != old_status) or (new_local != old_local) or (new_resp != old_resp):
            data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO historico_movimentacao (
                    equipamento_id, status_anterior, status_novo, 
                    localizacao_anterior, localizacao_nova, 
                    responsavel_anterior, responsavel_novo, 
                    data_movimentacao, observacao
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (id_equipamento, old_status, new_status, old_local, new_local, old_resp, new_resp, data_atual, "Atualização/Movimentação"))
        
        conn.commit()
        print("\n[SUCESSO] Equipamento atualizado e histórico de movimentação registrado!")
        conn.close()

    def excluir_equipamento(self, id_equipamento):
        """Remove um equipamento (o histórico associado será removido via CASCADE)."""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipamentos WHERE id = ?", (id_equipamento,))
        conn.commit()
        if cursor.rowcount > 0:
            print("\n[SUCESSO] Equipamento e seu histórico foram excluídos com sucesso!")
        else:
            print("\n[ERRO] Equipamento não encontrado.")
        conn.close()

    def listar_historico(self, id_equipamento=None):
        """Retorna o histórico de movimentações (geral ou de um equipamento específico)."""
        conn = self.conectar()
        cursor = conn.cursor()
        
        if id_equipamento:
            query = """
                SELECT h.id, e.tipo || ' ' || e.marca || ' ' || e.modelo, 
                       h.status_anterior, h.status_novo, 
                       h.localizacao_anterior, h.localizacao_nova, 
                       h.responsavel_anterior, h.responsavel_novo, 
                       h.data_movimentacao, h.observacao
                FROM historico_movimentacao h
                JOIN equipamentos e ON h.equipamento_id = e.id
                WHERE h.equipamento_id = ?
                ORDER BY h.data_movimentacao DESC
            """
            cursor.execute(query, (id_equipamento,))
        else:
            query = """
                SELECT h.id, e.tipo || ' ' || e.marca || ' ' || e.modelo, 
                       h.status_anterior, h.status_novo, 
                       h.localizacao_anterior, h.localizacao_nova, 
                       h.responsavel_anterior, h.responsavel_novo, 
                       h.data_movimentacao, h.observacao
                FROM historico_movimentacao h
                JOIN equipamentos e ON h.equipamento_id = e.id
                ORDER BY h.data_movimentacao DESC
            """
            cursor.execute(query)
            
        historico = cursor.fetchall()
        conn.close()
        return historico

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
    """Formata a exibição dos equipamentos no terminal."""
    if not equipamentos:
        print("\nNenhum equipamento encontrado.")
        return
    
    template = "{:<5} | {:<15} | {:<15} | {:<15} | {:<15} | {:<12} | {:<15} | {:<15}"
    print("-" * 120)
    print(template.format("ID", "Tipo", "Marca", "Modelo", "Nº Série", "Status", "Localização", "Responsável"))
    print("-" * 120)
    for eq in equipamentos:
        print(template.format(eq[0], eq[1][:15], eq[2][:15], eq[3][:15], eq[4][:15], eq[5][:12], str(eq[6])[:15], str(eq[7])[:15]))
    print("-" * 120)

def exibir_tabela_historico(historico):
    """Formata a exibição do histórico de movimentações no terminal."""
    if not historico:
        print("\nNenhum histórico de movimentação registrado.")
        return
    
    template = "{:<5} | {:<20} | {:<22} | {:<22} | {:<22} | {:<19}"
    print("-" * 122)
    print(template.format("ID", "Equipamento", "Status (De -> Para)", "Local (De -> Para)", "Responsável (De -> Para)", "Data Mov."))
    print("-" * 122)
    for h in historico:
        # h[0]=ID, h[1]=Equipamento, h[2]=St_Ant, h[3]=St_Nov, h[4]=Loc_Ant, h[5]=Loc_Nov, h[6]=Resp_Ant, h[7]=Resp_Nov, h[8]=Data, h[9]=Obs
        status_transicao = f"{h[2]} -> {h[3]}"
        local_transicao = f"{h[4]} -> {h[5]}"
        resp_transicao = f"{h[6]} -> {h[7]}"
        print(template.format(h[0], h[1][:20], status_transicao[:22], local_transicao[:22], resp_transicao[:22], h[8]))
    print("-" * 122)

def menu_principal():
    sistema = InventarioTI()
    
    while True:
        print("\n" + "="*45)
        print("  SISTEMA DE INVENTÁRIO DE EQUIPAMENTOS DE TI  ")
        print("="*45)
        print("1. Cadastrar Novo Equipamento")
        print("2. Listar Todos os Equipamentos")
        print("3. Buscar Equipamento (Nº Série, Tipo, Responsável)")
        print("4. Atualizar Equipamento (Gera histórico)")
        print("5. Excluir Equipamento")
        print("6. Visualizar Histórico de Movimentações")
        print("7. Exportar Inventário para CSV")
        print("8. Sair")
        print("="*45)
        
        opcao = input("Escolha uma opção (1-8): ").strip()
        
        if opcao == "1":
            print("\n--- CADASTRO DE EQUIPAMENTO ---")
            tipo = input("Tipo (ex: Notebook, Monitor, Switch): ").strip()
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            numero_serie = input("Número de Série (Único): ").strip()
            status = input("Status (Disponível, Em uso, Manutenção): ").strip()
            localizacao = input("Localização/Setor: ").strip()
            responsavel = input("Responsável: ").strip()
            
            if not (tipo and marca and modelo and numero_serie and status):
                print("\n[ERRO] Campos obrigatórios não podem ficar vazios.")
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
                print("[AVISO] Busca cancelada.")
                
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
                "status": input("Novo Status: ").strip(),
                "localizacao": input("Nova Localização: ").strip(),
                "responsavel": input("Novo Responsável: ").strip()
            }
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
            print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---")
            print("1. Ver Histórico Geral")
            print("2. Filtrar por ID de Equipamento")
            sub_opcao = input("Escolha uma opção (1-2): ").strip()
            
            if sub_opcao == "1":
                historico = sistema.listar_historico()
                exibir_tabela_historico(historico)
            elif sub_opcao == "2":
                id_eq = input("Digite o ID do equipamento: ").strip()
                if id_eq.isdigit():
                    historico = sistema.listar_historico(int(id_eq))
                    exibir_tabela_historico(historico)
                else:
                    print("[ERRO] ID inválido.")
            else:
                print("[ERRO] Opção inválida.")

        elif opcao == "7":
            sistema.exportar_para_csv()
            
        elif opcao == "8":
            print("\nEncerrando o sistema de inventário. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()