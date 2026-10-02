# AtividadeEstruturaAvancadas


Respostas obtidas nos testes: 
luizcm@:~/AtividadeEstruturaAvan-adas$ python testes.py
Quantidade de gavetas inicialmente 8
luizcm@:~/AtividadeEstruturaAvan-adas$ python testes.py
Quantidade de gavetas inicialmente:  8
[(0, 'a'), (8, 'b'), (16, 'c')]
buscar(8): b
luizcm@:~/AtividadeEstruturaAvan-adas$ python testes.py
Quantidade de gavetas inicialmente:  8
[(0, 'a'), (8, 'b'), (16, 'c')]
buscar(8): b
gavetas: 16
gaveta 0: [(0, 'a'), (16, 'c')]
gaveta 8: [(8, 'b')]
luizcm@:~/AtividadeEstruturaAvan-adas$ python testes.py
Quantidade de gavetas inicialmente:  8
[(0, 'a'), (8, 'b'), (16, 'c')]
buscar(8): b
gavetas: 16
[[(0, 'a'), (16, 'c')], [], [], [], [], [], [], [], [(8, 'b')], [], [], [], [], [], [], []]
gaveta 0: [(0, 'a'), (16, 'c')]
gaveta 8: [(8, 'b')]


luizcm@:~/AtividadeEstruturaAvan-adas$ python testes.py
1) gavetas no final: 512
2) maior gaveta: 1
3) maior gaveta sem crescer: 25




Como eu sei a 3 sem ter a parte prática?
Explicando sem código como dividir as chaves pelas gavetas.
Explicando sem código como dividir as chaves pelas gavetas.

Dá para calcular na cabeça, porque o resto reparte as chaves de forma regular.

Com 8 gavetas, a gaveta de cada chave é o resto da divisão por 8, e os restos possíveis são 0, 1, 2, ..., 7. Se as chaves são os números consecutivos 0, 1, 2, ..., 199, os restos se repetem em ciclos de 8:

0 1 2 3 4 5 6 7 | 0 1 2 3 4 5 6 7 | 0 1 2 3 ...

Cada ciclo completo coloca 1 chave em cada gaveta. Em 200 chaves cabem 200 ÷ 8 = 25 ciclos exatos, então cada gaveta recebe 25 chaves. Todas ficam do mesmo tamanho, e a maior tem 25.

Sem saber quais são as chaves, ainda dá para dizer algo:

    Mínimo possível: nunca será menor que 25. Se 200 chaves são distribuídas em 8 gavetas, alguma gaveta tem pelo menos 200 ÷ 8 = 25. Se todas tivessem 24 ou menos, o total daria no máximo 192, e faltariam chaves.
    Máximo possível: 200, se todas as chaves tiverem o mesmo resto (como os múltiplos de 8).
