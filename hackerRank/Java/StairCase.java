import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StairCase {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String whiteSpace = " ";
        String hash = "#";

        for(int i = 0; i < n; i++){
            for(int j = n-1; j > i; j--){
                System.out.print(whiteSpace);
            }
            for(int j = 0; j <= i; j++){
                System.out.print(hash);
            }
            System.out.println("");
        }
    }
    
}
