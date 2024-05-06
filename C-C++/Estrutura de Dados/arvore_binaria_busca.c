#include <stdio.h>
#include <stdlib.h>

/*
    Definição da estrutura de um nó da árvore
*/
typedef struct No
{
    int chave;
    struct No *esq;
    struct No *dir;
} No;

// Função para criar um novo nó
No *createNo(int chave)
{
    No *newNo = (No *)malloc(sizeof(No));
    newNo->chave = chave;
    newNo->esq = NULL;
    newNo->dir = NULL;
    return newNo;
}

// Função para inserir um novo nó na árvore
No *insere(No *raiz, int chave)
{
    if (raiz == NULL)
    {
        return createNo(chave);
    }

    if (chave < raiz->chave)
    {
        raiz->esq = insere(raiz->esq, chave);
    }
    else if (chave > raiz->chave)
    {
        raiz->dir = insere(raiz->dir, chave);
    }

    return raiz;
}

// Função auxiliar para encontrar o nó com a menor chave em uma árvore
No *minValueNo(No *No)
{
    No *atual = No;

    while (atual && atual->esq != NULL)
    {
        atual = atual->esq;
    }

    return atual;
}

// Função para remover um nó da árvore
No *removeNo(No *raiz, int chave)
{
    if (raiz == NULL)
    {
        return raiz;
    }

    if (chave < raiz->chave)
    {
        raiz->esq = removeNo(raiz->esq, chave);
    }
    else if (chave > raiz->chave)
    {
        raiz->dir = removeNo(raiz->dir, chave);
    }
    else
    {
        if (raiz->esq == NULL)
        {
            No *temp = raiz->dir;
            free(raiz);
            return temp;
        }
        else if (raiz->dir == NULL)
        {
            No *temp = raiz->esq;
            free(raiz);
            return temp;
        }

        No *temp = minValueNo(raiz->dir);
        raiz->chave = temp->chave;
        raiz->dir = removeNo(raiz->dir, temp->chave);
    }

    return raiz;
}

// Função para imprimir os nós da árvore em ordem
void inorderTraversal(No *raiz)
{
    if (raiz != NULL)
    {
        inorderTraversal(raiz->esq);
        printf("%d ", raiz->chave);
        inorderTraversal(raiz->dir);
    }
}

int main()
{
    No *raiz = NULL;
    char action[3];
    int chave;

    while (1)
    {
        if (fgets(action, sizeof(action), stdin) == NULL || action[0] == '\n')
        {
            break;
        }

        switch (action[0])
        {
        case 'i':
            scanf("%d", &chave);
            raiz = insere(raiz, chave);
            getchar(); // Consumir o caractere de nova linha deixado pelo Enter
            break;
        case 'r':
            scanf("%d", &chave);
            raiz = removeNo(raiz, chave);
            getchar(); // Consumir o caractere de nova linha deixado pelo Enter
            break;
        case 'p':
            inorderTraversal(raiz);
            printf("\n");
            break;
        default:
            break;
        }
    }
    return 0;
}
