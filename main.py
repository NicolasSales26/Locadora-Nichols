# LOCADORA NICHOLS - Versão Final Portfólio
# Desenvolvido por Nicolas - Engenharia de Software - Estácio

carros = {
    "1": {"nome": "Gol", "preco": 89, "disponivel": True},
    "2": {"nome": "Onix", "preco": 99, "disponivel": True},
    "3": {"nome": "HB20", "preco": 95, "disponivel": True}
}

reservas = []

print("=== LOCADORA NICHOLS - SISTEMA FINAL ===")

while True:
    print("\n--- CARROS ---")
    for k,v in carros.items():
        status = "DISPONIVEL" if v["disponivel"] else "ALUGADO"
        print(f"{k} - {v['nome']} - R$ {v['preco']}/dia [{status}]")

    print("\n4 - Ver relatório de reservas")
    print("0 - Sair e fechar caixa")

    opcao = input("\nEscolha: ")

    if opcao == "0":
        print("\n--- FECHAMENTO DO DIA ---")
        dia_total = sum(r["total"] for r in reservas)
        print(f"Total de reservas: {len(reservas)}")
        print(f"Faturamento total: R$ {dia_total}")
        print("Sistema encerrado!")
        break
