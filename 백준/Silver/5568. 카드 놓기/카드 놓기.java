import java.io.*;
import java.util.*;

public class Main {
    static int n, k;
    static int[] cards;
    static Set<String> uniqueNumbers = new HashSet<>();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        
        cards = new int[n];
        for (int i = 0; i < n; i++) {
            cards[i] = Integer.parseInt(br.readLine());
        }
        
        permutation(new ArrayList<>(), new boolean[n]);
        
        System.out.println(uniqueNumbers.size());
    }
    
    static void permutation(List<Integer> current, boolean[] visited) {
        if (current.size() == k) {
            StringBuilder sb = new StringBuilder();
            for (int num : current) {
                sb.append(num);
            }
            uniqueNumbers.add(sb.toString());
            return;
        }
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                current.add(cards[i]);
                
                permutation(current, visited);
                
                current.remove(current.size() - 1);
                visited[i] = false;
            }
        }
    }
}