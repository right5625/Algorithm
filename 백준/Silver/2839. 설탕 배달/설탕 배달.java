import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int result = -1;
        for (int i = N / 5; i >= 0; i--) {
        	if ((N - i * 5) % 3 == 0) {
        		result = i + (N - i * 5) / 3;
        		break;
        	}
        }
        bw.write(result + "\n");
        bw.flush();
    }
}