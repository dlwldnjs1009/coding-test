import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = bf.readLine().split(" ");
        int a = Integer.parseInt(strs[0]);
        int b = Integer.parseInt(strs[1]);
        String[] strs1 = bf.readLine().split(" ");
        int c = Integer.parseInt(strs1[0]);
        int h_to_m, total_m;
        h_to_m = a * 60;
        total_m = h_to_m + b + c;
        if (total_m/60 > 23){
            System.out.print((total_m/60) % 24 + " " + total_m % 60);
        } else {
            System.out.print(total_m / 60 + " " + total_m % 60);
        }
        bf.close();
    }
}
