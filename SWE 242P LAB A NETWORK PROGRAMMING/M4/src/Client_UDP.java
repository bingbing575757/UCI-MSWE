import java.io.*;
import java.net.*;


public class Client_UDP {

    public static void main(String[] args) {
        DatagramSocket st = null;
        try {
            byte[] buf = new byte[Constants_UDP.BUFFER_SIZE];
            InetAddress inetAd = InetAddress.getByName(Constants_UDP.ADRESS);

            // Create DatagramSocket, let the operating system generate the port number
            st = new DatagramSocket();
            System.out.println("Socket at port " + st.getLocalPort());
            st.setSoTimeout(Constants_UDP.TIMEOUT);// Set timeout duration
            DatagramPacket packet = new DatagramPacket(buf, Constants_UDP.BUFFER_SIZE, inetAd, Constants_UDP.PORT);
            // Create a BufferedReader object to read input from the standard input stream (keyboard).
            BufferedReader keyboardIn = new BufferedReader(new InputStreamReader(System.in));

            while (true) {
                System.out.print("client> ");
                String command = keyboardIn.readLine();
                if (command.equals("index") || command.startsWith("get ")) {
                    // Send command to the server
                    packet.setData(command.getBytes(), 0, command.getBytes().length);
                    st.send(packet);
                    // Receive response from the server
                    packet.setData(buf, 0, buf.length);
                    st.receive(packet);
                    int packetCount = 1;
                    int receiveSize = 0;
                    StringBuilder sb = new StringBuilder();
                    // Process the response for 'index' command
                    if (command.equals("index")) {
                        String reply = new String(buf);
                        reply = reply.replace("\0", "");
                        sb.append(reply);
                    } else {
                        while ((receiveSize = packet.getLength()) != 0) {
                            String reply = new String(buf);
                            reply = reply.replace("\0", "");
                            // Exit loop if 'exit' signal is received
                            if (reply.equals("exit")) {
                                System.out.println("End");
                                packet.setData("exit".getBytes(), 0, "exit".getBytes().length);
                                st.send(packet);
                                break;
                            }
                            sb.append(reply);
                            // Send success signal back to the server
                            packet.setData("succ".getBytes(), 0, "succ".getBytes().length);
                            st.send(packet);
                            // Prepare to receive the next packet
                            buf = new byte[Constants_UDP.BUFFER_SIZE];
                            packet.setData(buf, 0, buf.length);
                            System.out.println("The No." + (packetCount++) + " packets received successfully.");
                            st.receive(packet);
                        }
                    }
                    sb.append("\n");
                    String res = sb.toString();
                    System.out.print(res);
                    // If it's a 'get' command and there's no error, break the loop
                    if (command.startsWith("get ") && !res.startsWith("error")) {
                        break;
                    }
                } else {
                    System.err.println("Invalid command.");
                }
            }
        } catch (ConnectException e) {
            System.err.println("Timeout.");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (st != null)
                    st.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
