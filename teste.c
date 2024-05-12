#include <stdio.h>
const int MAX = 100;

int main(void)
{
    char expressao[MAX];

    scanf("%s", expressao);

    if (expressao[0] == "i")
    {
        printf("Insere\n");
    }
    else if (expressao[0] == "r")
    {
        printf("remove\n");
    }
    else if (expressao[0] == "p")
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