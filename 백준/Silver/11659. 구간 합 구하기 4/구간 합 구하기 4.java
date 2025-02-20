import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        int[] A = new int[N + 1];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 1; i <= N; i++) {
        	A[i] = Integer.parseInt(st.nextToken());
        }
        
        int[] DP = new int[N + 1];
        for (int i = 1; i <= N; i++) {
        	DP[i] = A[i] + DP[i - 1];
        }
        
        for (int k = 0; k < M; k++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	int i = Integer.parseInt(st.nextToken()), j = Integer.parseInt(st.nextToken());
        	bw.write((DP[j] - DP[i - 1]) + "\n");
        }
        bw.flush();
    }
}
