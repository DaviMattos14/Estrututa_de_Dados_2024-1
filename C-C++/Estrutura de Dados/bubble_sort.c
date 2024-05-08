#include <stdio.h>
#include <stdbool.h>
#define MAX = 100

void bubble_sort(int vetor[], int n)
{
    int i = 1;
    int j;
    bool trocou = true;

    while (trocou && i <= n)
    {
        trocou = false;
        for (j = 0; j < n - 1; j++)
        {
            if (vetor[j] > vetor[j + 1])
            {
                int temp = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = temp;
                trocou = true;
            }
        }
        i++;
    }
}

void imprimir_vetor(int vetor[], int tamanho)
{
    int i;
    for (i = 0; i < tamanho; i++)
    {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}

int main(void)
{
    int numeros[] = {14, 2, 55, 5, 1, 86, 45, 23, 12, 3, 7};
    int len = sizeof(numeros) / sizeof(numeros[0]);
    
    bubble_sort(numeros, len);
    printf("%d\n", len);
    imprimir_vetor(numeros, len);


    int num[] = {1,2,3,45,21,35,78,5};
    len = sizeof(num) / sizeof(num[0]);

    bubble_sort(num, len);
    printf("%d\n", len);
    imprimir_vetor(num, len);
    
    return 0;
}