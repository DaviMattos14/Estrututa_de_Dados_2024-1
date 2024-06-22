#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *parent;
    int *rank;
    int *size; // Array to keep track of the size of each set
    int n;
} UnionFind;

UnionFind* createSet(int n) {
    UnionFind *uf = (UnionFind*) malloc(sizeof(UnionFind));
    uf->parent = (int*) malloc((n + 1) * sizeof(int));
    uf->rank = (int*) malloc((n + 1) * sizeof(int));
    uf->size = (int*) malloc((n + 1) * sizeof(int));
    uf->n = n;
    for (int i = 1; i <= n; i++) {
        uf->parent[i] = i;
        uf->rank[i] = 0;
        uf->size[i] = 1;
    }
    return uf;
}

int find(UnionFind *uf, int x) {
    if (uf->parent[x] != x) {
        uf->parent[x] = find(uf, uf->parent[x]);
    }
    return uf->parent[x];
}

void unionSets(UnionFind *uf, int x, int y) {
    int rootX = find(uf, x);
    int rootY = find(uf, y);

    if (rootX != rootY) {
        if (uf->rank[rootX] < uf->rank[rootY]) {
            uf->parent[rootX] = rootY;
            uf->size[rootY] += uf->size[rootX];
        } else {
            uf->parent[rootY] = rootX;
            uf->size[rootX] += uf->size[rootY];
            uf->rank[rootX]++;
        }
    }
}

int getMaxGroupSize(UnionFind *uf) {
    int maxSize = 0;
    for (int i = 1; i <= uf->n; i++) {
        if (uf->parent[i] == i && uf->size[i] > maxSize) {
            maxSize = uf->size[i];
        }
    }
    return maxSize;
}

void freeSet(UnionFind *uf) {
    free(uf->parent);
    free(uf->rank);
    free(uf->size);
    free(uf);
}

int main() {
    int testCases;
    scanf("%d", &testCases);

    while (testCases--) {
        int n, m;
        scanf("%d %d", &n, &m);

        UnionFind *uf = createSet(n);

        for (int i = 0; i < m; i++) {
            int a, b;
            scanf("%d %d", &a, &b);
            unionSets(uf, a, b);
        }

        printf("%d\n", getMaxGroupSize(uf));
        freeSet(uf);
    }

    return 0;
}
