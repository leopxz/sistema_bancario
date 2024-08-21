# Sistema Bancário com Tkinter

Este é um aplicativo de sistema bancário simples construído com a biblioteca Tkinter do Python. Ele permite que os usuários realizem operações bancárias básicas como depósitos, saques, visualização de extratos, e gerenciamento de contas e usuários.

## Contexto
Este projeto é um exemplo de aplicação GUI (interface gráfica do usuário) para gerenciamento bancário utilizando Python e Tkinter. Ele inclui funcionalidades básicas de um banco, como:

Depositar: Adicionar dinheiro à conta.
Sacar: Retirar dinheiro da conta.
Extrato: Visualizar as transações realizadas.
Novo Usuário: Criar um novo usuário.
Nova Conta: Criar uma nova conta bancária para um usuário existente.
Listar Contas: Mostrar todas as contas cadastradas.
O sistema tem limitações, como um número máximo de saques e um limite de saldo para saques.

## Configuração
Para executar este aplicativo, você precisará ter o Python instalado no seu sistema. O Tkinter já está incluído na biblioteca padrão do Python, então você não precisa instalar pacotes adicionais.

Certifique-se de ter o Python instalado:

Você pode verificar isso executando python --version ou python3 --version no terminal.
Clone o repositório ou baixe o código:
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio

Execute o código:

No terminal, execute o script com:
python nome_do_seu_script.py

## Execução
Após iniciar o aplicativo, a janela principal será exibida com um menu de opções. Você pode interagir com o sistema clicando nos botões disponíveis:

Depositar: Permite que você adicione dinheiro à conta.
Sacar: Permite que você retire dinheiro da conta.
Extrato: Mostra o extrato das transações realizadas.
Novo Usuário: Cria um novo usuário para o banco.
Nova Conta: Cria uma nova conta bancária para um usuário existente.
Listar Contas: Lista todas as contas cadastradas.
Sair: Fecha o aplicativo.

Estrutura
O código está organizado da seguinte forma:

## BancoApp (Classe Principal):

Contém todos os métodos e funcionalidades principais do aplicativo.
Métodos:
__init__(self, root): Inicializa a interface e configura o menu principal.
create_main_menu(self): Cria o menu principal com botões de navegação.
clear_screen(self): Limpa a tela atual para exibir uma nova interface.
depositar(self): Permite depósitos na conta.
sacar(self): Permite saques da conta com validação de saldo e limite.
exibir_extrato(self): Exibe o extrato de transações e saldo atual.
criar_usuario(self): Cria um novo usuário com validação de CPF.
validar_cpf(self, cpf): Valida o formato e unicidade do CPF.
criar_conta(self): Cria uma nova conta para um usuário existente.
filtrar_usuario(self, cpf): Busca um usuário pelo CPF.
listar_contas(self): Lista todas as contas cadastradas.
Bloco principal (if __name__ == "__main__"):

Cria a instância do Tkinter e inicia o loop principal do aplicativo.
