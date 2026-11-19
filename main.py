
# MENTE ABERTA - Central de Apoio ao Cidadão

# ========== DADOS ==========
cidadaos = []
servicos = []
necessidades = []

# ========== ORIENTAÇÕES DO MENTE ABERTA ==========

orientacoes = [
    # SAÚDE
    [1, "Saúde", "Encontrar medicamentos gratuitos",
     "Remédio na Hora - e-saúdeSP",
     "Consulte a disponibilidade de medicamentos nas farmácias municipais de São Paulo.",
     "https://prefeitura.sp.gov.br/web/saude/w/atencao_basica/207663",
     "São Paulo - SP"],

    [2, "Saúde", "Consultar vacinas e histórico de saúde",
     "Meu SUS Digital",
     "Acesse informações de saúde disponíveis no sistema do SUS.",
     "https://meususdigital.saude.gov.br/",
     "Brasil"],

    [3, "Saúde", "Conseguir medicamentos pelo programa federal",
     "Farmácia Popular",
     "Consulte os medicamentos e insumos gratuitos e as regras do programa.",
     "https://www.gov.br/saude/pt-br/composicao/sectics/farmacia-popular",
     "Brasil"],

    # BENEFÍCIOS SOCIAIS
    [4, "Benefícios sociais", "Consultar Cadastro Único",
     "Aplicativo Cadastro Único",
     "Verifique informações cadastrais e encontre postos de atendimento.",
     "https://cadunico.dataprev.gov.br/",
     "Brasil"],

    [5, "Benefícios sociais", "Consultar benefícios do INSS",
     "Meu INSS",
     "Consulte benefícios, requerimentos e serviços previdenciários.",
     "https://meu.inss.gov.br/",
     "Brasil"],

    [6, "Benefícios sociais", "Consultar informações do Bolsa Família",
     "Bolsa Família",
     "Consulte orientações oficiais sobre o benefício e seus requisitos.",
     "https://www.gov.br/mds/pt-br/acoes-e-programas/bolsa-familia",
     "Brasil"],

    # EDUCAÇÃO
    [7, "Educação", "Fazer cursos gratuitos",
     "Escola Virtual de Governo",
     "Encontre cursos gratuitos de diversas áreas do conhecimento.",
     "https://www.escolavirtual.gov.br/",
     "Brasil"],

    [8, "Educação", "Buscar bolsas de faculdade",
     "Prouni",
     "Consulte informações sobre bolsas de estudo no ensino superior.",
     "https://acessounico.mec.gov.br/prouni",
     "Brasil"],

    [9, "Educação", "Ingressar em universidade pública",
     "Sisu",
     "Consulte informações sobre seleção para instituições públicas.",
     "https://acessounico.mec.gov.br/sisu",
     "Brasil"],

    # EMPREGO E RENDA
    [10, "Emprego e renda", "Encontrar vagas de emprego",
     "Portal Emprega Brasil",
     "Consulte oportunidades de emprego disponíveis no SINE.",
     "https://servicos.mte.gov.br/",
     "Brasil"],

    [11, "Emprego e renda", "Consultar carteira de trabalho",
     "Carteira de Trabalho Digital",
     "Acesse informações sobre seus vínculos de trabalho.",
     "https://www.gov.br/pt-br/apps/ctps-digital",
     "Brasil"],

    [12, "Emprego e renda", "Aprender tecnologia gratuitamente",
     "Escola do Trabalhador 4.0",
     "Encontre cursos gratuitos de tecnologia e produtividade.",
     "https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/qualificacao-profissional/caminho-digital/caminho-digital",
     "Brasil"],

    # DIREITOS E SERVIÇOS PÚBLICOS
    [13, "Direitos e serviços públicos", "Resolver problemas com empresas",
     "Consumidor.gov.br",
     "Registre reclamações contra empresas participantes da plataforma.",
     "https://www.consumidor.gov.br/",
     "Brasil"],

    [14, "Direitos e serviços públicos", "Conseguir assistência jurídica gratuita",
     "Defensoria Pública",
     "Consulte atendimento jurídico gratuito conforme os critérios locais.",
     "https://www.defensoria.sp.def.br/",
     "São Paulo - SP"],

    [15, "Direitos e serviços públicos", "Acessar serviços do governo",
     "Portal Gov.br",
     "Encontre serviços públicos digitais e informações oficiais.",
     "https://www.gov.br/",
     "Brasil"],

    # INCLUSÃO DIGITAL
    [16, "Inclusão digital", "Encontrar computadores e internet gratuitos",
     "Telecentros de São Paulo",
     "Consulte espaços públicos de acesso à internet e computadores.",
     "https://prefeitura.sp.gov.br/web/inovacao/w/telecentro",
     "São Paulo - SP"],

    [17, "Inclusão digital", "Aprender informática",
     "Escola do Trabalhador 4.0",
     "Encontre cursos gratuitos de habilidades digitais.",
     "https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/qualificacao-profissional/caminho-digital/caminho-digital",
     "Brasil"],

    [18, "Inclusão digital", "Aprender a utilizar serviços públicos digitais",
     "Portal Gov.br",
     "Acesse informações sobre contas e serviços digitais do governo.",
     "https://www.gov.br/",
     "Brasil"],

    [19, "Inclusão digital", "Encontrar informações e serviços para o dia a dia",
     "Mente Aberta - Plataforma Digital",
     "Plataforma que reúne orientações, oportunidades e informações sobre saúde, educação, emprego, benefícios sociais e serviços públicos.",
     "https://gabrielhenriquedantas.github.io/mente-aberta-citec/",
    "Brasil"]
]


