import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;

import java.util.regex.*;

public class Array1 {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int inp = in.nextInt();
        String[] s = new String[inp];
        for(int i=0; i<inp;i++)
        {
            s[i] = in.next();
        }
        
        int q = in.nextInt();
        for(int j=0; j<q;j++){
            int count=0;
            String st = in.next();
            for(int k=0; k<inp; k++){
                if(st.equals(s[k])){
                    count+=1;
                }
            }
            System.out.println(count);
        }
    }
}