package FUN;
import java.util.*;
class PrimeRecursive{
    static boolean isPrime(int n, int divisor) {
        if (divisor == 1) {
            return true;
        }
        if (n % divisor == 0) {
            return false;
        }
        return isPrime(n, divisor - 1);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number to check if it's prime:");
        int n = scanner.nextInt();
        scanner.close();

        if (n <= 1) {
            System.out.println(n + " is not a prime number.");
        } else if (isPrime(n, (int) Math.sqrt(n))) {
            System.out.println(n + " is a prime number.");
        } else {
            System.out.println(n + " is not a prime number.");
        }
    }
}