# ========== MENU INICIAL ==========
def menu_inicial():
    print("\n========== MENTE ABERTA ==========")
    print("1 - Cadastrar-se")
    print("2 - Continuar como visitante")
    print("3 - Acesso administrativo")
    print("4 - Sair")
    print("==================================")

    return input("Escolha uma opção: ")

# ========== MENU DO CIDADÃO ==========
def menu_cidadao(cidadao=None):
    while True:
        print("\n========== MENTE ABERTA ==========")
        print("1 - LOGIN")
        print("2 - BUSCAR AJUDA E ORIENTAÇÃO")
        print("3 - CONSULTAR SERVIÇOS DISPONÍVEIS")
        print("4 - REGISTRAR UMA NECESSIDADE")
        print("5 - CONSULTAR MINHAS NECESSIDADES")
        print("6 - SAIR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                # Realiza o login e guarda o cidadão autenticado
                usuario_logado = login_cidadao(cidadaos)

                if usuario_logado is not None:
                    cidadao = usuario_logado

            case "2":
                # Busca orientações por categoria
                buscar_orientacao()

            case "3":
                # Pesquisa os serviços disponíveis
                consultar_servicos()

            case "4":
                # Verifica se o cidadão está identificado
                if cidadao is None:
                    tentativas = 0

                    while tentativas < 3:
                        cpf = input("Digite seu CPF: ").strip()
                        encontrado = False

                        # Procura o CPF na lista de cidadãos
                        for usuario in cidadaos:
                            if usuario[1] == cpf:
                                encontrado = True
                                break

                        if encontrado:
                            print("CPF encontrado! Faça login.")
                            cidadao = login_cidadao(cidadaos)
                            break

                        print("CPF não cadastrado!")
                        resposta = input("Deseja se cadastrar? (s/n): ").strip().lower()

                        if resposta in ("s", "sim"):
                            cidadao = cadastrar_cidadao(cidadaos)
                            break

                        tentativas += 1
                        print(f"Tentativas restantes: {3 - tentativas}")

                # Registra a necessidade do cidadão identificado
                if cidadao is not None:
                    registrar_necessidade(cidadao)

            case "5":
                # Solicita login caso o cidadão seja visitante
                if cidadao is None:
                    print("Você precisa fazer login para consultar suas necessidades.")
                    cidadao = login_cidadao(cidadaos)

                # Exibe apenas as necessidades do cidadão
                if cidadao is not None:
                    consultar_necessidades(cidadao)

            case "6":
                # Encerra o menu do cidadão
                break

            case _:
                print("Opção inválida!")


# ========== CADASTRO E LOGIN ==========

def cadastrar_cidadao(cidadaos):

    # Solicita e valida o nome do cidadão
    while True:
        print("========== CADASTRO ==========")
        nome = input("Digite o seu nome: ").strip()

        if nome != "" and nome.replace(" ", "").isalpha():
            break
        else:
            print("Nome inválido! Digite apenas letras.")

    # Valida o CPF e impede cadastros duplicados
    while True:
        cpf = input("Digite o seu CPF: ").strip()

        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido! Digite 11 números.")
            continue

        if any(usuario[1] == cpf for usuario in cidadaos):
            print("CPF já cadastrado!")
            continue

        break

    # Solicita e valida o e-mail
    while True:
        email = input("Digite o seu e-mail: ").strip()

        if "@" in email and "." in email.split("@")[-1]:
            break
        else:
            print("E-mail inválido!")

    # Solicita uma senha com no mínimo 8 caracteres
    while True:
        senha = input("Crie sua senha (mínimo de 8 caracteres): ")

        if len(senha) >= 8:
            break
        else:
            print("Senha inválida! Digite no mínimo 8 caracteres.")

    # Armazena os dados do cidadão na lista
    novo_cidadao = [nome, cpf, email, senha]
    cidadaos.append(novo_cidadao)

    print(f"Cadastro realizado com sucesso! Bem-vindo(a), {nome}!")

    # Retorna o cidadão cadastrado para o sistema
    return novo_cidadao

def login_cidadao(cidadaos):
    # Define o limite de três tentativas de login
    tentativas = 0

    while tentativas < 3:
        cpf = input("Digite seu CPF: ").strip()
        senha = input("Digite sua senha: ")

        # Verifica se o CPF e a senha correspondem a um cadastro
        for cidadao in cidadaos:
            if cidadao[1] == cpf and cidadao[3] == senha:
                print(f"Olá {cidadao[0]}, seu login foi realizado com sucesso!")
                return cidadao
        # Contabiliza tentativas incorretas
        tentativas += 1
        print(f"CPF ou senha incorretos! Tentativas restantes: {3 - tentativas}")
    # Encerra o login após três erros
    print("Limite de 3 tentativas atingido!")
    return None

#
# ========== FUNCIONALIDADES DO CIDADÃO ==========

def buscar_orientacao():
    # Exibe as categorias de ajuda disponíveis
    print("\n========== BUSCAR AJUDA E ORIENTAÇÃO ==========")
    print("1 - Saúde")
    print("2 - Benefícios sociais")
    print("3 - Educação")
    print("4 - Emprego e renda")
    print("5 - Direitos e serviços públicos")
    print("6 - Inclusão digital")
    print("7 - Voltar")
    print("================================================")

    opcao = input("Escolha a área em que precisa de ajuda: ")

    # Identifica a categoria selecionada pelo cidadão
    match opcao:
        case "1":
            categoria = "Saúde"
        case "2":
            categoria = "Benefícios sociais"
        case "3":
            categoria = "Educação"
        case "4":
            categoria = "Emprego e renda"
        case "5":
            categoria = "Direitos e serviços públicos"
        case "6":
            categoria = "Inclusão digital"
        case "7":
            return
        case _:
            print("Opção inválida!")
            return

    # Consulta as orientações da categoria escolhida
    consultar_orientacoes(categoria)


# ========== CONSULTAR ORIENTAÇÕES ==========

def consultar_orientacoes(categoria):
    encontrado = False

    # Percorre as orientações cadastradas
    for orientacao in orientacoes:
        if orientacao[1] == categoria:
            print(f"\nProblema: {orientacao[2]}")
            print(f"Solução: {orientacao[3]}")
            print(f"Descrição: {orientacao[4]}")
            print(f"Link: {orientacao[5]}")
            print(f"Região: {orientacao[6]}")
            print("-----------------------------------")

            encontrado = True

    # Informa quando não existem orientações na categoria
    if not encontrado:
        print("Nenhuma orientação encontrada nessa categoria.")


# ========== CONSULTAR SERVIÇOS ==========

def consultar_servicos():
    print("\n========== CONSULTAR SERVIÇOS ==========")

    # Solicita o nome do serviço e padroniza a pesquisa
    pesquisa = input("Digite o nome do serviço que procura: ").strip().lower()

    # Impede pesquisas vazias
    if pesquisa == "":
        print("Digite o nome de um serviço para pesquisar!")
        return

    encontrado = False

    # Pesquisa os serviços cadastrados na lista de orientações
    for orientacao in orientacoes:
        if pesquisa in orientacao[3].lower():
            print(f"\nServiço: {orientacao[3]}")
            print(f"Categoria: {orientacao[1]}")
            print(f"Descrição: {orientacao[4]}")
            print(f"Link: {orientacao[5]}")
            print(f"Região: {orientacao[6]}")
            print("-----------------------------------")

            encontrado = True

    # Informa quando nenhum serviço corresponde à pesquisa
    if not encontrado:
        print("Nenhum serviço encontrado com esse nome.")


# ========== REGISTRAR NECESSIDADE ==========

def registrar_necessidade(cidadao):

    # Impede o registro caso o cidadão não esteja logado
    if cidadao is None:
        print("Você precisa estar logado para registrar uma necessidade!")
        return

    print("\n========== REGISTRAR NECESSIDADE ==========")

    # Solicita as informações da necessidade
    categoria = input("Digite a categoria da necessidade: ").strip()
    descricao = input("Descreva sua necessidade: ").strip()

    # Verifica se os campos foram preenchidos
    if categoria == "" or descricao == "":
        print("Preencha todos os campos!")
        return

    # Gera um código para identificar a necessidade
    id_necessidade = len(necessidades) + 1

    # Armazena o código, CPF, categoria, descrição e status
    nova_necessidade = [
        id_necessidade,
        cidadao[1],
        categoria,
        descricao,
        "Pendente"
    ]

    # Adiciona a necessidade à lista
    necessidades.append(nova_necessidade)

    print("Necessidade registrada com sucesso!")


# ========== CONSULTAR MINHAS NECESSIDADES ==========

def consultar_necessidades(cidadao):

    print("\n========== MINHAS NECESSIDADES ==========")
    print(f"Cidadão: {cidadao[0]}")

    encontrado = False

    # Percorre as necessidades registradas
    for necessidade in necessidades:

        # Compara o CPF da necessidade com o cidadão logado
        if necessidade[1] == cidadao[1]:
            print(f"\nCódigo: {necessidade[0]}")
            print(f"Categoria: {necessidade[2]}")
            print(f"Descrição: {necessidade[3]}")
            print(f"Status: {necessidade[4]}")
            print("-----------------------------------")

            encontrado = True

    # Informa quando o cidadão não possui registros
    if not encontrado:
        print("Você ainda não possui necessidades registradas.")


# ========== MENU ADMINISTRATIVO ==========

def menu_administrador():
    # Mantém o menu aberto até o administrador escolher sair
    while True:
        print("\n========== ÁREA ADMINISTRATIVA ==========")
        print("1 - CONSULTAR CIDADÃOS CADASTRADOS")
        print("2 - CONSULTAR NECESSIDADES REGISTRADAS")
        print("3 - ATUALIZAR STATUS DE NECESSIDADES")
        print("4 - CADASTRAR ORIENTAÇÃO OU SERVIÇO")
        print("5 - EDITAR ORIENTAÇÃO OU SERVIÇO")
        print("6 - EXCLUIR ORIENTAÇÃO OU SERVIÇO")
        print("7 - SAIR")

        opcao = input("Escolha uma opção: ")

        # Executa a funcionalidade escolhida
        match opcao:
            case "1":
                consultar_cidadaos()
            case "2":
                consultar_necessidades_admin()
            case "3":
                atualizar_status()
            case "4":
                cadastrar_orientacao()
            case "5":
                editar_orientacao()
            case "6":
                excluir_orientacao()
            case "7":
                print("Saindo da área administrativa...")
                break
            case _:
                print("Opção inválida!")


# ========== LOGIN DO ADMINISTRADOR ==========

def login_administrador():
    # Define a senha administrativa e o limite de tentativas
    senha_admin = "Admin@2026"
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha do administrador: ")

        # Libera o acesso quando a senha está correta
        if senha == senha_admin:
            print("Acesso autorizado!")
            return True

        # Contabiliza as tentativas incorretas
        tentativas += 1
        print(f"Senha incorreta! Tentativas restantes: {3 - tentativas}")

    # Bloqueia o acesso após três tentativas
    print("Limite de tentativas atingido!")
    return False


# ========== CONSULTAR CIDADÃOS CADASTRADOS ==========

def consultar_cidadaos():
    print("\n========== CIDADÃOS CADASTRADOS ==========")

    # Verifica se existem cidadãos cadastrados
    if len(cidadaos) == 0:
        print("Nenhum cidadão cadastrado.")
        return

    # Exibe os dados dos cidadãos sem mostrar suas senhas
    for cidadao in cidadaos:
        print(f"\nNome: {cidadao[0]}")
        print(f"CPF: {cidadao[1]}")
        print(f"E-mail: {cidadao[2]}")
        print("-----------------------------------")


# ========== CONSULTAR NECESSIDADES REGISTRADAS ==========

def consultar_necessidades_admin():
    print("\n========== NECESSIDADES REGISTRADAS ==========")

    # Verifica se existem necessidades cadastradas
    if len(necessidades) == 0:
        print("Nenhuma necessidade registrada.")
        return

    # Percorre todas as necessidades registradas
    for necessidade in necessidades:
        nome = "Não encontrado"

        # Localiza o nome do cidadão por meio do CPF
        for cidadao in cidadaos:
            if cidadao[1] == necessidade[1]:
                nome = cidadao[0]
                break

        # Exibe as informações da necessidade
        print(f"\nCódigo: {necessidade[0]}")
        print(f"Cidadão: {nome}")
        print(f"Categoria: {necessidade[2]}")
        print(f"Descrição: {necessidade[3]}")
        print(f"Status: {necessidade[4]}")
        print("-----------------------------------")


# ========== ATUALIZAR STATUS DAS NECESSIDADES ==========

def atualizar_status():
    print("\n========== ATUALIZAR STATUS ==========")

    # Verifica se existem necessidades para atualizar
    if len(necessidades) == 0:
        print("Nenhuma necessidade registrada.")
        return

    # Exibe as necessidades para o administrador escolher
    consultar_necessidades_admin()

    codigo = input("Digite o código da necessidade: ").strip()

    # Procura a necessidade pelo código informado
    for necessidade in necessidades:
        if str(necessidade[0]) == codigo:
            print("\n1 - Pendente")
            print("2 - Em andamento")
            print("3 - Resolvida")

            opcao = input("Escolha o novo status: ")

            # Atualiza o status conforme a opção escolhida
            match opcao:
                case "1":
                    necessidade[4] = "Pendente"
                case "2":
                    necessidade[4] = "Em andamento"
                case "3":
                    necessidade[4] = "Resolvida"
                case _:
                    print("Opção inválida!")
                    return

            print("Status atualizado com sucesso!")
            return

    # Informa quando o código não corresponde a uma necessidade
    print("Necessidade não encontrada!")

    opcao = input("Escolha a categoria: ")

    # Define a categoria conforme a opção selecionada
    match opcao:
        case "1":
            categoria = "Saúde"
        case "2":
            categoria = "Benefícios sociais"
        case "3":
            categoria = "Educação"
        case "4":
            categoria = "Emprego e renda"
        case "5":
            categoria = "Direitos e serviços públicos"
        case "6":
            categoria = "Inclusão digital"
        case _:
            print("Categoria inválida!")
            return

    # Solicita os dados da nova orientação ou serviço
    problema = input("Qual problema esse serviço resolve? ").strip()
    solucao = input("Nome do serviço ou solução: ").strip()
    descricao = input("Descrição do serviço: ").strip()
    link = input("Link de acesso: ").strip()
    regiao = input("Região atendida: ").strip()

    # Verifica se todos os campos foram preenchidos
    if not all([problema, solucao, descricao, link, regiao]):
        print("Preencha todos os campos!")
        return

    # Gera um identificador único com base no maior ID existente
    novo_id = max([item[0] for item in orientacoes], default=0) + 1

    # Organiza as informações em uma lista
    nova_orientacao = [
        novo_id,
        categoria,
        problema,
        solucao,
        descricao,
        link,
        regiao
    ]

    # Adiciona a nova orientação à lista principal
    orientacoes.append(nova_orientacao)

    print("Orientação ou serviço cadastrado com sucesso!")

# ========== EDITAR ORIENTAÇÃO OU SERVIÇO ==========

def editar_orientacao():
    print("\n========== EDITAR ORIENTAÇÃO OU SERVIÇO ==========")

    # Verifica se existem orientações cadastradas
    if len(orientacoes) == 0:
        print("Nenhuma orientação cadastrada.")
        return

    # Exibe os códigos e nomes dos serviços disponíveis
    for orientacao in orientacoes:
        print(f"Código: {orientacao[0]} | Serviço: {orientacao[3]}")

    codigo = input("\nDigite o código do serviço que deseja editar: ").strip()

    # Procura o serviço pelo código informado
    for orientacao in orientacoes:
        if str(orientacao[0]) == codigo:
            print(f"\nServiço selecionado: {orientacao[3]}")

            # Permite editar vários campos até escolher voltar
            while True:
                print("\n1 - Editar categoria")
                print("2 - Editar problema")
                print("3 - Editar nome do serviço")
                print("4 - Editar descrição")
                print("5 - Editar link")
                print("6 - Editar região")
                print("7 - Voltar")

                opcao = input("Escolha o campo: ")

                if opcao == "7":
                    return

                # Impede a seleção de campos inexistentes
                if opcao not in ("1", "2", "3", "4", "5", "6"):
                    print("Opção inválida!")
                    continue

                # Trata separadamente a edição da categoria
                if opcao == "1":
                    print("\n1 - Saúde")
                    print("2 - Benefícios sociais")
                    print("3 - Educação")
                    print("4 - Emprego e renda")
                    print("5 - Direitos e serviços públicos")
                    print("6 - Inclusão digital")

                    categoria = input("Escolha a nova categoria: ")

                    # Lista de categorias permitidas
                    categorias = [
                        "Saúde",
                        "Benefícios sociais",
                        "Educação",
                        "Emprego e renda",
                        "Direitos e serviços públicos",
                        "Inclusão digital"
                    ]

                    if categoria not in ("1", "2", "3", "4", "5", "6"):
                        print("Categoria inválida!")
                        continue

                    # Atualiza a categoria na posição 1 da orientação
                    orientacao[1] = categorias[int(categoria) - 1]

                else:
                    # Solicita a nova informação do campo escolhido
                    novo_valor = input("Digite a nova informação: ").strip()

                    if novo_valor == "":
                        print("O campo não pode ficar vazio!")
                        continue

                    # Usa a opção escolhida como índice da lista
                    indice = int(opcao)
                    orientacao[indice] = novo_valor

                print("Informação atualizada com sucesso!")

            # O menu de edição é encerrado pela opção 7

    print("Serviço não encontrado!")


# ========== EXCLUIR ORIENTAÇÃO OU SERVIÇO ==========

def excluir_orientacao():
    print("\n========== EXCLUIR SERVIÇO ==========")

    # Exibe os serviços cadastrados e seus identificadores
    for orientacao in orientacoes:
        print(f"Código: {orientacao[0]} | Serviço: {orientacao[3]}")

    # Solicita o código do serviço que será excluído
    codigo = input("Digite o código do serviço: ").strip()

    # Procura o serviço correspondente ao código
    for orientacao in orientacoes:
        if str(orientacao[0]) == codigo:

            # Solicita confirmação antes de excluir
            confirmar = input("Deseja excluir? (s/n): ").strip().lower()

            if confirmar in ("s", "sim"):
                # Remove o serviço da lista de orientações
                orientacoes.remove(orientacao)
                print("Serviço excluído com sucesso!")
            else:
                print("Exclusão cancelada!")

            return

    # Informa quando o código não corresponde a nenhum serviço
    print("Serviço não encontrado!")





# ========== EXECUÇÃO PRINCIPAL ==========

# Mantém o sistema funcionando até o usuário escolher sair
while True:
    opcao = menu_inicial()

    match opcao:
        case "1":
            # Cadastra o cidadão e abre o menu já identificado
            usuario = cadastrar_cidadao(cidadaos)
            menu_cidadao(usuario)

        case "2":
            # Permite acessar o sistema como visitante
            menu_cidadao()

        case "3":
            # Verifica a senha antes de liberar a área administrativa
            if login_administrador():
                menu_administrador()

        case "4":
            # Encerra a execução do programa
            print("Encerrando o Mente Aberta...")
            break

        case _:
            # Trata opções não reconhecidas
            print("Opção inválida!")
