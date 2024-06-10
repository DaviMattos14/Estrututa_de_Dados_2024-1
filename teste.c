#include <stdio.h>
#include<stdlib.h>
const int MAX = 100;

typedef struct no
{
    int chave;
    struct no *esq;
    struct no *dir;
}no;

no* criar_no(int chave){
    no* novo_no = (no *)malloc(sizeof(no));
    novo_no->chave= chave;
    novo_no->esq = NULL;
    novo_no->dir = NULL;
    return novo_no;
}

no *insere(no *raiz, int valor){
    if (raiz == NULL)
    {
        return criar_no(valor);
    }
    else if (valor < raiz->chave)
    {
        raiz->esq = insere(raiz->esq, valor);
    }
    else if (valor >= raiz->chave)
    {
        raiz->dir = insere(raiz->dir, valor);  
    }
    return raiz;    
}
void imprimir(no *raiz){
    if (raiz!=NULL)
    {
        imprimir(raiz->esq);
        printf("%d ", raiz->chave);
        imprimir(raiz->dir);
    }
}

int main(void)
{
    char expressao[MAX] = " ";
    int chave;
    no* raiz = NULL;

    scanf("%s", expressao);
    scanf(" %d", &chave);
    while (expressao[0])
    {
        /* code */
    }
    
    if ((expressao[0] == 'i'))
    {
        printf("Insere ");
        printf("%d\n", chave);
        raiz = insere(raiz,chave);
    }
    else if ((expressao[0] == 'r'))
    {
        printf("remove ");
        printf("%d\n", chave);
    }
    else if ((expressao[0] == 'p'))
    {
        printf("printar\n");
    }
    return 0;
}

/* code

    for(int i = 0; expressao[i]!=0;i++){
        if (expressao[i]>=48 && expressao[i]<=57){
            //printf("posicao %d: %c\n", i, expressao[i]);
            printf("agr em int: %d\n", (expressao[i] - '0'));
        }
        else if (expressao[i]==40)
        {
            continue;
        }
        else if (expressao[i]==41)
        {
            printf("DESEMPILHA\n");
        }
        else{
            int op = (int)expressao[i];
            printf("operador em ascii: %d\n", op);
        }
    }
*/