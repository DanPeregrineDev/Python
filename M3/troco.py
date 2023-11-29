def troco(pagar, dinheiro):
    dinheiro = dinheiro - pagar
    print(f"Pagou {pagar} e ficou com {dinheiro}")


carteira = 100


troco(50, carteira)
print(f"Tem na carteira {carteira}")
