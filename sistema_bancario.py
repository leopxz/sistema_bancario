import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime


# Classes de Transações e Operações Bancárias

class Transacao:
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def registrar(self, conta):
        if self.valor > conta.saldo:
            raise ValueError("Saldo insuficiente")
        conta.saldo -= self.valor
        conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def exibir(self):
        extrato = ""
        for transacao in self.transacoes:
            tipo = "Depósito" if isinstance(transacao, Deposito) else "Saque"
            extrato += f"{transacao.data.strftime('%d/%m/%Y %H:%M:%S')} - {tipo}: R$ {transacao.valor:.2f}\n"
        return extrato


class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        saque = Saque(valor)
        saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

    def exibir_extrato(self):
        return self.historico.exibir() + f"Saldo atual: R$ {self.saldo:.2f}"


class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


# Classe principal do aplicativo bancário
class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bancário")

        self.LIMITE_SAQUES = 3
        self.usuarios = []
        self.contas = []

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Menu Principal", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Depositar", command=self.depositar).pack(pady=5)
        tk.Button(self.root, text="Sacar", command=self.sacar).pack(pady=5)
        tk.Button(self.root, text="Extrato", command=self.exibir_extrato).pack(pady=5)
        tk.Button(self.root, text="Novo Usuário", command=self.criar_usuario).pack(pady=5)
        tk.Button(self.root, text="Nova Conta", command=self.criar_conta).pack(pady=5)
        tk.Button(self.root, text="Listar Contas", command=self.listar_contas).pack(pady=5)
        tk.Button(self.root, text="Sair", command=self.root.quit).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def depositar(self):
        self.clear_screen()
        tk.Label(self.root, text="Depositar", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Depósito", "Informe o CPF do cliente:")
        valor = simpledialog.askfloat("Depositar", "Informe o valor do depósito:", minvalue=0.01)

        if cpf and valor:
            cliente = self.encontrar_cliente(cpf)
            if cliente and cliente.contas:
                conta = cliente.contas[0]  # Usando a primeira conta do cliente para o exemplo
                conta.depositar(valor)
                messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Cliente ou conta não encontrados.")

        self.create_main_menu()

    def sacar(self):
        self.clear_screen()
        tk.Label(self.root, text="Sacar", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Saque", "Informe o CPF do cliente:")
        valor = simpledialog.askfloat("Sacar", "Informe o valor do saque:", minvalue=0.01)

        if cpf and valor:
            cliente = self.encontrar_cliente(cpf)
            if cliente and cliente.contas:
                conta = cliente.contas[0]
                try:
                    conta.sacar(valor)
                    messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
                except ValueError as e:
                    messagebox.showerror("Erro", str(e))
            else:
                messagebox.showerror("Erro", "Cliente ou conta não encontrados.")

        self.create_main_menu()

    def exibir_extrato(self):
        self.clear_screen()
        tk.Label(self.root, text="Extrato", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Extrato", "Informe o CPF do cliente:")

        if cpf:
            cliente = self.encontrar_cliente(cpf)
            if cliente and cliente.contas:
                conta = cliente.contas[0]
                extrato_display = conta.exibir_extrato()
                tk.Label(self.root, text=extrato_display, font=("Arial", 12), justify=tk.LEFT).pack(pady=10)
            else:
                messagebox.showerror("Erro", "Cliente ou conta não encontrados.")

        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=5)

    def criar_usuario(self):
        self.clear_screen()
        tk.Label(self.root, text="Novo Usuário", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Novo Usuário", "Informe o CPF (somente números):")
        if cpf and cpf.isdigit() and len(cpf) == 11:
            nome = simpledialog.askstring("Novo Usuário", "Informe o nome completo:")
            endereco = simpledialog.askstring("Novo Usuário", "Informe o endereço:")

            cliente = Cliente(nome, cpf, endereco)
            self.usuarios.append(cliente)
            messagebox.showinfo("Resultado", "Usuário criado com sucesso.")
        else:
            messagebox.showerror("Erro", "CPF inválido. Deve conter apenas números e ter 11 dígitos.")
        self.create_main_menu()

    def criar_conta(self):
        self.clear_screen()
        tk.Label(self.root, text="Nova Conta", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Nova Conta", "Informe o CPF do usuário:")
        if cpf:
            cliente = self.encontrar_cliente(cpf)
            if cliente:
                numero_conta = len(self.contas) + 1
                conta = Conta(numero=numero_conta, agencia="0001", cliente=cliente)
                cliente.adicionar_conta(conta)
                self.contas.append(conta)
                messagebox.showinfo("Resultado", "Conta criada com sucesso.")
            else:
                messagebox.showerror("Erro", "Cliente não encontrado.")
        self.create_main_menu()

    def listar_contas(self):
        self.clear_screen()
        tk.Label(self.root, text="Listar Contas", font=("Arial", 16)).pack(pady=10)

        if not self.contas:
            tk.Label(self.root, text="Nenhuma conta cadastrada.", font=("Arial", 12)).pack(pady=10)
        else:
            for conta in self.contas:
                info = f"Agência: {conta.agencia}\nConta: {conta.numero}\nTitular: {conta.cliente.nome}\n"
                tk.Label(self.root, text=info, font=("Arial", 12), justify=tk.LEFT).pack(pady=5)

        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=5)

    def encontrar_cliente(self, cpf):
        for cliente in self.usuarios:
            if cliente.cpf == cpf:
                return cliente
        return None


# Inicializando a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
