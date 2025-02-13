import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int[] A = new int[N];
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine(), " ");
		int B = Integer.parseInt(st.nextToken()), C = Integer.parseInt(st.nextToken());
		
		long result = 0;
		for (int i = 0; i < N; i++) {
			A[i] = Math.max(A[i] - B, 0);
			result++;
			if (A[i] > 0) {
				result += A[i] / C;
				if (A[i] % C != 0) {
					result++;
				}
			}
		}
		System.out.println(result);
	}
}