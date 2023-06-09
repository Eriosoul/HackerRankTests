/**
* Most HackerRank challenges require you to read input from stdin (standard input) and write output to stdout (standard output).
*
* One popular way to read input from stdin is by using the Scanner class and specifying the Input Stream as System.in. For example:
*
* Scanner scanner = new Scanner(System.in);
* String myString = scanner.next();
* int myInt = scanner.nextInt();
* scanner.close();
*
* System.out.println("myString is: " + myString);
* System.out.println("myInt is: " + myInt);
* The code above creates a Scanner object named  and uses it to read a String and an int. It then closes the Scanner object because there is no more input to read, and prints to stdout using System.out.println(String). So, if our input is:
*
* Hi 5
* Our code will print:
*
* myString is: Hi
* myInt is: 5
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        // Complete this line
        int b = scan.nextInt();
        // Complete this line
        int c = scan.nextInt();
        scan.close();

        System.out.println(a);
        // Complete this line
        System.out.println(b);
        // Complete this line
        System.out.println(c);
    }
}