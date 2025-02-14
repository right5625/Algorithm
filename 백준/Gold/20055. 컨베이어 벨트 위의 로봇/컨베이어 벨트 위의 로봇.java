import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken()), K = Integer.parseInt(st.nextToken());
		ArrayList<Integer> A = new ArrayList<>();
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N * 2; i++) {
			A.add(Integer.parseInt(st.nextToken()));
		}
		ArrayList<Boolean> R = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			R.add(false);
		}
		
		int cnt = 0, res = 0;
		while (cnt < K) {
			A.add(0, A.get(N * 2 - 1));
			A.remove(N * 2);
			R.add(0, false);
			R.remove(N);
			R.set(N - 1, false);
			for (int i = N - 1; i > 0; i--) {
				if (A.get(i) > 0 && !R.get(i) && R.get(i - 1)) {
					A.set(i, A.get(i) - 1);
					R.set(i, true);
					R.set(i - 1, false);
					if (A.get(i) == 0) {
						cnt++;
					}
				}
			}
			if (A.get(0) > 0 && !R.get(0)) {
				A.set(0, A.get(0) - 1);
				R.set(0, true);
				if (A.get(0) == 0) {
					cnt++;
				}
			}
			res++;
		}
		System.out.println(res);
	}
}