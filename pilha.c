#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
typedef struct no
{
    int chave;
    struct no *prox;
} no;

no *criar_no(int valor)
{
    no *novo_no = (no *)malloc(sizeof(no));
    novo_no->chave = valor;
    novo_no->prox = NULL;
    return novo_no;
}

void empilhar(no** topo, int valor)
{
    no *novo_no = criar_no(valor);
    novo_no->prox = *topo;
    *topo = novo_no;
}

void desempilhar(no** pilha){
    if (*pilha == NULL)
    {
        printf("pilha vazia");
    }
    else
    {
        no* topo= *pilha;
        *pilha = topo->prox;
    }
}

int last(no *topo)
{
    if (isEmpty(topo))
    {
        return -1;
    }
    return topo->chave;
}

int isEmpty(no *topo)
{
    return (topo == NULL);
}

void imprimir(no *pilha)
{
    while (pilha != NULL)
    {
        printf("%d ", pilha->chave);
        pilha = pilha->prox;
    }
    printf("\n");
}
/*
 */

int main(void)
{

    no* pilha = NULL;
    int valor = 0;

    while (valor >= 0)
    {
        scanf("%d", &valor);
        if (valor >= 0)
        {
            empilhar(&pilha, valor);
        }
    }
    printf("\n");
    printf("ultimo valor: %d\n", last(pilha));
    desempilhar(&pilha);
    imprimir(pilha);

    return 0;
}

/*
 */
