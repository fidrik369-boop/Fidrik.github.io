import java.util.Scanner;

class ArithmeticDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Taking input from user
        System.out.print("Enter first integer: ");
        int num1 = sc.nextInt();

        System.out.print("Enter second integer: ");
        int num2 = sc.nextInt();

        // Performing arithmetic operations
        int sum = num1 + num2;
        int difference = num1 - num2;
        int product = num1 * num2;
        int quotient = num1 / num2;   // integer division
        int remainder = num1 % num2;// modulus

        // Displaying results
        System.out.println("Addition: " + sum);
        System.out.println("Subtraction: " + difference);
        System.out.println("Multiplication: " + product);
            System.out.println("Division (Quotient): " + quotient);
            System.out.println("Remainder: " + remainder);
      sc.close();
    }
}
