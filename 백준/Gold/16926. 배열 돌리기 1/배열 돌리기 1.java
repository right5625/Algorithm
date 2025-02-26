import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	StringTokenizer st;
    	st = new StringTokenizer(br.readLine(), " ");
    	int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken()), R = Integer.parseInt(st.nextToken());
    	int[][] A = new int[N][M];
    	for (int r = 0; r < N; r++) {
    		st = new StringTokenizer(br.readLine(), " ");
    		for (int c = 0; c < M; c++) {
    			A[r][c] = Integer.parseInt(st.nextToken());
    		}
    	}
    	
    	for (int i = 0; i < R; i++) {
    		int startR = 0, endR = N - 1, startC = 0, endC = M - 1;
    		while (startR < endR && startC < endC) {
    			int t = A[startR][startC];
    			for (int c = startC; c < endC; c++) {
    				A[startR][c] = A[startR][c + 1];
    			}
    			for (int r = startR; r < endR; r++) {
    				A[r][endC] = A[r + 1][endC];
    			}
    			for (int c = endC; c > startC; c--) {
    				A[endR][c] = A[endR][c - 1];
    			}
    			for (int r = endR; r > startR + 1; r--) {
    				A[r][startC] = A[r - 1][startC];
    			}
    			A[startR + 1][startC] = t;
    			startR++; endR--; startC++; endC--;
    		}
    	}
    	
    	for (int i = 0; i < N; i++) {
    		bw.write(Arrays.stream(A[i]).mapToObj(String::valueOf).collect(Collectors.joining(" ")) + "\n");
    	}
    	bw.flush();
    }
}