import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static boolean[][] vst;
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	
	static void dfs(int r, int c) {
		vst[r][c] = true;
		for (int i = 0; i < 4; i++) {
			int mr = r + dr[i], mc = c + dc[i];
			if (mr >= 0 && mr < N && mc >= 0 && mc < N && !vst[mr][mc]) {
				dfs(mr, mc);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		int[][] A = new int[N][N];
		int max = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
				max = Math.max(max, A[i][j]);
			}
		}
		
		int result = 0;
		for (int m = 0; m < max; m++) {
			vst = new boolean[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (A[i][j] <= m) {
						vst[i][j] = true;
					}
				}
			}
			
			int cnt = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (!vst[i][j]) {
						dfs(i, j);
						cnt++;
					}
				}
			}
			result = Math.max(result, cnt);
		}
		bw.write(result + "\n");
		bw.flush();
	}
}