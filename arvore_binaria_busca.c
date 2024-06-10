#include <stdio.h>
#include <stdlib.h>

/*
Estrutura de um nó da árvore
*/ 
typedef struct Node
{
    int chave;
    struct Node *esq;
    struct Node *dir;
} Node;

// Função para criar um novo nó
Node *criar_No(int chave)
{
    Node *novo_No = (Node *)malloc(sizeof(Node));
    novo_No->chave = chave;
    novo_No->esq = NULL;
    novo_No->dir = NULL;
    return novo_No;
}

// Função para inserir um novo nó na árvore
Node *inserir(Node *raiz, int chave)
{
    if (raiz == NULL)
    {
        return criar_No(chave);
    }

    if (chave < raiz->chave)
    {
        raiz->esq = inserir(raiz->esq, chave);
    }
    else if (chave > raiz->chave)
    {
        raiz->dir = inserir(raiz->dir, chave);
    }

    return raiz;
}

// Função auxiliar para encontrar o nó com a menor chave em uma árvore
Node *min_no(Node *node)
{
    Node *atual = node;

    while (atual && atual->esq != NULL)
    {
        atual = atual->esq;
    }

    return atual;
}

// Função para remover um nó da árvore
Node *remove_No(Node *raiz, int chave)
{
    if (raiz == NULL)
    {
        return raiz;
    }

    if (chave < raiz->chave)
    {
        raiz->esq = remove_No(raiz->esq, chave);
    }
    else if (chave > raiz->chave)
    {
        raiz->dir = remove_No(raiz->dir, chave);
    }
    else
    {
        if (raiz->esq == NULL)
        {
            Node *temp = raiz->dir;
            free(raiz);
            return temp;
        }
        else if (raiz->dir == NULL)
        {
            Node *temp = raiz->esq;
            free(raiz);
            return temp;
        }

        Node *temp = min_no(raiz->dir);
        raiz->chave = temp->chave;
        raiz->dir = remove_No(raiz->dir, temp->chave);
    }

    return raiz;
}

// Função para imprimir os nós da árvore em ordem
void print_emOrdem(Node *raiz)
{
    if (raiz != NULL)
    {
        printf("%d ", raiz->chave);
        print_emOrdem(raiz->esq);
        print_emOrdem(raiz->dir);
    }
}

int main()
{
    Node *raiz = NULL;
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
            raiz = inserir(raiz, chave);
            getchar(); // Consumir o caractere de nova linha deixado pelo Enter
            break;
        case 'r':
            scanf("%d", &chave);
            raiz = remove_No(raiz, chave);
            getchar(); // Consumir o caractere de nova linha deixado pelo Enter
            break;
        case 'p':
            print_emOrdem(raiz);
            printf("\n");
            break;
        default:
            break;
        }
    }

    return 0;
}
