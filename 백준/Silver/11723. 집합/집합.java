import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	StringTokenizer st;
    	Set<Integer> set = new HashSet<>();
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	String s = st.nextToken();
        	if (s.equals("add")) {
        		set.add(Integer.parseInt(st.nextToken()));
        	} else if (s.equals("remove")) {
        		set.remove(Integer.parseInt(st.nextToken()));
        	} else if (s.equals("check")) {
        		bw.write(set.contains(Integer.parseInt(st.nextToken())) ? "1\n" : "0\n");
        	} else if (s.equals("toggle")) {
        		int x = Integer.parseInt(st.nextToken());
        		if (!set.remove(x)) {
        			set.add(x);
        		}
        	} else if (s.equals("all")) {
        		set = new HashSet<>();
        		for (int j = 1; j <= 20; j++) {
        			set.add(j);
        		}
        	} else {
        		set.clear();
        	}
        }
        bw.flush();
    }
}