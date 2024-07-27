import java.util.Scanner;

public class Main {
    public static void main(String[]args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();

        if(a >= 90 && a <= 100){
            System.out.printf("A");
        }
        else if(a >= 80 && a <= 89){
            System.out.printf("B");
        }
        else if(a >= 70 && a <= 79){
            System.out.printf("C");
        }
        else if(a >= 60 && a <= 69){
            System.out.printf("D");
        }
        else{
            System.out.printf("F");
        }
    }
}