
carrinho = [("Produto 1", 30), ("Produto 2", 20), ("Produto 3", 50), ("Produto 3", 50), ("Produto 3", 50),
            ("Produto 3", 50), ("Produto 3", 50), ("Produto 3", 50), ("Produto 3", 50)]

print(sum([produto[1] for produto in carrinho]))
# Idênticos
print(sum([y for x, y in carrinho]))
