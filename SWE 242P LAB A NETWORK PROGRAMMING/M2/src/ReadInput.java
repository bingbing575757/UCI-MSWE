import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ReadInput {

    public static void main(String[] args) {
        ExecutorService executorService = Executors.newFixedThreadPool(5);

        // Get the path of the src folder in the current working directory
        String directoryPath = "src";

        // Create a File object representing this path
        File directory = new File(directoryPath);

        // Check if the path exists and is a directory
        if (directory.exists() && directory.isDirectory()) {
            // Get all files in the directory
            File[] files = directory.listFiles();

            if (files != null) {
                // Iterate through the files
                for (File file : files) {
                    // Check if the file is a text file ending with .txt
                    if (file.isFile() && file.getName().endsWith(".txt")) {
                        final String fileName = file.getName(); // Get the file name

                        executorService.execute(() -> {
                            try {
                                countLines(file, fileName);
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                        });
                    }
                }
            } else {
                System.out.println("No files found in the directory.");
            }
        } else {
            System.out.println("Invalid directory path or directory does not exist.");
        }

        executorService.shutdown();
        try {
            executorService.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static void countLines(File file, String fileName) {
        BufferedReader inputStream;
        int lineCount = 0;

        try {
            inputStream = new BufferedReader(new FileReader(file));
            String line = inputStream.readLine();

            while (line != null) {
                lineCount++;
                line = inputStream.readLine();
            }
            inputStream.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println(fileName + ": " + lineCount + " lines");
    }
}
