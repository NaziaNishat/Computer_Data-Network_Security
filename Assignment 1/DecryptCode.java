import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class DecryptCode {
	public static void main(String[] args) throws IOException {

		String key = "bxicl yo dthngavukfwerm ps";
		int incr = 0;

		Map<String, Integer> map = new HashMap<>();
		for (int i = 97; i <= 122; i++) {
			map.put(Character.toString((char) i), incr);
			incr++;
		}

		File in = new File("E:\\data.txt");
		File out = new File("E:\\decryptedFile.txt");
		if (!out.exists())
			out.createNewFile();
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(in)));
		BufferedWriter bw = new BufferedWriter(new FileWriter(out));

		String line = null;
		while ((line = br.readLine()) != null) {
			char[] array = line.toCharArray();
			for (int i = 0; i < array.length; i++) {
				if (array[i] >= 'a' && array[i] <= 'z') {
					String str = Character.toString(array[i]);
					array[i] = key.charAt(map.get(str));
				}
			}

			System.out.println(array);
			bw.write(array);
			bw.newLine();
		}
		br.close();
		bw.close();

	}
}
