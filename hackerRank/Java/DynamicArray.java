import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class DynamicArray {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
         Scanner scan = new Scanner(System.in);
        int N,Q;
        int lastAns = 0;
        N = scan.nextInt();
        Q = scan.nextInt();
        
        int arr[][] = new int[Q][3];
        
        for(int i = 0 ; i < Q ; i++){
            for(int j = 0 ; j < 3 ; j++){
                arr[i][j] = scan.nextInt();
            }
        }
        scan.close(); 
        ArrayList<ArrayList<Integer>> seqList = new ArrayList<ArrayList<Integer>>();
        for(int k = 0 ; k < N ; k++){
            seqList.add(new ArrayList<Integer>());
        }
        
        for(int a = 0 ; a < Q ; a++){
           
            if(arr[a][0] == 1){
                
                int index = ((arr[a][1]^lastAns)%N);
                seqList.get(index).add(arr[a][2]);
                
                
            }
            if(arr[a][0] == 2){
                
                int index2 = ((arr[a][1]^lastAns)%N);
                int index3 = (arr[a][2])%(seqList.get(index2).size());
                
                lastAns = seqList.get(index2).get(index3);
                System.out.println(lastAns);
                
            }
            
        }
    }
}
