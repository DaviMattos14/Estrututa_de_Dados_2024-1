#include <stdio.h>

int main(void)
{
    char expressao[3];
    int chave;

    while (1)
    {
        if (fgets(expressao, sizeof(expressao), stdin) == NULL || expressao[0] == '\n')
        {
            break;
        }
        scanf(" %d", &chave);
        getchar();
        printf(" \n %d ", expressao[0]);
        printf("%d \n", chave);
    }
    
    return 0;
}