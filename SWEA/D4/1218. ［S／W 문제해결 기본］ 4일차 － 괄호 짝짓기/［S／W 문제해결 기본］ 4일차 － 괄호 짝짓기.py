import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int t = 1; t <= 10; t++) {
        	br.readLine();
        	Stack<Character> stack = new Stack<>();
        	Map<Character, Character> map = new HashMap<>();
        	map.put(')', '(');
        	map.put(']', '[');
        	map.put('}', '{');
        	map.put('>', '<');
        	
        	int res = 1;
        	for (char c: br.readLine().toCharArray()) {
        		if (map.containsKey(c)) {
        			if (stack.isEmpty() || map.get(c) != stack.pop()) {
        				res = 0;
        				break;
        			}
        		}
        		else {
        			stack.push(c);
        		}
        	}
        	bw.write("#" + t + " " + res + "\n");
        	bw.flush();
        }
    }
}