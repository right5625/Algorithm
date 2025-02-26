import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	StringTokenizer st;
    	st = new StringTokenizer(br.readLine(), " ");
    	int N = Integer.parseInt(st.nextToken()), L = Integer.parseInt(st.nextToken());
    	List<Integer> h = new ArrayList<>();
    	st = new StringTokenizer(br.readLine(), " ");
    	for (int i = 0; i < N; i++) {
    		h.add(Integer.parseInt(st.nextToken()));
    	}
    	
    	Collections.sort(h);
    	for (int i = 0; i < N; i++) {
    		if (h.get(i) > L) {
    			break;
    		}
    		L++;
    	}
    	bw.write(L + "\n");
    	bw.flush();
    }
}