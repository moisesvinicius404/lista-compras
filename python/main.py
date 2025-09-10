import tkinter as tk
from tkinter import ttk, messagebox

lista_compras = []

class ListaComprasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Compras")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f0f0")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 11), padding=6)
        style.configure("Treeview", font=("Segoe UI", 11), rowheight=28)
        style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"))

        self.frame_top = ttk.Frame(self.root, padding=10)
        self.frame_top.pack(fill="x")

        ttk.Label(self.frame_top, text="Item:", font=("Segoe UI", 11)).grid(row=0, column=0, padx=5)
        self.nome_entry = ttk.Entry(self.frame_top, width=20)
        self.nome_entry.grid(row=0, column=1, padx=5)

        ttk.Label(self.frame_top, text="Quantidade:", font=("Segoe UI", 11)).grid(row=0, column=2, padx=5)
        self.quantidade_entry = ttk.Entry(self.frame_top, width=10)
        self.quantidade_entry.grid(row=0, column=3, padx=5)

        self.add_btn = ttk.Button(self.frame_top, text="Adicionar", command=self.adicionar_item)
        self.add_btn.grid(row=0, column=4, padx=5)

        self.tree = ttk.Treeview(self.root, columns=("Nome", "Quantidade", "Status"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Status", text="Status")
        self.tree.column("Nome", width=200)
        self.tree.column("Quantidade", width=100, anchor="center")
        self.tree.column("Status", width=100, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        style.configure("Danger.TButton", foreground="white", background="#d9534f")
        style.map("Danger.TButton", background=[("active", "#c9302c")])

        style.configure("Success.TButton", foreground="white", background="#5cb85c")
        style.map("Success.TButton", background=[("active", "#449d44")])

        self.frame_bottom = ttk.Frame(self.root, padding=10)
        self.frame_bottom.pack(fill="x")

        self.remove_btn = ttk.Button(self.frame_bottom, text="Remover", style="Danger.TButton", command=self.remover_item)
        self.remove_btn.pack(side="left", padx=5)

        self.marcar_btn = ttk.Button(self.frame_bottom, text="Marcar como Comprado", style="Success.TButton", command=self.marcar_comprado)
        self.marcar_btn.pack(side="left", padx=5)

        self.atualizar_lista()

    def adicionar_item(self):
        nome = self.nome_entry.get().capitalize()
        quantidade = self.quantidade_entry.get()
        if not nome or not quantidade.isdigit():
            messagebox.showwarning("Erro", "Preencha todos os campos corretamente!")
            return
        itens = {"nome": nome, "quantidade": int(quantidade), "status": "Pendente"}
        lista_compras.append(itens)
        self.atualizar_lista()
        self.nome_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)

    def remover_item(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para remover!")
            return
        indice = self.tree.index(selecionado)
        del lista_compras[indice]
        self.atualizar_lista()

    def marcar_comprado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para marcar!")
            return
        indice = self.tree.index(selecionado)
        lista_compras[indice]["status"] = "Comprado"
        self.atualizar_lista()

    def atualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for item in lista_compras:
            self.tree.insert("", "end", values=(item["nome"], item["quantidade"], item["status"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaComprasApp(root)
    root.mainloop()


