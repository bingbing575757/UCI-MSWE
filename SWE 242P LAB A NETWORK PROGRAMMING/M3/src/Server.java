import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Server {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Please input the folder path.");
            return;
        }

        String folderPathString = args[0];
        Path folderPath = Paths.get(folderPathString);

        if (!Files.isDirectory(folderPath)) {
            System.err.println("Invalid folder path" + folderPath);
            return;
        }

        try (ServerSocket ss = new ServerSocket(8889);
             Socket st = ss.accept();
             BufferedReader in = new BufferedReader(new InputStreamReader(st.getInputStream()));
             PrintWriter out = new PrintWriter(st.getOutputStream(), true)) {

            while (true) {
                String command = in.readLine();

                if (command == null || command.isEmpty()) {
                    continue;
                }

                if (command.equals("index")) {
                    handleIndexCommand(folderPath, out);
                } else if (command.startsWith("get ")) {
                    handleGetCommand(folderPath, command, out);
                    break;
                } else {
                    out.println("error\nInvalid command.\nEOF\n");
                    System.err.println("Invalid command.");
                }
                out.flush();
            }
            out.close();
            in.close();
            st.close();
            ss.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void handleIndexCommand(Path folderPath, PrintWriter out) {
        StringBuilder sb = new StringBuilder();
        sb.append("Folder Path: ").append(folderPath.toAbsolutePath()).append("\n");

        try (DirectoryStream<Path> stream = Files.newDirectoryStream(folderPath)) {
            for (Path p : stream) {
                sb.append(p.getFileName()).append("\n");
            }
            sb.append("EOF\n");
            out.print(sb);
        } catch (IOException e) {
            out.println("error\nInvalid folder path.\nEOF\n");
            System.err.println("Invalid folder path.");
            e.printStackTrace();
        }
    }

    private static void handleGetCommand(Path folderPath, String command, PrintWriter out) {
        String filePathString = command.split(" ")[1];
        Path filePath = Paths.get(folderPath.toString(), filePathString);
        if (Files.notExists(filePath)) {
            out.println("error\nInvalid file name.\nEOF\n");
            System.err.println("Invalid file name.");
            return;
        }
        try {
            out.println("ok");
            Files.lines(filePath).forEach(line -> out.println(line));
            out.println("EOF");
        } catch (IOException e) {
            out.println("error\nError reading file.\nEOF\n");
            System.err.println("Error reading file.");
            e.printStackTrace();

    }
}}
