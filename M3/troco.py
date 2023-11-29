def troco(pagar, dinheiro):
    if dinheiro <= 0 or dinheiro < pagar:
        print("Não tem dinheiro suficiente")
        return None
    dinheiro = dinheiro - pagar
    print(f"Pagou {pagar} e ficou com {dinheiro}")
    return dinheiro


carteira = 100
carteira = troco(50, carteira)

if carteira is None:
    print("Não tem dinheiro na carteira")
else:
    print(f"Tem na carteira {carteira}")
