# MENTE ABERTA - Central de Apoio ao Cidadão

def menu_inicial():
    print("\n========== MENTE ABERTA ==========")
    print("1 - Login do cidadão")
    print("2 - Cadastrar cidadão")
    print("3 - Login do administrador")
    print("4 - Acessar como visitante")
    print("5 - Sair")
    print("==================================")
cidadao = []
servicos = [
    [1, "Saúde", "UBS", "Atendimento básico gratuito pelo SUS"],
    [2, "Benefícios sociais", "CRAS", "Orientação sobre assistência social e CadÚnico"],
    [3, "Educação", "Cursos gratuitos", "Informações sobre oportunidades de estudo"],
    [4, "Emprego", "SINE", "Apoio na busca por oportunidades de trabalho"],
    [5, "Direitos", "Defensoria Pública", "Orientação e assistência jurídica gratuita para quem atende aos critérios"]
]


def buscar_orientacao(servicos):

    print("\n========== BUSCAR ORIENTAÇÃO ==========")
    print("Em qual área você precisa de ajuda?")
    print("1 - Saúde")
    print("2 - Benefícios sociais")
    print("3 - Educação")
    print("4 - Emprego")
    print("5 - Direitos")
    print("6 - Voltar")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            categoria = "Saúde"
        case "2":
            categoria = "Benefícios sociais"
        case "3":
            categoria = "Educação"
        case "4":
            categoria = "Emprego"
        case "5":
            categoria = "Direitos"
        case "6":
            return
        case _:
            print("Opção inválida!")
            return

    encontrado = False
    for servico in servicos:
        if servico[1] == categoria:
            print(f"\nServiço: {servico[2]}")
            print(f"Orientação: {servico[3]}")
            encontrado = True
    if not encontrado:
        print("Nenhuma orientação disponível nessa categoria.")


def login_cidadao(cidadaos):

    print("\n========== LOGIN DO CIDADÃO ==========")

    cpf = input("Digite seu CPF: ").strip()
    senha = input("Digite sua senha: ")

    for cidadao in cidadaos:

        if cidadao[1] == cpf and cidadao[3] == senha:
            print(f"\nBem-vindo(a), {cidadao[0]}!")
            return cidadao

    print("CPF ou senha incorretos!")
    return None


def cadastrar_cidadao(cidadaos):

    # Validação do nome
    while True:
        nome = input("Digite seu nome completo: ").strip()
        if nome != "" and nome.replace(" ", "").isalpha():
            break
        else:
            print("Nome inválido! Digite apenas letras.")

    # Validação do CPF
    while True:
        cpf = input("Digite seu CPF (11 números): ").strip()
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido! Digite 11 números.")
            continue
        cpf_existente = False

        for cidadao in cidadaos:
            if cidadao[1] == cpf:
                cpf_existente = True
                break
        if cpf_existente:
            print("Este CPF já está cadastrado!")
        else:
            break

    # Validação do e-mail
    while True:
        email = input("Digite seu e-mail: ").strip()
        if "@" in email and "." in email.split("@")[-1]:
            break
        else:
            print("E-mail inválido!")

    # Validação da senha
    while True:
        senha = input("Crie uma senha (mínimo 8 caracteres): ")
        if len(senha) >= 8:
            break
        else:
            print("A senha deve ter pelo menos 8 caracteres.")

    # Armazenamento na lista
    novo_cidadao = [nome, cpf, email, senha]
    cidadaos.append(novo_cidadao)
    print(f"\nCadastro realizado com sucesso! Bem-vindo(a), {nome}!")
    print("Cadastro realizado com sucesso!")

def consultar_servicos(servicos):

    print("\n========== SERVIÇOS DISPONÍVEIS ==========")

    if len(servicos) == 0:
        print("Nenhum serviço disponível.")
        return
    for servico in servicos:
        print(f"\nCódigo: {servico[0]}")
        print(f"Categoria: {servico[1]}")
        print(f"Nome: {servico[2]}")
        print(f"Descrição: {servico[3]}")
        print("----------------------------------")


def menu_cidadao(cidadao=None):

    while True:
        print("\n========== MENTE ABERTA ==========")
        if cidadao is not None:
            print(f"Bem-vindo(a), {cidadao[0]}!")
        else:
            print("Bem-vindo(a), visitante!")
        print("1 - Buscar ajuda e orientação")
        print("2 - Consultar serviços disponíveis")
        print("3 - Registrar uma necessidade")
        print("4 - Consultar minhas necessidades")
        print("5 - Sair da conta")
        print("==================================")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print("Buscar ajuda e orientação")
            case "2":
                consultar_servicos(servicos)
            case "3":
                print("Registrar uma necessidade")
            case "4":
                print("Consultar minhas necessidades")
            case "5":
                print("Saindo da conta...")
                break
            case _:
                print("Opção inválida! Tente novamente.")


def menu_administrador():

    while True:
        print("\n========== ÁREA DO ADMINISTRADOR ==========")
        print("1 - Consultar serviços")
        print("2 - Cadastrar novo serviço")
        print("3 - Editar serviço")
        print("4 - Excluir serviço")
        print("5 - Sair da área administrativa")
        print("==========================================")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                consultar_servicos(servicos)
            case "2":
                print("Cadastrar novo serviço")
            case "3":
                print("Editar serviço")
            case "4":
                print("Excluir serviço")
            case "5":
                print("Saindo da área administrativa...")
                break
            case _:
                print("Opção inválida! Tente novamente.")


def cadastrar_servico(servicos):

    print("\n========== CADASTRAR SERVIÇO ==========")

    categorias = ["Saúde", "Benefícios sociais", "Educação", "Emprego", "Direitos"]

    for indice in range(len(categorias)):

        print(f"{indice + 1} - {categorias[indice]}")

    while True:
        opcao = input("Escolha a categoria: ")
        if opcao.isdigit() and 1 <= int(opcao) <= len(categorias):
            categoria = categorias[int(opcao) - 1]
            break
        else:
            print("Categoria inválida!")

    while True:
        nome = input("Nome do serviço: ").strip()

        if nome != "":
            break

        print("O nome não pode ficar vazio!")

    while True:
        descricao = input("Descrição e orientação do serviço: ").strip()

        if descricao != "":
            break

        print("A descrição não pode ficar vazia!")

    novo_id = 1

    for servico in servicos:
        if servico[0] >= novo_id:
            novo_id = servico[0] + 1

    novo_servico = [novo_id, categoria, nome, descricao]
    servicos.append(novo_servico)

    print(f"\nServiço '{nome}' cadastrado com sucesso!")


while True:
    menu_inicial()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            usuario_logado = login_cidadao(cidadao)
            if usuario_logado is not None:
                menu_cidadao(usuario_logado)
        case "2":
            cadastrar_cidadao(cidadao)
        case "3":
            print("Login do administrador")
        case "4":
            menu_cidadao()
        case "5":
            print("Encerrando o Mente Aberta...")
            break
        case _:
            print("Opção inválida! Tente novamente.")
