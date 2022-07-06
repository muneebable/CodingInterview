import java.io.*;
import java.util.*;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
public class TimeConversion {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        String time_12 = in.nextLine();
        LocalTime time = LocalTime.parse(time_12, DateTimeFormatter.ofPattern("hh:mm:ssa"));
        System.out.println(time.format(DateTimeFormatter.ofPattern("HH:mm:ss")));
    }
}
