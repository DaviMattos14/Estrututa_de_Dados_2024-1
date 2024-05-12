#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
const int MAX = 100;

// Definição da estrutura de um nó da pilha
typedef struct no
{
    int chave;
    struct no *prox;
} no;

// Função para criar um novo nó
no *criar_no(int valor)
{
    no *novo_no = (no *)malloc(sizeof(no));
    novo_no->chave = valor;
    novo_no->prox = NULL;
    return novo_no;
}

// Função para verificar se a pilha está vazia
int isEmpty(no *topo)
{
    return (topo == NULL);
}

// Função para empilhar um elemento
void empilhar(no **topo, int valor)
{
    no *novo_no = criar_no(valor);
    novo_no->prox = *topo;
    *topo = novo_no;
}

// Função para desempilhar um elemento
void desempilhar(no **pilha)
{
    if (*pilha == NULL)
    {
        printf("pilha vazia\n");
    }
    else
    {
        no *topo = *pilha;
        *pilha = topo->prox;
    }
}

// Função para retornar o elemento do topoo da pilha sem removê-lo
int last(no *topo)
{
    if (isEmpty(topo))
    {
        return -1;
    }
    return topo->chave;
}

// Função para verificar se um caractere é um operador
int isOperator(char ch)
{
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/');
}

// Função para retornar a precedência do operador
int precedence(char op)
{
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return 0;
}

// Função para aplicar a operação
int operacao(int a, int b, int op)
{
    switch (op)
    {
    case 43:
        // printf("%d", a+b);
        return a + b;
    case 45:
        return a - b;
    case 42:
        return a * b;
    case 47:
        return a / b;
    }
    return 0;
}

// Função para calcular a expressão
void calcula(no **numeros, no **operadores)
{
    int num1 = last(*numeros);
    desempilhar(&*numeros);
    int op = last(*operadores);
    desempilhar(&*operadores);
    int num2 = last(*numeros);
    desempilhar(&*numeros);
    int resultado = operacao(num2, num1, op);
    empilhar(&*numeros, resultado);
}
int main()
{
    char expressao[MAX];

    scanf("%s", expressao);

    no *numPilha = NULL;
    no *opPilha = NULL;

    for (int i = 0; expressao[i] != 0; i++)
    {
        if (expressao[i] >= 48 && expressao[i] <= 57)
        {
            empilhar(&numPilha, (expressao[i] - '0'));
        }
        else if (expressao[i] == 40)
        {
            continue;
        }
        else if (expressao[i] == 41)
        {
            calcula(&numPilha, &opPilha);
        }
        else if (isOperator(expressao[i]))
        {
            int op = (int)expressao[i];
            empilhar(&opPilha, op);
        }
    }
    printf("%d\n", numPilha->chave);
    return 0;
}
