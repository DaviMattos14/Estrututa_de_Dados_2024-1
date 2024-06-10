#include <stdio.h>
#include <stdlib.h>

// Estrutura do Nó
typedef struct Node {
    int chave;
    struct Node *esq, *dir, *pai;
    int cor; // 0 para Negro, 1 para Rubro
} Node;

// Estrutura pra Árvore RN
typedef struct {
    Node *raiz;
} ArvoreRN;

// Função para criar um novo nó
Node* criarNo(int chave) {
    Node* novo_no = (Node*)malloc(sizeof(Node));
    novo_no->chave = chave;
    novo_no->esq = novo_no->dir = novo_no->pai = NULL;
    novo_no->cor = 1; // Inicializa como Rubro
    return novo_no;
}

//Função para rodar a árvore para esquerda
void leftRotate(ArvoreRN *arvore, Node *x) {
    Node *y = x->dir;
    x->dir = y->esq;
    if (y->esq != NULL) y->esq->pai = x;
    y->pai = x->pai;
    if (x->pai == NULL) arvore->raiz = y;
    else if (x == x->pai->esq) x->pai->esq = y;
    else x->pai->dir = y;
    y->esq = x;
    x->pai = y;
}

//Função para rodar a árvore para direita
void rightRotate(ArvoreRN *arvore, Node *y) {
    Node *x = y->esq;
    y->esq = x->dir;
    if (x->dir != NULL) x->dir->pai = y;
    x->pai = y->pai;
    if (y->pai == NULL) arvore->raiz = x;
    else if (y == y->pai->esq) y->pai->esq = x;
    else y->pai->dir = x;
    x->dir = y;
    y->pai = x;
}

// Função para balancear a Árvore RN
void balanceamento(ArvoreRN *arvore, Node *z) {
    while (z->pai && z->pai->cor == 1) {
        if (z->pai == z->pai->pai->esq) {
            Node *y = z->pai->pai->dir;
            if (y && y->cor == 1) {
                z->pai->cor = 0;
                y->cor = 0;
                z->pai->pai->cor = 1;
                z = z->pai->pai;
            } else {
                if (z == z->pai->dir) {
                    z = z->pai;
                    leftRotate(arvore, z);
                }
                z->pai->cor = 0;
                z->pai->pai->cor = 1;
                rightRotate(arvore, z->pai->pai);
            }
        } else {
            Node *y = z->pai->pai->esq;
            if (y && y->cor == 1) {
                z->pai->cor = 0;
                y->cor = 0;
                z->pai->pai->cor = 1;
                z = z->pai->pai;
            } else {
                if (z == z->pai->esq) {
                    z = z->pai;
                    rightRotate(arvore, z);
                }
                z->pai->cor = 0;
                z->pai->pai->cor = 1;
                leftRotate(arvore, z->pai->pai);
            }
        }
    }
    arvore->raiz->cor = 0;
}

// Função para inserir um novo nó na árvore
void insere(ArvoreRN *arvore, int chave) {
    Node *z = criarNo(chave);
    Node *y = NULL;
    Node *x = arvore->raiz;

    while (x != NULL) {
        y = x;
        if (z->chave < x->chave) x = x->esq;
        else x = x->dir;
    }

    z->pai = y;
    if (y == NULL) arvore->raiz = z;
    else if (z->chave < y->chave) y->esq = z;
    else y->dir = z;

    balanceamento(arvore, z);
}

// Função para imprimir a árvore em pré ordem com cores
void imprimir(Node* raiz) {
    if (raiz != NULL) {
        printf("%d%s ", raiz->chave, raiz->cor == 1 ? "R" : "N");
        imprimir(raiz->esq);
        imprimir(raiz->dir);
    }
}

int main() {
    ArvoreRN arvore = {NULL};
    char entrada[3];
    int chave;

    while (1)
    {
        if (fgets(entrada, sizeof(entrada), stdin) == NULL || entrada[0] == '\n')
        {
            break;
        }

        switch (entrada[0])
        {
        case 'i':
            scanf("%d", &chave);
            insere(&arvore, chave);
            getchar(); // Consumir o caractere de nova linha deixado pelo Enter
            break;
        case 'p':
            imprimir(arvore.raiz);
            printf("\n");
            break;
        default:
            break;
        }
    }

    return 0;
}