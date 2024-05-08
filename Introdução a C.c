/* Resumo de Introdução a C / C++ */

//Bibliotecas	http://linguagemc.com.br/a-biblioteca-padrao-da-linguagem-c/
#include <stdio.h> //Biblioteca de entrada e saida
#include <stdbool.h> //Biblioteca de valores Booloeano
#include <math.h> //Biblioteca de funções matemáticas
#include <time.h> //Biblioteca de Tempo e Data
#include <stdlib.h> //Biblioteca de geração de numeros aleatórios
#include <ctype.h> //Biblioteca de Manipulação de caracteres
#include <string.h> // Biblioteca de manipulação de strings

// Constantes '#define [mome] [constante] 
#define constante_int 10 // define uma constanta inteira 
#define constante_string "Caracteres" // define uma constante em string

// Comentários

/*	Bloco de Comentários 

	Compilador: 
		gcc -o nome_do_arquivo nome_do_arquivo.c -Wall -pedantic - ansi
		No Prompt de comando: nome_do_arquivo.exe
		No Visual Code .\"nome_do_arquivo.exe"

*/



// Função Principal - Primeira a ser executada pelo programa
int main(void) {

	// Tipos de Variáveis
	
	int inteiro;
	char caracteres;
	double ponto_flutuante_duplo;
	float ponto_flutuante_simples;
	// void vazio;
	
	/*
		int = Número Inteiro - unsigned / singed / long
		char = Caractere - unsigned / singed
		float = Numero flutuante simples 
		double = ponro flutuante duplo - long
		void = Vazio
		
		Declaração:
			[variavel] nome_da_variavel ";" ou " = [valor];"
	*/
	
	// Entrada e Saída
	
	printf("Imprime uma mensagen na tela\n"); // para quebra de linha usar '\n'
	scanf("%d", &inteiro); // Recebe uma mensagem do usuário, usa '&' para atribuir valor a uma variavel
		//Quando se recebe uma string, não há necesidade de utilizar '&' para atribuir valores

	/*
			"%c" Caracter simples
			"%d" Inteiro decimal com sinal
			"%i" Inteiro decimal com sinal
			"%E" Real em notação científica com E
			"%e" Real em notação científica com e
			"%f" Real em ponto flutuante
			"%lf" Real em ponto flutuante duplo (double)
			"%G" %E ou %f, o que for mais curto
			"%g" %g ou %f, o que for mais curto
			"%o" Inteiro em base octal
			"%s" Cadeia Caracteres
			"%u" Inteiro decimal sem sinal
			"%x" Inteiro em base hexadecimal (letras minúsculas)
			"%X" Inteiro em base hexadecimal (letras maiúsculas)
			"%p" Endereço de memória
			"%%" Imprime o caractere %
			
			Códigos de Conversão de Entrada:
			
				%{largura}{modificadores}tipo		
				'h': Os tipos d, i e n, que são int passam a ser short int e os tipos o, u e x,
				também int passam a ser unsigned short int.
				'l': Os tipos d, i e n passam a ser long int e os tipos o, u e x passam a
				unsigned long int. Os tipos e, f e g passam de float para double.
				'L': Os tipos e, f e g passam de float para long double
		
			
			Código de Conversão de Saída:
			
				%[modificadores][largura][.precisão][comprimento]código
				
				[modificadores] Usados logo após o caractere %.
					’-’ Um sinal de menos serve para especificar que o argumento deve ser justificado à esquerda no seu campo de impressão. Caso nenhum sinal seja usado o argumento será ajustado à direita.
					’+’ Força que o resultado seja precedido por sinal de menos ou de mais, mesmo para números positivos. O padrão é que somente negativos sejam precedidos por sinal de menos. espaço Caso nenhum sinal vá ser escrito, um espaço é inserido antes do valor.
					’#’ Usado com o, x ou X precede o valor com 0, 0x ou 0X respectivamente para valores diferentes de zero. Usado com e, E e f, força que a saída contenha um ponto decimal mesmo que não haja parte fracionária. Por padrão, se não há parte fracionária o ponto decimal não é escrito. Usado com g ou G o resultado é o mesmo que com e ou E, mas os zeros finais não são retirados.
					’0’ Completa o campo, pela esquerda, com zeros (0) ao invés de espaços
				
				[largura] Caso seja usado um número inteiro, este especifica o tamanho mínimo do campo onde o argumento será impresso
				
				[.precisão] Este número tem diferentes significados dependendo do código usado.
					caracteres: No caso de impressão de cadeia de caracteres (s), este número especifica o número máximo de caracteres de uma cadeia de caracteres a serem impressos.
					ponto flutuante: No caso de formato (e, E, f) é o número de dígitos a serem impressos a direita do ponto, ou seja o número de casas decimais. Para o formato g ou G é o número máximo dígitos significativos.
					inteiros: No formatos inteiros (d, i, o, u, x, X) a precisão especificou o número máximo de dígitos a serem impressos. Se o número de
					caracteres a serem impressos é menor que este o resultado é completado com brancos. O valor não é truncado
				
				comprimento: Modifica os formatos da seguinte maneira:
					'l' Aplicado aos formatos de tipo d, i, o, u, x e X indicando que o dado é do tipo long int e não int.
					'h' Modifica o dado, nos formatos d, i, o, u, x e X para tipo short int.
					'L' Nos formatos e, E, f, g e G o argumento é modificado para long double		
		*/
		
		// Tratamento de Variáveis
		
		/*
			Atribuição Composta: 
				variavel = variavel [operador] expressão	
		*/
		
		inteiro = inteiro + 2; 
		// Ou
		inteiro += 2;
	
		/*
			Operadores Aritiméticos
			
				'+' Mais unário
				'-' Menos unário
				'++' Incremento
				'–-' Decremento
				'*' Multiplicação
				'/' Divisão
				'%' Resto da divisão
				'+' Soma
				'-' Subtração		
		*/
		
		// Blocos de Comando (Decisão)
		
		int a = 1;
		int b = 2;

		if(a > b){
			//comandos;
		}
		else if (b > a){
			//comandos;
		}
		else{
			//comandos;
		}
		
		int dia_da_semana;

		switch (dia_da_semana){
			
			case 1: 
				//comandos; se o dia_da_semana for igual a 1 ele entra no 'case 1'
				break;
			case 2:
				//comandos;
				break;
			//	.
			//	.
			//	.
			default:
			//comandos;
		}
		// Comando ternário:
			a > b ? b*2 : a*2; // expressão1 ? expressão2 : expressão3
		//Verfica o resultado da [expressão1], retorna [expressão2] caso o resultado seja verdadeiro ou [expressão3] caso seja falso
		
		// Laços de Repetição 'for' 'while' 'do while'
		
		int i;

		a = 0;
		b = 100;

		for(i=0; i<b; i++){ 
			/* código a ser repetido*/
		}
		
		while(a < b){
			/* código a ser repetido e que termine fazendo a condição ser falsa 'return false' */ 
		}
		
		do{
			/* código a ser repetido*/
		}while(a < b);
		
		// Vetores - tipo nome_da_variavel[tamanho];
		int num[10];	//Vetor de 10 número inteiros
		float  notas[20];	// Vetor de 20 números reais
		char carac[30];	//Vetor de 30 Caracteres
		
		// tipo nome[dim] = {lista_de_valores};
		int vetor[5] = { 10, 15, 20, 25, 30 };
		
		// Funções da Biblioteca string.h
		char nome[12] = "Davi";
		char sobrenome[12] = "Mattos";
		char copia[12];
		int tamanho;

		tamanho = strlen(nome); /* Retorna o tamanho da string */
		// strlen(string);

		strcpy(copia, nome); /*Faz uma cópia de um vetor para outro*/
		// strcpy(destino, origem);
		// strncpy(destino, origem, tamanho);

		strcat(nome, sobrenome); /*Realiza a concatenação de uma string a outra*/
		/*  Saída: 'DaviMattos'
			strcat(destino, string);
			strncat(destino, string, tamanho);
		*/
		
		gets(nome); // Função 'scanf' para string

		tamanho = strcmp(nome, sobrenome); // Compara o conteúdo de duas strings
		/*
			0: conteúdo das strings são iguais
			< 0: conteúdo da string1 é menor do que string2
			> 0: conteúdo da string1 é maior do que string2

			variável_do_tipo_inteiro = strncmp(string1, string2, tamanho a ser comparado);
		*/
		
		// Matrizes - tipo nome [dim1][dim2][dim3]...[dimN];
		

		//Matriz tipo nome [dim1][dim2][dim3]...[dimN];
		int matriz[10][20]; //	int matriz [linha][coluna];
		int m2[10][20];
		int m3[10][20];
		
		// Multiplicação de Matrizes
		
		int i, j, k, count;

		for (i = 0; i < 10; i++){
			for (j = 0; j < 20; j++){
				count = 0;
	 			for (k = 0; k < 20; k++)
					count += matriz[i][k] * m2[k][j];
				m3[i][j] = count;
			}
		}
		
		//Ponteiros
		int *numero; // declaração de ponteiro [tipo] *[nome]
		
	return 0;
}

/* Funções e Estruturas */