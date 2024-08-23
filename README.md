# Sistema Bancário com Tkinter

Este é um aplicativo de sistema bancário simples construído com a biblioteca Tkinter do Python. Ele permite que os usuários realizem operações bancárias básicas como depósitos, saques, visualização de extratos, e gerenciamento de contas e usuários.

## Contexto
Este projeto é um exemplo de aplicação GUI (interface gráfica do usuário) para gerenciamento bancário utilizando Python e Tkinter. Ele inclui funcionalidades básicas de um banco, como:<br>

**Depositar:** Adicionar dinheiro à conta.<br>
**Sacar:** Retirar dinheiro da conta.<br>
**Extrato:** Visualizar as transações realizadas.<br>
**Novo Usuário:** Criar um novo usuário.<br>
**Nova Conta:** Criar uma nova conta bancária para um usuário existente.<br>
**Listar Contas:** Mostrar todas as contas cadastradas.<br>

Além dessas funcionalidades, o sistema agora também registra a data e hora de cada transação realizada, como saques, depósitos e visualização de extrato. O sistema possui limitações, como um número máximo de saques diários e um limite de valor para saques.<br>

## Configuração
Para executar este aplicativo, você precisará ter o Python instalado no seu sistema. O Tkinter já está incluído na biblioteca padrão do Python, então você não precisa instalar pacotes adicionais.

Certifique-se de ter o Python instalado:

Você pode verificar isso executando python --version ou python3 --version no terminal.
Clone o repositório ou baixe o código:

```
git clone https://github.com/leopxz/sistema_bancario.git
cd sistema_bancario
```

Execute o código:

No terminal, execute o script com:
```
python sistema_bancario.py
```
OU SE preferir clique com o botão direito do mouse no seu código e clique em: RUN PYTHON > RUN PYTHON FILE IN TERMINAL.

## Execução
Após iniciar o aplicativo, a janela principal será exibida com um menu de opções. Você pode interagir com o sistema clicando nos botões disponíveis:<br>

**Depositar:** Permite que você adicione dinheiro à conta.<br>
**Sacar:** Permite que você retire dinheiro da conta.<br>
**Extrato:** Mostra o extrato das transações realizadas.<br>
**Novo Usuário:** Cria um novo usuário para o banco.<br>
**Nova Conta:** Cria uma nova conta bancária para um usuário existente.<br>
**Listar Contas:** Lista todas as contas cadastradas.<br>
**Sair:** Fecha o aplicativo.<br>

## Estrutura
O código está organizado da seguinte forma:

 BancoApp (Classe Principal):
Contém todos os métodos e funcionalidades principais do aplicativo.<br>

**Métodos:**<br>
__init__(self, root): Inicializa a interface e configura o menu principal.<br>
create_main_menu(self): Cria o menu principal com botões de navegação.<br>
clear_screen(self): Limpa a tela atual para exibir uma nova interface.<br>
depositar(self): Permite depósitos na conta.<br>
sacar(self): Permite saques da conta com validação de saldo e limite.<br>
exibir_extrato(self): Exibe o extrato de transações e saldo atual.<br>
criar_usuario(self): Cria um novo usuário com validação de CPF.<br>
validar_cpf(self, cpf): Valida o formato e unicidade do CPF.<br>
criar_conta(self): Cria uma nova conta para um usuário existente.<br>
filtrar_usuario(self, cpf): Busca um usuário pelo CPF.<br>
listar_contas(self): Lista todas as contas cadastradas.<br>
Bloco principal (if __name__ == "__main__"): Cria a instância do Tkinter e inicia o loop principal do aplicativo.<br>

## Funções Auxiliares:<br>
registrar_hora(): Retorna a data e hora atuais no formato dd/mm/aaaa hh:mm:ss.<br>
sacar(*, saldo, valor, extrato, limite_saque, numero_saques, limite_saques): Função modular para sacar, com argumentos nomeados e validação de limites.<br>
depositar(saldo, valor, extrato): Função modular para depositar, com argumentos posicionais.<br>
exibir_extrato(saldo, *, extrato): Função modular para exibir o extrato, com argumentos mistos.<br>
criar_usuario(usuarios, nome, data_nascimento, cpf, endereco): Função modular para criar um novo usuário, verificando a unicidade do CPF.<br>
criar_conta(contas, usuarios, cpf): Função modular para criar uma nova conta bancária vinculada a um usuário existente.<br>
listar_contas(contas): Função modular para listar todas as contas cadastradas.<br>


## Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções neste projeto. Sugestões e pull requests são sempre bem-vindos.
