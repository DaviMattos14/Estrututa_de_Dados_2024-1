
arvore_bb: arvore_binaria_busca.c
	gcc -o arvore_binaria_busca arvore_binaria_busca.c -ansi -Wall -pedantic -std=c99
	arvore_binaria_busca.exe	
bubble_sort: bubble_sort.c
	gcc -o bubble_sort bubble_sort.c -ansi -Wall -pedantic -std=c99
	bubble_sort.exe
linked_list: Lista_encadeada.c
	gcc -o linked_list Lista_encadeada.c -ansi -Wall -pedantic -std=c99
	linked_list.exe
teste1: teste.c
	gcc -o test1 teste.c -ansi -Wall -pedantic -std=c99
	test1.exe
teste2: teste2.c
	gcc -o test2 teste2.c -ansi -Wall -pedantic -std=c99
	test2.exe
arvore_rn:
	gcc -o arvore_rn arvore_rn.c -ansi -Wall -pedantic -std=c99
	arvore_rn.exe

