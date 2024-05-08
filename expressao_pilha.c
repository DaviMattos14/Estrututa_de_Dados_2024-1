#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Definição da estrutura de um nó da pilha
typedef struct no
{
    int data;
    struct no *prox;
} no;

// Função para criar um novo nó
no *criar_no(int data)
{
    no *novo_no = (no *)malloc(sizeof(no));
    novo_no->data = data;
    novo_no->prox = NULL;
    return novo_no;
}

// Função para verificar se a pilha está vazia
int isEmpty(no *top)
{
    return (top == NULL);
}

// Função para empilhar um elemento
void push(no **top, int data)
{
    no *novo_no = criar_no(data);
    novo_no->prox = *top;
    *top = novo_no;
}

// Função para desempilhar um elemento
int pop(no **top)
{
    if (isEmpty(*top))
    {
        exit(EXIT_FAILURE);
    }
    no *temp = *top;
    *top = (*top)->prox;
    int popped = temp->data;
    free(temp);
    return popped;
}

// Função para retornar o elemento do topo da pilha sem removê-lo
int peek(no *top)
{
    if (isEmpty(top))
    {
        exit(EXIT_FAILURE);
    }
    return top->data;
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
int applyOperation(int a, int b, char op)
{
    switch (op)
    {
    case '+':
        return a + b;
    case '-':
        return a - b;
    case '*':
        return a * b;
    case '/':
        return a / b;
    }
    return 0;
}

// Função para calcular o resultado da expressão
int evaluateExpression(const char *expression)
{
    no *numPilha = NULL; // Pilha para operandos
    no *opPilha = NULL;  // Pilha para operadores

    for (int i = 0; expression[i] != '\0'; i++)
    {
        if (expression[i] == '(')
        {
            continue; // Ignorar '('
        }
        else if (isdigit(expression[i]))
        {
            int num = 0;
            while (isdigit(expression[i]))
            {
                num = num * 10 + (expression[i] - '0');
                i++;
            }
            push(&numPilha, num);
            i--; // Ajustar o índice de volta para o último dígito
        }
        else if (isOperator(expression[i]))
        {
            while (!isEmpty(opPilha) && peek(opPilha) != '(' && precedence(peek(opPilha)) >= precedence(expression[i]))
            {
                int num2 = pop(&numPilha);
                int num1 = pop(&numPilha);
                char op = pop(&opPilha);
                int result = applyOperation(num1, num2, op);
                push(&numPilha, result);
            }
            push(&opPilha, expression[i]);
        }
        else if (expression[i] == ')')
        {
            while (!isEmpty(opPilha) && peek(opPilha) != '(')
            {
                int num2 = pop(&numPilha);
                int num1 = pop(&numPilha);
                char op = pop(&opPilha);
                int result = applyOperation(num1, num2, op);
                push(&numPilha, result);
            }
            if (!isEmpty(opPilha) && peek(opPilha) == '(')
                pop(&opPilha); // Remover '(' correspondente
        }
    }

    while (!isEmpty(opPilha))
    {
        int num2 = pop(&numPilha);
        int num1 = pop(&numPilha);
        char op = pop(&opPilha);
        int result = applyOperation(num1, num2, op);
        push(&numPilha, result);
    }

    return pop(&numPilha);
}

int main()
{
    char expression[100];
    scanf("%s", expression);

    int result = evaluateExpression(expression);
    printf("%d\n", result);

    return 0;
}
