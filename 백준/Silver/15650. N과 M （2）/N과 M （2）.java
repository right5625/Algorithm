import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static int N, M;
	static boolean[] vst;
	
	static void combination(ArrayList<Integer> list, int start, int rem) throws IOException {
		if (rem == 0) {
			bw.write(list.stream().map(String::valueOf).collect(Collectors.joining(" ")) + "\n");
			return;
		}
		
		for (int i = start; i <= N; i++) {
			if (!vst[i]) {
				vst[i] = true;
				list.add(i);
				combination(list, i + 1, rem - 1);
				list.remove(list.size() - 1);
				vst[i] = false;
			}
		}
	}
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        vst = new boolean[N + 1];
        combination(new ArrayList<>(), 1, M);
        bw.flush();
    }
}
