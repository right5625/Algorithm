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
			result += A[i] % C == 0 ? A[i] / C : A[i] / C + 1;
		}
		System.out.println(result);
	}
}