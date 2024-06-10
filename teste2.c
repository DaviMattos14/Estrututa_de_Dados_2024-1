#include <stdio.h>
#include <stdlib.h>

typedef enum { RED, BLACK } Color;

typedef struct Node {
    int data;
    Color color;
    struct Node *left, *right, *parent;
} Node;

typedef struct {
    Node *root;
} RedBlackTree;

Node* createNode(int data) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->color = RED;
    node->left = node->right = node->parent = NULL;
    return node;
}

void leftRotate(RedBlackTree *tree, Node *x) {
    Node *y = x->right;
    x->right = y->left;
    if (y->left != NULL) y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == NULL) tree->root = y;
    else if (x == x->parent->left) x->parent->left = y;
    else x->parent->right = y;
    y->left = x;
    x->parent = y;
}

void rightRotate(RedBlackTree *tree, Node *y) {
    Node *x = y->left;
    y->left = x->right;
    if (x->right != NULL) x->right->parent = y;
    x->parent = y->parent;
    if (y->parent == NULL) tree->root = x;
    else if (y == y->parent->left) y->parent->left = x;
    else y->parent->right = x;
    x->right = y;
    y->parent = x;
}

void fixInsert(RedBlackTree *tree, Node *z) {
    while (z->parent && z->parent->color == RED) {
        if (z->parent == z->parent->parent->left) {
            Node *y = z->parent->parent->right;
            if (y && y->color == RED) {
                z->parent->color = BLACK;
                y->color = BLACK;
                z->parent->parent->color = RED;
                z = z->parent->parent;
            } else {
                if (z == z->parent->right) {
                    z = z->parent;
                    leftRotate(tree, z);
                }
                z->parent->color = BLACK;
                z->parent->parent->color = RED;
                rightRotate(tree, z->parent->parent);
            }
        } else {
            Node *y = z->parent->parent->left;
            if (y && y->color == RED) {
                z->parent->color = BLACK;
                y->color = BLACK;
                z->parent->parent->color = RED;
                z = z->parent->parent;
            } else {
                if (z == z->parent->left) {
                    z = z->parent;
                    rightRotate(tree, z);
                }
                z->parent->color = BLACK;
                z->parent->parent->color = RED;
                leftRotate(tree, z->parent->parent);
            }
        }
    }
    tree->root->color = BLACK;
}

void insert(RedBlackTree *tree, int data) {
    Node *z = createNode(data);
    Node *y = NULL;
    Node *x = tree->root;

    while (x != NULL) {
        y = x;
        if (z->data < x->data) x = x->left;
        else x = x->right;
    }

    z->parent = y;
    if (y == NULL) tree->root = z;
    else if (z->data < y->data) y->left = z;
    else y->right = z;

    fixInsert(tree, z);
}

void printTree(Node *node) {
    if (node == NULL) return;
    printf("%d %c ", node->data, node->color == RED ? 'R' : 'B');
    printTree(node->left);
    printTree(node->right);
}

int main() {
    RedBlackTree tree = {NULL};
    char command[10];
    int data;

    while (1) {
        if (fgets(command, sizeof(command), stdin) == NULL || command[0] == '\n') break;
        if (command[0] == 'i') {
            sscanf(command + 2, "%d", &data);
            insert(&tree, data);
        } else if (command[0] == 'p') {
            printTree(tree.root);
            printf("\n");
        }
    }
    return 0;
}


// #include <stdio.h>

// int main(void)
// {
//     char expressao[3];
//     int chave;

//     while (1)
//     {
//         if (fgets(expressao, sizeof(expressao), stdin) == NULL || expressao[0] == '\n')
//         {
//             break;
//         }
//         scanf(" %d", &chave);
//         getchar();
//         printf(" \n %d ", expressao[0]);
//         printf("%d \n", chave);
//     }
    
//     return 0;
// }

