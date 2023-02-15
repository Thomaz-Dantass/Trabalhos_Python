import tkinter as tk

class Calculadora:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")

        self.display = tk.Entry(self.janela, width=20, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        numeros = "789456123"
        self.botoes = []
        for i, numero in enumerate(numeros):
            linha = i // 3 + 1
            coluna = i % 3
            botao = tk.Button(self.janela, text=numero, width=5, height=2, font=("Arial", 16), command=lambda x=numero: self.clique(x))
            botao.grid(row=linha, column=coluna, padx=5, pady=5)
            self.botoes.append(botao)

        operacoes = "+-*/"
        for i, operacao in enumerate(operacoes):
            botao = tk.Button(self.janela, text=operacao, width=5, height=2, font=("Arial", 16), command=lambda x=operacao: self.clique(x))
            botao.grid(row=i+1, column=3, padx=5, pady=5)
            self.botoes.append(botao)

        igual = tk.Button(self.janela, text="=", width=5, height=2, font=("Arial", 16), command=self.igual)
        igual.grid(row=4, column=2, padx=5, pady=5)
        self.botoes.append(igual)

        limpar = tk.Button(self.janela, text="C", width=5, height=2, font=("Arial", 16), command=self.limpar)
        limpar.grid(row=4, column=1, padx=5, pady=5)
        self.botoes.append(limpar)

        ponto = tk.Button(self.janela, text=".", width=5, height=2, font=("Arial", 16), command=lambda x=".": self.clique(x))
        ponto.grid(row=4, column=0, padx=5, pady=5)
        self.botoes.append(ponto)

    def clique(self, valor):
        self.display.insert(tk.END, valor)

    def limpar(self):
        self.display.delete(0, tk.END)

    def igual(self):
        try:
            resultado = eval(self.display.get())
            self.limpar()
            self.display.insert(0, resultado)
        except Exception as e:
            print(e)

    def run(self):
        self.janela.mainloop()

calculadora = Calculadora()
calculadora.run()
