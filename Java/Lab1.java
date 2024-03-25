import java.util.*;

class Lab1 {
    public static void main(String[] args) {
        double R, r, pi = 3.14159;

        Scanner sc = new Scanner(System.in);

        R = sc.nextDouble();
        r = sc.nextDouble();
        System.out.println((pi*(Math.pow(R,2)-Math.pow(r, 2))));

    }
}

class Atividade2 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Nome: ");
        String nome = sc.nextLine();

        System.out.print("Idade: ");
        int idade = sc.nextInt();

        System.out.print("Altura: ");
        double altura = sc.nextDouble();

        System.out.printf("\nNome: %s\nIdade: %d\nAltura:%.2f", nome, idade, altura);

    }
}

class Atividade3{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Nota 1: ");
        double nota1 = sc.nextDouble();
        System.out.print("Nota 2: ");
        double nota2 = sc.nextDouble();

        System.out.println( (nota1 + nota2)/ 2 >= 7
        ? "Aprovado"
        : (nota1 + nota2)/ 2 < 7 && (nota1 + nota2)/ 2 >= 3
        ? "Prova Final"
        : "Reprovado");

    }
}

class Atividade4 {

    static int factorial( int n ) {
        return n != 0 ? n * factorial(n-1) : 1;
    }

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um numero: ");
        int num = sc.nextInt();

        System.err.printf("\n%d! = %d",num, factorial(num));
    }    
}