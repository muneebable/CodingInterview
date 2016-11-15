import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PlusMinus {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double pos=0, neg=0 ,zer=0;
        int n = in.nextInt();
        double size=n;
        int arr[] = new int[n];
        for(int arr_i=0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        
        for(int i=0; i<arr.length ; i++){
            if(arr[i]>0){
                pos=pos+1;
            }else if(arr[i]<0){
                neg=neg+1;
            }else if(arr[i]==0){
                zer=zer+1;
            }
        }
       
        System.out.println(String.format("%6f",pos/size));
        System.out.println(String.format("%6f",neg/size));
        System.out.println(String.format("%6f",zer/size));
    }
}
