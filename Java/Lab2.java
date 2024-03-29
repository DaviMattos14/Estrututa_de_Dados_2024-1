import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;

class Lab2_A1{
    public static void main(String[] args){
        
        ArrayList notas = new ArrayList<Double>();
        double somaNotas = 0;

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a nota: ");
        double entrada = sc.nextDouble();

        while (entrada != -1) {
            
            somaNotas += entrada;
            System.out.print("Digite a nota: ");
            entrada = sc.nextDouble();
            notas.add(entrada);
        }

        System.out.printf("\nMedia: %.2f\n", (somaNotas / notas.size()));
    }
}

class Lab2_A2 {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int d_Frango = sc.nextInt(), d_Bife = sc.nextInt(), d_Massa = sc.nextInt();

        int p_Frango = sc.nextInt(), p_Bife = sc.nextInt(),p_Massa = sc.nextInt();

        int resp = 0;

        if (d_Frango < p_Frango)
            resp += Math.abs(d_Frango - p_Frango);
        if (d_Bife < p_Bife)
            resp += Math.abs(d_Bife - p_Bife);
        if (d_Massa < p_Massa)
            resp += Math.abs(d_Massa - p_Massa);

        System.out.println(resp);
    }
    
}

class Lab2_A3 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double r = sc.nextDouble();

        System.out.printf("VOLUME = %.3f\n", ((4/3.0) * (3.14159 * Math.pow( r , 3 ))));

    }
}

class Lab2_A4{
    public static void main(String[] args) {


        Scanner sc = new Scanner(System.in);

        String operador="", input="";

        System.out.println("Escolha uma operacao:\nSoma: +\nSubtracao: -\nMultiplicacao: *\nDivisao: /\n");
        while (input.equals("s") == false) {
            operador = input;
            input = sc.nextLine();
        }

        System.out.println("Digite dois numeros");
        int num1 = sc.nextInt(), num2 = sc.nextInt();

        switch (operador) {
            case "+":
            System.out.println(num1+num2);
                break;
            case "-":
            System.out.println(num1-num2);
                break;
            case "*":
            System.out.println(num1*num2);
                break;
            case "/":
            System.out.println(num1/num2);
                break;
        }

    }
}

class Lab2_A5{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double tempo = sc.nextInt();
        double vm = sc.nextInt();

        double litros = (vm * tempo) / 12;

        System.out.printf("%.3f", litros);

    }
}

class Lab2_A6 {
    
	private static int getRandomNumberInRange(int min, int max) {

		Random r = new Random();
		return r.nextInt((max - min) + 1) + min;
	}


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 1, min = 0, max = 100;
        String entrada = "";
        int num = getRandomNumberInRange(min, max);
        while (entrada.equalsIgnoreCase("Sim") == false){

            System.out.printf("Seu numero eh %d ?\n", num);
            entrada = sc.nextLine();

            if (entrada.equalsIgnoreCase("Sim") == false) {

                System.out.println("Maior ou menor?");
                entrada = sc.nextLine();
                if (entrada.equalsIgnoreCase("menor") == true) {
                    max = num;
                    num = getRandomNumberInRange(min, max);
                    i++;
                }
                if (entrada.equalsIgnoreCase("maior") == true) {
                    min = num;
                    num = getRandomNumberInRange(min, max);
                    i++;
                }
            }
        }
        System.out.printf("\nForam um total de %d iteracoes\n",i);
    }
}
