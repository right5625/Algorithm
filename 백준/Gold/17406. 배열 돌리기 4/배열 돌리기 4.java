import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M, K;
	static int[][] A;
	static int[][] rcs;
	static ArrayList<int[]> seqList = new ArrayList<>();
	static int[][] B;
	static int result = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		A = new int[N + 1][M + 1];
		for (int i = 1; i < N + 1; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 1; j < M + 1; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		rcs = new int[K][3];
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < 3; j++) {
				rcs[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		permutation(new ArrayList<>());
		
		for (int[] seq: seqList) {
			rotate(seq);
			for (int r = 1; r < N + 1; r++) {
				int sum = 0;
				for (int c = 1; c < M + 1; c++) {
					sum += B[r][c];
				}
				result = Math.min(result, sum);
			}
		}
		
		System.out.println(result);
	}
	
	static void permutation(ArrayList<Integer> list) {
		if (list.size() == K) {
			seqList.add(list.stream().mapToInt(Integer::intValue).toArray());
			return;
		}
		for (int i = 0; i < K; i++) {
			if (!list.contains(i)) {
				ArrayList<Integer> a = new ArrayList<>(list);
				a.add(i);
				permutation(a);
			}
		}
	}
	
	static void rotate(int[] seq) {
		B = new int[N + 1][M + 1];
		for (int r = 1; r < N + 1; r++) {
			for (int c = 1; c < M + 1; c++) {
				B[r][c] = A[r][c];
			}
		}
		for (int n: seq) {
			int r = rcs[n][0], c = rcs[n][1], s = rcs[n][2];
			int minR = r - s, minC = c - s, maxR = r + s, maxC = c + s;
			while (minR != maxR) {
				int t = B[minR][minC];
				for (int k = minR + 1; k <= maxR; k++) {
					B[k - 1][minC] = B[k][minC];
				}
				for (int k = minC + 1; k <= maxC; k++) {
					B[maxR][k - 1] = B[maxR][k];
				}
				for (int k = maxR - 1; k >= minR; k--) {
					B[k + 1][maxC] = B[k][maxC];
				}
				for (int k = maxC - 1; k >= minC; k--) {
					B[minR][k + 1] = B[minR][k];
				}
				B[minR][minC + 1] = t;
				minR++; minC++; maxR--; maxC--;
			}
		}
	}
}