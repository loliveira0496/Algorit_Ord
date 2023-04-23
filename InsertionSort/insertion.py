# Começamos pegando o tamanho da lista.
n = len(lista)
# Temos que iterar passando por cada um dos elementos, mas podemos ignorar o primeiro elementos, porque uma lista formada apenas pelo primeiro elemento já está ordenada, então podemos começar a partir do segundo elemento da lista aquele que esta no índice de nº 1.
for i in range(1, n):
    # Precisamos pegar aquele elemento que está na posição que eu estou olhando agora (posição i) para podermos comparar ele com os outros elementos que ja estão na lista menor que existe vou chamar esse elemento de chave.
    chave = lista[i]
    # Enquanto existir elementos a esquerda da nossa chave, ou seja do número que estamos analisando no momento, vamos querer ir comparando, aquilo a li é a parcela da lista que representa a nossa pequena lista que ja está ordenada e vamos crescendo, mas repara que tem uma dupla condição de parada, voltando ao quadro podemos ver que por exempo quando a gente quis colocar o 5 na posição ainda existia o 4 e o 2 ali a esquerda mas a gente pode parar, não precisou fazer mais comparações, então no momento que eu verificar que o número que está a esquerda da minha chave não é maior do que a chave eu posso parar porque como a sublista ja está ordenada quem tiver mais a esquerda vai ser menor necessariamente, então eu tenho uma dupla condição de parada e eu vou criar mais uma variável para podermos controlar ela eu vou criar a j que vai começar como i -1, enquanto o i começa no 1, no segundo elemento da lista o j começa no i - 1 o primeiro elemento da lista para representar então aquela parcela da lista que ja tá ordenada.
    j = i - 1
    # enquanto esse j for maior ou igual a zero e o elemento que estiver nessa posição j for maior que a nossa chave.
    while j >= 0 and lista[j] > chave:
        # eu vou avançar quem está na posição j, quem ta ali naquela sublista já ordenada de uma posição, eu vou avançando ele até que eu possa inserir o elemento que ta chegando
        lista[j+1] = lista[j]
        # Para que não fiquemos presos nesse loop pra sempre precisamos decrementar o j, ai vai verificar entao na primeira iteração o j já começa como 0 , ele faz essa verificação aqui se for o caso avança uma posição se não for não faz nada mas ai ele tem que decrementar o j o j vai para -1 então ele fala opa não posso repetir isso aqui de novo.
        j = j - 1
        # Então a gente vai ter encontrado a posição que ´podemos inserir a chave que vai ser a posição j + 1, temos que somar 1 porque sempre vamos estar subtraindo 1 ao final daquele loop ali, então você terminar na verdade uma posição antes de onde você deveria inserir ai vc avança uma e insere o número.
