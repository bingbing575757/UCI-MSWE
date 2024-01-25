import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;

class ReadInput_new {
    public static void main(String[] args) {
        for (String arg : args) {
            countLines(arg);
        }
    }

    public static void countLines(String path) {
        File file = new File(path);
        if (!file.exists()) {
            System.out.println("File \'" + path + "\' does not exist!");
            return;
        }

        try (FileReader fr = new FileReader(file);
             LineNumberReader lnr = new LineNumberReader(fr)) {

            int lineNumber = 0;
            while (lnr.readLine() != null) {
                lineNumber++;
            }
            System.out.println(path + ": " + lineNumber);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
