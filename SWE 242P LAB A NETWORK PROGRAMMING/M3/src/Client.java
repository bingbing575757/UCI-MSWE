//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.io.PrintWriter;
//import java.net.Socket;
//
//public class Client {
//    public static void main(String[] args) {
//        try {
//            Socket st = new Socket("localhost", 8889);
//            PrintWriter out = new PrintWriter(st.getOutputStream(), true);
//            BufferedReader in = new BufferedReader(new InputStreamReader(st.getInputStream()));
//            BufferedReader keyboardIn = new BufferedReader(new InputStreamReader(System.in));
//            while (true) {
//                System.out.print("client> ");
//                String command = keyboardIn.readLine();
//                if (command.equals("index") || command.startsWith("get ")) {
//                    out.println(command);
//                    String firstLine = "";
//                    String line = "";
//                    while (!(line = in.readLine()).equals("EOF")) {
//                        if (firstLine.equals("")) {
//                            firstLine = line;
//                        }
//                        System.out.println(line);
//                    }
//
//                    if (command.startsWith("get ") && !firstLine.startsWith("error")) {
//                        break;
//                    }
//                } else {
//                    System.err.println("Invalid command.");
//                }
//                out.flush();
//            }
//
//            out.close();
//            in.close();
//            st.close();
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//
//    }
//}
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
    public static void main(String[] args) {
        try {
            // Establishes a connection to the server's socket
            Socket socket = new Socket("localhost", 8889);

            // Output stream to send data to the server
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // Input stream to receive data from the server
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // Reads user input from the keyboard
            BufferedReader keyboardInput = new BufferedReader(new InputStreamReader(System.in));

            while (true) {
                System.out.print("client> ");
                String command = keyboardInput.readLine();

                // Checks if the command is valid
                if (command.equals("index") || command.startsWith("get ")) {
                    // Sends the command to the server
                    out.println(command);

                    String firstLine = "";
                    String line = "";

                    // Reads server response until encountering the end-of-file (EOF) marker
                    while (!(line = in.readLine()).equals("EOF")) {
                        if (firstLine.equals("")) {
                            firstLine = line; // Saves the content of the first line
                        }
                        System.out.println(line); // Prints each line of content
                    }

                    // If it's a command to get a file and no error occurred, exits the loop
                    if (command.startsWith("get ") && !firstLine.startsWith("error")) {
                        break;
                    }
                } else {
                    System.err.println("Invalid command.");
                }
                out.flush(); // Forces the output stream to flush and ensure data is sent
            }

            // Closes the connection
            out.close();
            in.close();
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
