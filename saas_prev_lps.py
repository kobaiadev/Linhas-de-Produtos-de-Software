import json

# ==========================================
# 1. CORE ASSET (Componentes Obrigatórios)
# ==========================================

class CoreSecuritySystem:
    """Representa a base obrigatória da LPS (comum a todos os clientes)."""
    def __init__(self, cliente_nome: str):
        self.cliente_nome = cliente_nome
        print(f"\n--- Inicializando SaaS-Prev para: {self.cliente_nome} ---")

    def autenticar_usuario(self, usuario: str) -> bool:
        print(f"[CORE] Usuário '{usuario}' autenticado com sucesso via logs auditáveis.")
        return True

    def registrar_ocorrencia(self, descricao: str):
        print(f"[CORE] Ocorrência salva no banco central: '{descricao}'")


# ==========================================
# 2. VARIABILIDADES (Módulos Opcionais/Plugins)
# ==========================================

class ModuloCFTV:
    def processar(self):
        print("[VARIÁVEL - CFTV] Analisando streams de vídeo com IA (Detecção de manchas térmicas).")

class ModuloAuditoriaEstoque:
    def processar(self):
        print("[VARIÁVEL - ESTOQUE] Sincronizando coletores de dados e buscando divergências.")

class ModuloFraudePDV:
    def processar(self):
        print("[VARIÁVEL - PDV] Monitorando quebras de caixa e cupons cancelados em tempo real.")


# ==========================================
# 3. GERENCIADOR DE VARIABILIDADE (Engine da LPS)
# ==========================================

class ProductDerivator:
    """Mecanismo que lê o perfil/contrato do cliente e deriva o produto customizado."""
    def __init__(self, core: CoreSecuritySystem, features_contratadas: list):
        self.core = core
        self.features = features_contratadas
        self.modulos_ativos = {}
        self._instanciar_variabilidades()

    def _instanciar_variabilidades(self):
        # Mapeamento de Features da Árvore de Recursos para as Classes Python
        mapeamento = {
            "cftv_ia": ModuloCFTV,
            "auditoria_estoque": ModuloAuditoriaEstoque,
            "fraude_pdv": ModuloFraudePDV
        }
        
        for feature in self.features:
            if feature in mapeamento:
                self.modulos_ativos[feature] = mapeamento[feature]()
                print(f"[LPS Engine] Feature '{feature}' injetada com sucesso.")

    def executar_sistema(self):
        # Executa o Core
        self.core.autenticar_usuario("operador_seguranca")
        self.core.registrar_ocorrencia("Abertura de rotina de monitoramento.")
        
        # Executa as Variabilidades dinamicamente se estiverem ativas no contrato
        if self.modulos_ativos:
            print("\n[LPS Engine] Ativando recursos específicos contratados:")
            for nome_feature, instancia_modulo in self.modulos_ativos.items():
                instancia_modulo.processar()
        else:
            print("\n[LPS Engine] Nenhuma feature adicional contratada para este perfil.")


# ==========================================
# 4. SIMULAÇÃO DA ENGENHARIA DE APLICAÇÃO (Cenários)
# ==========================================
if __name__ == "__main__":
    
    # Exemplo 1: Derivação de Produto para um Supermercado (Foco em PDV e Estoque)
    contrato_supermercado = ["auditoria_estoque", "fraude_pdv"]
    
    core_loja_a = CoreSecuritySystem(cliente_nome="Supermercado ABC - Volta Redonda")
    app_supermercado = ProductDerivator(core_loja_a, contrato_supermercado)
    app_supermercado.executar_sistema()
    
    print("-" * 60)

    # Exemplo 2: Derivação de Produto para um Centro de Distribuição (Foco em CFTV com IA)
    contrato_cd = ["cftv_ia"]
    
    core_cd_b = CoreSecuritySystem(cliente_nome="Centro de Distribuição Logística")
    app_cd = ProductDerivator(core_cd_b, contrato_cd)
    app_cd.executar_sistema()
