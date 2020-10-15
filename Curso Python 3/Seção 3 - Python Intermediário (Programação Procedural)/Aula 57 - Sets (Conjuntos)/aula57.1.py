s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s3 = s1 | s2    # UNION (pipe) = Todos os elementos presentes em qualquer um dos sets
s4 = s1 & s2    # INTERSECTION (&) = Elementos presentes nos dois sets
s5 = s1 - s2    # DIFFERENCE (-) = Elementos apenas no set da esquerda
s6 = s1 ^ s2    # SYMETRIC_DIFFERENCE (^) = Contrário da intersection

print(s3)
print(s4)
print(s5)
print(s6)
