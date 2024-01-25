import java.io.IOException;
import java.io.RandomAccessFile;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.file.DirectoryStream;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Server_UDP {
    private static DatagramSocket st = null;
    private static String folderPathString = "";
    private static Path folderPath = null;
    private static class Task implements Callable<Void> {

        private DatagramPacket packet;
        private byte[] buf;
        private byte[] signBuf;
        private RandomAccessFile file;
        private String adress;

        Task(DatagramPacket packet, byte[] buf) {
            this.packet = packet;
            this.buf = buf;
            this.signBuf = new byte[4];
            this.adress = this.packet.getAddress().getHostAddress() + ":" + this.packet.getPort();
        }

        @Override
        public Void call() throws Exception {
            Thread.currentThread().setPriority(10);

            try {
                String command = new String(buf);
                command = command.replace("\0", "");
                System.out.println("Command received: " + command + " from " + adress);
                // When the command is 'index'.
                if (command.equals("index")) {
                    StringBuilder sb = new StringBuilder();
                    sb.append("Folder Path: " + folderPath.toAbsolutePath().toString() + "\n");
                    try (DirectoryStream<Path> stream = Files.newDirectoryStream(folderPath)) {
                        // Open a directory stream using try-with-resources to iterate through the files in the folder
                        // DirectoryStream interface allows iterating over files and directories, using Path to represent file paths
                        // This will automatically close the file stream at the end of the block
                        for (Path p : stream) {
                            // Iterate through each file (Path object) in the folder
                            sb.append(p.getFileName() + "\n");
                        }
                        String message = sb.toString();
                        System.out.print(message);
                        packet.setData(message.getBytes(), 0, message.getBytes().length);
                        // Send out the data through the socket.
                        st.send(packet);

                    } catch (IOException e) {
                        System.err.println("Invalid folder path.");
                        e.printStackTrace();
                    }
                } else if (command.startsWith("get ")) {
                    String filePathString = command.split(" ")[1];
                    // Create the path of the file requested.
                    Path filePath = Paths.get(folderPathString + "/" + filePathString);
                    if (Files.notExists(filePath)) {
                        // If not exist, send error.
                        packet.setData("error\nInvalid file name.".getBytes(), 0,
                                "error\nInvalid file name.".getBytes().length);
                        st.send(packet);
                        System.err.println("Invalid file name.");
                    } else {
                        file = new RandomAccessFile(folderPathString + "/" + filePathString, "r");
                        // Initialize packet counter.
                        int packetCount = 1;
                        // Initialize receive size.
                        int receiveSize = -1;

                        // Read data from the file into the buffer, return the actual number of bytes read until the end of file.
                        while ((receiveSize = file.read(buf)) != -1) {
                            // Set the data from the buffer into the datagram packet
                            packet.setData(buf, 0, receiveSize);
                            // Send the datagram packet using DatagramSocket
                            st.send(packet);
                            // Wait for successful response
                            while (true) {
                                // Set the data buffer for the packet.
                                packet.setData(signBuf, 0, signBuf.length);
                                st.receive(packet);
                                String reply = new String(signBuf);
                                reply = reply.replace("\0", "");
                                // Check if the received reply is "succ"; if so, exit the loop; otherwise, resend the packet.
                                if (reply.equals("succ")) {
                                    break;
                                } else {
                                    System.out.println("resent packet " + packetCount);
                                    packet.setData(buf, 0, receiveSize);
                                    st.send(packet);
                                }
                            }
                            System.out.println("The No." + (packetCount++) + " packets sent successfully.");
                        }
                        // Send exit sign. The logic is similar to sending packages.
                        while (true) {
                            System.out.println("Send exit sign");
                            packet.setData("exit".getBytes(), 0, "exit".getBytes().length);
                            st.send(packet);

                            packet.setData(signBuf, 0, signBuf.length);
                            st.receive(packet);
                            // exit
                            String reply = new String(signBuf);
                            reply = reply.replace("\0", "");

                            if (reply.equals("exit")) {
                                break;
                            } else {
                                System.out.println("Resent exit sign");
                                packet.setData("exit".getBytes(), 0, "exit".getBytes().length);
                                st.send(packet);
                            }
                        }

                    }
                } else {
                    packet.setData("error\nInvalid file name.".getBytes(), 0,
                            "error\nInvalid file name.".getBytes().length);
                    st.send(packet);
                    System.err.println("Invalid command.");
                }

            } catch (Exception e) {
                e.printStackTrace();
            }
            return null;
        }
    }

    public static void main(String[] args) {

        folderPathString = "E:\\1Programming Language\\dir";
        folderPath = Paths.get(folderPathString);
        //Check whether is a valid folder path.
        if (!Files.isDirectory(folderPath)) {
            System.err.println("Invalid folder path.");
            return;
        }
        // Create a thread pool for concurrent handling of client requests
        ExecutorService pool = Executors.newFixedThreadPool(50);

        try {
            // Create UDP server socket
            InetAddress inetAd = InetAddress.getByName(Constants_UDP.ADRESS);
            st = new DatagramSocket(Constants_UDP.PORT, inetAd);
            System.out.println("Socket at port " + st.getLocalPort());
            // Timeout exception thrown if no data is received within the specified time.
            st.setSoTimeout(Constants_UDP.TIMEOUT);

            while (true) {
                try {
                    // Creating a byte array to store incoming data.
                    byte[] buf = new byte[Constants_UDP.BUFFER_SIZE];
                    // Creating a DatagramPacket to receive the incoming data.
                    DatagramPacket packet = new DatagramPacket(buf, Constants_UDP.BUFFER_SIZE);
                    // Pausing execution for 2 seconds (this might be for timing purposes or delay).
                    Thread.sleep(2000);
                    st.receive(packet);
                    String command = new String(buf);
                    command = command.replace("\0", "");
                    System.out.println(command);
                    if (command.equals("index") || command.startsWith("get ")) {
                        System.out.println("Packet received from " + packet.getAddress().getHostAddress() + ":"
                                + packet.getPort());
                        // Submitting the received packet and data to a thread pool.
                        pool.submit(new Task(packet, buf));
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (st != null) {
                    st.close();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}