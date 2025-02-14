import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		HashMap<Integer, int[]> map = new LinkedHashMap<>();
		for (int i = 0; i < N * N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int key = Integer.parseInt(st.nextToken());
			int[] arr = new int[4];
			for (int j = 0; j < 4; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
			}
			map.put(key, arr);
		}
		int[][] A = new int[N][N];
		
		int[] dr = {-1, 1, 0, 0};
		int[] dc = {0, 0, -1, 1};
		for (int k : map.keySet()) {
			ArrayList<int[]> pos1 = new ArrayList<>();
			int maxCnt = 0;
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < N; c++) {
					if (A[r][c] == 0) {
						int cnt = 0;
						for (int i = 0; i < 4; i++) {
							int mr = r + dr[i], mc = c + dc[i];
							if (mr >= 0 && mr < N && mc >= 0 && mc < N) {
								int[] arr = map.get(k);
								for (int j = 0; j < 4; j++) {
									if (A[mr][mc] == arr[j]) {
										cnt++;
										break;
									}
								}
							}
						}
						if (maxCnt < cnt) {
							maxCnt = cnt;
							pos1.clear();
							pos1.add(new int[] {r, c});
						}
						else if (maxCnt == cnt) {
							pos1.add(new int[] {r, c});
						}
					}
				}
			}
			if (pos1.size() == 1) {
				int[] rc = pos1.get(0);
				A[rc[0]][rc[1]] = k;
				continue;
			}
			
			ArrayList<int[]> pos2 = new ArrayList<>();
			maxCnt = 0;
			for (int[] rc: pos1) {
				int r = rc[0], c = rc[1];
				int cnt = 0;
				for (int i = 0; i < 4; i++) {
					int mr = r + dr[i], mc = c + dc[i];
					if (mr >= 0 && mr < N && mc >= 0 && mc < N && A[mr][mc] == 0) {
						cnt++;
					}
				}
				if (maxCnt < cnt) {
					maxCnt = cnt;
					pos2.clear();
					pos2.add(new int[] {r, c});
				}
				else if (maxCnt == cnt) {
					pos2.add(new int[] {r, c});
				}
			}
			if (pos2.size() == 1) {
				int[] rc = pos2.get(0);
				A[rc[0]][rc[1]] = k;
				continue;
			}
			
			int[] pos3 = {Integer.MAX_VALUE, Integer.MAX_VALUE};
			for (int[] rc: pos2) {
				int r = rc[0], c = rc[1];
				if (r < pos3[0]) {
					pos3[0] = r;
					pos3[1] = c;
				}
				else if (r == pos3[0]) {
					pos3[1] = Math.min(pos3[1], c);
				}
			}
			A[pos3[0]][pos3[1]] = k;
		}
		
		int[] s = {0, 1, 10, 100, 1000};
		int result = 0;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				int cnt = 0;
				for (int i = 0; i < 4; i++) {
					int mr = r + dr[i], mc = c + dc[i];
					if (mr >= 0 && mr < N && mc >= 0 && mc < N) {
						int[] arr = map.get(A[r][c]);
						for (int j = 0; j < 4; j++) {
							if (A[mr][mc] == arr[j]) {
								cnt++;
								break;
							}
						}
					}
				}
				result += s[cnt];
			}
		}
		System.out.println(result);
	}
}