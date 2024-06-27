#include <stdio.h>
#include <stdlib.h>

typedef struct UnionFind{
    int *raiz, *tam;
} UnionFind;

UnionFind* criarConj(int n){
    UnionFind *conj = (UnionFind*) malloc(sizeof(UnionFind));
    conj->raiz = (int*) malloc((n+1) * sizeof(int));
    conj->tam = (int*) malloc((n+1) * sizeof(int));
    
    for (int i = 1; i <= n; i++){
        conj->raiz[i] = i;
        conj->tam[i] = 1;
    }
    return conj;
}

int find(UnionFind *conj, int x){

    if (conj->raiz[x] != x){
        conj->raiz[x] = find(conj, conj->raiz[x]);
    }
    return conj->raiz[x];
}

void uniao_conj(UnionFind *conj, int a, int b){
    int raizA = find(conj, a);
    int raizB = find(conj, b);

    if (raizA != raizB)
    {
        if (conj->tam[raizA] < conj->tam[raizB]){
            conj->raiz[raizA] = raizB;
            conj->tam[raizB] += conj->tam[raizA];
        }else{
            conj->raiz[raizB] = raizA;
            conj->tam[raizA] += conj->tam[raizB];
        }
    }
}

int tamMAX(UnionFind *conj,int n){
    int tamMAX = 0;
    for (int i = 1; i <= n; i++){
        if (conj->raiz[i] == i && conj->tam[i] > tamMAX){
            tamMAX = conj->tam[i];
        }
    }
    return tamMAX;
}

int main(){;
    int casos;
    scanf("%d", &casos);

    while (casos--){
        int n,m;
        scanf("%d %d", &n, &m);
        
        UnionFind *conj = criarConj(n);
        
        for (int i = 0; i < m; i++){
            int a, b;
            scanf("%d %d", &a, &b);
            uniao_conj(conj,a,b);
        }
        printf("%d\n",tamMAX(conj, n));
        free(conj);
    }
    return 0;
}