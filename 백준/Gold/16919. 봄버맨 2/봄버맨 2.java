import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		char[][] A = new char[R][C];
		for (int i = 0; i < R; i++) {
			String s = br.readLine();
			for (int j = 0; j < C; j++) {
				A[i][j] = s.charAt(j);
			}
		}
		
		if (N != 1) {
			ArrayList<int[]> list = new ArrayList<>();
			int[] dr = {-1, 1, 0, 0};
			int[] dc = {0, 0, -1, 1};
			for (int s = 2; s <= N % 4 + 4; s++) {
				if (s % 2 == 0) {
					for (int i = 0; i < R; i++) {
						for (int j = 0; j < C; j++) {
							if (A[i][j] == 'O') {
								list.add(new int[] {i, j});
							}
							A[i][j] = 'O';
						}
					}
				}
				else {
					for (int[] a: list) {
						int r = a[0], c = a[1];
						A[r][c] = '.';
						for (int i = 0; i < 4; i++) {
							int mr = r + dr[i], mc = c + dc[i];
							if (mr >= 0 && mr < R && mc >= 0 && mc < C) {
								A[mr][mc] = '.';
							}
						}
					}
					list.clear();
				}
			}
		}
		
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				wr.write(A[i][j]);
			}
			wr.write('\n');
		}
		wr.flush();
	}
}