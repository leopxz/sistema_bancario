import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import textwrap

class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bancário")

        self.LIMITE_SAQUES = 3
        self.AGENCIA = "0001"
        self.saldo = 0
        self.limite = 500
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
            if valor > 0:
                self.saldo += valor
                self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
                messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "O valor informado é inválido.")
        self.create_main_menu()

    def sacar(self):
        self.clear_screen()
        tk.Label(self.root, text="Sacar", font=("Arial", 16)).pack(pady=10)

        valor = simpledialog.askfloat("Sacar", "Informe o valor do saque:", minvalue=0.01)
        if valor is not None:
            excedeu_saldo = valor > self.saldo
            excedeu_limite = valor > self.limite
            excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

            if excedeu_saldo:
                messagebox.showerror("Erro", "Você não tem saldo suficiente.")
            elif excedeu_limite:
                messagebox.showerror("Erro", "O valor do saque excede o limite.")
            elif excedeu_saques:
                messagebox.showerror("Erro", "Número máximo de saques excedido.")
            elif valor > 0:
                self.saldo -= valor
                self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                self.numero_saques += 1
                messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "O valor informado é inválido.")
        self.create_main_menu()

    def exibir_extrato(self):
        self.clear_screen()
        tk.Label(self.root, text="Extrato", font=("Arial", 16)).pack(pady=10)

        if not self.extrato:
            extrato_display = "Não foram realizadas movimentações."
        else:
            extrato_display = self.extrato

        tk.Label(self.root, text=extrato_display, font=("Arial", 12), justify=tk.LEFT).pack(pady=10)
        tk.Label(self.root, text=f"Saldo:\t\tR$ {self.saldo:.2f}", font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=5)

    def criar_usuario(self):
        self.clear_screen()
        tk.Label(self.root, text="Novo Usuário", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Novo Usuário", "Informe o CPF (somente números):")
        if cpf and self.validar_cpf(cpf):
            nome = simpledialog.askstring("Novo Usuário", "Informe o nome completo:")
            data_nascimento = simpledialog.askstring("Novo Usuário", "Informe a data de nascimento (dd-mm-aaaa):")
            endereco = simpledialog.askstring("Novo Usuário", "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")

            self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
            messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
        self.create_main_menu()

    def validar_cpf(self, cpf):
        if not cpf.isdigit() or len(cpf) != 11:
            messagebox.showerror("Erro", "CPF inválido. Deve conter apenas números e ter 11 dígitos.")
            return False
        if any(usuario["cpf"] == cpf for usuario in self.usuarios):
            messagebox.showerror("Erro", "Já existe usuário com esse CPF.")
            return False
        return True

    def criar_conta(self):
        self.clear_screen()
        tk.Label(self.root, text="Nova Conta", font=("Arial", 16)).pack(pady=10)

        cpf = simpledialog.askstring("Nova Conta", "Informe o CPF do usuário:")
        if cpf:
            usuario = self.filtrar_usuario(cpf)
            if usuario:
                numero_conta = len(self.contas) + 1
                conta = {"agencia": self.AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
                self.contas.append(conta)
                messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
            else:
                messagebox.showerror("Erro", "Usuário não encontrado.")
        self.create_main_menu()

    def filtrar_usuario(self, cpf):
        return next((usuario for usuario in self.usuarios if usuario["cpf"] == cpf), None)

    def listar_contas(self):
        self.clear_screen()
        tk.Label(self.root, text="Listar Contas", font=("Arial", 16)).pack(pady=10)

        if not self.contas:
            tk.Label(self.root, text="Nenhuma conta cadastrada.", font=("Arial", 12)).pack(pady=10)
        else:
            for conta in self.contas:
                linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
                """
                tk.Label(self.root, text=textwrap.dedent(linha), font=("Arial", 12), justify=tk.LEFT).pack(pady=5)

        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
