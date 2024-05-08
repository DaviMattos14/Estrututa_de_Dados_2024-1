#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura de um nó da árvore
typedef struct Node {
    int chave;
    struct Node* esq;
    struct Node* dir;
} Node;

// Função para criar um novo nó
Node* criar_Node(int chave) {
    Node* novo_Node = (Node*)malloc(sizeof(Node));
    novo_Node->chave = chave;
    novo_Node->esq = NULL;
    novo_Node->dir = NULL;
    return novo_Node;
}

// Função para inserir um novo nó na árvore
Node* inserir(Node* raiz, int chave) {
    if (raiz == NULL) {
        return criar_Node(chave);
    }

    if (chave < raiz->chave) {
        raiz->esq = inserir(raiz->esq, chave);
    } else if (chave > raiz->chave) {
        raiz->dir = inserir(raiz->dir, chave);
    }

    return raiz;
}

// Função auxiliar para encontrar o nó com a menor chave em uma árvore
Node* min_no(Node* node) {
    Node* current = node;

    while (current && current->esq != NULL) {
        current = current->esq;
    }

    return current;
}

// Função para remover um nó da árvore
Node* remove_Node(Node* raiz, int chave) {
    if (raiz == NULL) {
        return raiz;
    }

    if (chave < raiz->chave) {
        raiz->esq = remove_Node(raiz->esq, chave);
    } else if (chave > raiz->chave) {
        raiz->dir = remove_Node(raiz->dir, chave);
    } else {
        if (raiz->esq == NULL) {
            Node* temp = raiz->dir;
            free(raiz);
            return temp;
        } else if (raiz->dir == NULL) {
            Node* temp = raiz->esq;
            free(raiz);
            return temp;
        }

        Node* temp = min_no(raiz->dir);
        raiz->chave = temp->chave;
        raiz->dir = remove_Node(raiz->dir, temp->chave);
    }

    return raiz;
}

// Função para imprimir os nós da árvore em ordem
void inorderTraversal(Node* raiz) {
    if (raiz != NULL) {
        inorderTraversal(raiz->esq);
        printf("%d ", raiz->chave);
        inorderTraversal(raiz->dir);
    }
}

int main() {
    Node* raiz = NULL;
    char action[3];
    int chave;

    while (1) {
        if (fgets(action, sizeof(action), stdin) == NULL || action[0] == '\n') {
            break;
        }

        switch (action[0]) {
            case 'i':
                scanf("%d", &chave);
                raiz = inserir(raiz, chave);
                getchar(); // Consumir o caractere de nova linha deixado pelo Enter
                break;
            case 'r':
                scanf("%d", &chave);
                raiz = remove_Node(raiz, chave);
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

    // Liberar a memória alocada para a árvore
    // (não necessário para este exemplo simples,
    // mas importante em programas maiores)
    // Código para liberar memória:
    // void freeTree(Node* raiz) {
    //     if (raiz != NULL) {
    //         freeTree(raiz->esq);
    //         freeTree(raiz->dir);
    //         free(raiz);
    //     }
    // }
    // freeTree(raiz);

    return 0;
}
