/*
    Estrutura de Dados
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct No
{
  int valor;
  struct No* prox;
}node;

/* Lista encadeada*/
void Imprime_Lista_Encadeada(node *pt) {
  while (pt != NULL) {
    printf("%d ", pt->valor);
    pt = pt->prox;
  }
}

void insere_no_fim(node *ptcab, int novo_valor){
  node * novo_no = (node *) malloc(sizeof(node));
  novo_no->valor = novo_valor;
  while (ptcab->prox != NULL)
  {
    ptcab = ptcab ->prox;
  }
  ptcab->prox = novo_no;
  novo_no->prox = NULL;
  
}
int main(void){
  node * head = (node *)malloc(sizeof(node));
  head->valor = 14;
  head->prox = NULL;

  node *ptcab = head;

  insere_no_fim(ptcab,20);
  insere_no_fim(ptcab, 61);
  Imprime_Lista_Encadeada(head);
  return 0;
}