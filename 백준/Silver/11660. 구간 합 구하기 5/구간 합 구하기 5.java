import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        int[][] A = new int[N + 1][N + 1];
        for (int i = 1; i <= N; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
            for (int j = 1; j <= N; j++) {
            	A[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        int[][] DP = new int[N + 1][N + 1];
        for (int i = 1; i <= N; i++) {
        	for (int j = 1; j <= N; j++) {
        		DP[i][j] = A[i][j] + DP[i][j - 1];
        	}
        	for (int j = 1; j <= N; j++) {
        		DP[i][j] += DP[i - 1][j];
        	}
        }
        
        for (int i = 0; i < M; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	int x1 = Integer.parseInt(st.nextToken()), y1 = Integer.parseInt(st.nextToken()), x2 = Integer.parseInt(st.nextToken()), y2 = Integer.parseInt(st.nextToken());
        	bw.write((DP[x2][y2] - DP[x2][y1 - 1] - DP[x1 - 1][y2] + DP[x1 - 1][y1 - 1]) + "\n");
        }
        bw.flush();
    }
}
