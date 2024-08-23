import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import textwrap
from datetime import datetime

# Funções para operações bancárias

def registrar_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def sacar(*, saldo, valor, extrato, limite_saque, numero_saques, limite_saques):
    if valor > saldo:
        return saldo, extrato, numero_saques, "Saldo insuficiente."
    elif valor > limite_saque:
        return saldo, extrato, numero_saques, "O valor do saque excede o limite."
    elif numero_saques >= limite_saques:
        return saldo, extrato, numero_saques, "Número máximo de saques excedido."
    else:
        saldo -= valor
        extrato += f"{registrar_hora()} - Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques, "Saque realizado com sucesso."

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"{registrar_hora()} - Depósito:\tR$ {valor:.2f}\n"
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    historico = extrato if extrato else "Não foram realizadas movimentações."
    historico += f"{registrar_hora()} - Saldo:\t\tR$ {saldo:.2f}\n"
    return historico

def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        return usuarios, "Erro: CPF já cadastrado."
    else:
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        return usuarios, "Usuário criado com sucesso."

def criar_conta(contas, usuarios, cpf):
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        return contas, "Conta criada com sucesso."
    else:
        return contas, "Erro: Usuário não encontrado."

def listar_contas(contas):
    if not contas:
        return "Nenhuma conta cadastrada."
    else:
        lista = ""
        for conta in contas:
            lista += f"\nAgência: {conta['agencia']}\nC/C: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}\n"
        return lista

# Classe do Aplicativo Bancário

class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bancário")

        self.LIMITE_SAQUES = 3
        self.saldo = 0
        self.limite_saque = 500
        self.extrato = ""
        self.numero_saques = 0
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

        valor = simpledialog.askfloat("Depositar", "Informe o valor do depósito:", minvalue=0.01)
        if valor is not None:
            self.saldo, self.extrato = depositar(self.saldo, valor, self.extrato)
            messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
        self.create_main_menu()

    def sacar(self):
        self.clear_screen()
        tk.Label(self.root, text="Sacar", font=("Arial", 16)).pack(pady=10)

        valor = simpledialog.askfloat("Sacar", "Informe o valor do saque:", minvalue=0.01)
        if valor is not None:
            self.saldo, self.extrato, self.numero_saques, msg = sacar(
                saldo=self.saldo, valor=valor, extrato=self.extrato,
                limite_saque=self.limite_saque, numero_saques=self.numero_saques, limite_saques=self.LIMITE_SAQUES
            )
            messagebox.showinfo("Resultado", msg)
        self.create_main_menu()

    def exibir_extrato(self):
        self.clear_screen()
        tk.Label(self.root, text="Extrato", font=("Arial", 16)).pack(pady=10)

        extrato_display = exibir_extrato(self.saldo, extrato=self.extrato)
        tk.Label(self.root, text=extrato_display, font=("Arial", 12), justify=tk.LEFT).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=5)

    def criar_usuario(self):
        self.clear_screen()
        tk.Label(self.root, text="Novo Usuário", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Novo Usuário", "Informe o CPF (somente números):")
        if cpf and cpf.isdigit() and len(cpf) == 11:
            nome = simpledialog.askstring("Novo Usuário", "Informe o nome completo:")
            data_nascimento = simpledialog.askstring("Novo Usuário", "Informe a data de nascimento (dd-mm-aaaa):")
            endereco = simpledialog.askstring("Novo Usuário", "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")

            self.usuarios, msg = criar_usuario(self.usuarios, nome, data_nascimento, cpf, endereco)
            messagebox.showinfo("Resultado", msg)
        else:
            messagebox.showerror("Erro", "CPF inválido. Deve conter apenas números e ter 11 dígitos.")
        self.create_main_menu()

    def criar_conta(self):
        self.clear_screen()
        tk.Label(self.root, text="Nova Conta", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Nova Conta", "Informe o CPF do usuário:")
        if cpf:
            self.contas, msg = criar_conta(self.contas, self.usuarios, cpf)
            messagebox.showinfo("Resultado", msg)
        self.create_main_menu()

    def listar_contas(self):
        self.clear_screen()
        tk.Label(self.root, text="Listar Contas", font=("Arial", 16)).pack(pady=10)

        contas_display = listar_contas(self.contas)
        tk.Label(self.root, text=contas_display, font=("Arial", 12), justify=tk.LEFT).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
