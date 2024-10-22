seq = '123456789011223344556677889900111222333444555666777888999000'
single = slice(0, 9)
triple = slice(30, 57)
cost = int(seq[single])*int(seq[triple])
print(cost)
