from tabela import Tabela

t = Tabela()

#print("Quantidade de gavetas inicialmente: ", len(t.gavetas))



#t.inserir(0, "a")
#t.inserir(8, "b")
#t.inserir(16, "c")
#print(t.gavetas[0])                            
#print("buscar(8):", t.buscar(8))
# As três chaves caem na mesma gaveta, pois elas têm o mesmo resto, que é o determinante para saber em qual gaveta cada chave está.


#t.crescer()
#print("gavetas:", len(t.gavetas))
#print(t.gavetas)          
#print("gaveta 0:", t.gavetas[0])               
#print("gaveta 8:", t.gavetas[8]) 
#Porque a gaveta é o resto da divisão pelo número de gavetas, e esse número mudou de 8 para 16.
#Com 8 gavetas: 8 % 8 = 0, porque 8 ÷ 8 é exato e não sobra nada. O 8 ficava na gaveta 0.
#Com 16 gavetas: 8 % 16 = 8, porque 8 é menor que 16, então a divisão dá 0 e sobram os 8 inteiros. O 8 vai para a gaveta 8.


chaves = range(200)          # 200 chaves: 0, 1, 2, ..., 199

# 1 e 2: tabela normal, que cresce sozinha
t = Tabela()
for c in chaves:
    t.inserir(c, c)

print("1) gavetas no final:", len(t.gavetas))
print("2) maior gaveta:", max(len(g) for g in t.gavetas))

# 3: as mesmas 200 chaves em 8 gavetas, sem nunca crescer
gavetas = [[] for _ in range(8)]
for c in chaves:
    gavetas[hash(c) % 8].append(c)

print("3) maior gaveta sem crescer:", max(len(g) for g in gavetas))