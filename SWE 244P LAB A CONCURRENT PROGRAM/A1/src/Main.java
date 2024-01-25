import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ThreadManager threadManager = new ThreadManager();
        threadManager.start();
    }

    static class ThreadManager {
        private List<PrintThread> threads = new ArrayList<>();
        private LocalTime startTime = LocalTime.now();
        private DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");

        public void start() {
            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("Here are your options:");
                System.out.println("a - Create a new thread");
                System.out.println("b - Stop a given thread (e.g. \"b 2\" kills thread 2)");
                System.out.println("c - Stop all threads and exit this program.");

                String option = scanner.nextLine();

                switch (option.toLowerCase()) {
                    case "a":
                        createNewThread();
                        break;
                    case "b":
                        stopThread(scanner.nextInt());
                        break;
                    case "c":
                        stopAllThreads();
                        System.exit(0);
                        break;
                    default:
                        System.out.println("Invalid option. Please try again.");
                }
            }
        }

        private void createNewThread() {
            PrintThread newThread = new PrintThread(startTime, formatter);
            threads.add(newThread);
            newThread.start();
        }

        private void stopThread(int threadId) {
            for (PrintThread thread : threads) {
                if (thread.getThreadId() == threadId) {
                    thread.stopThread();
                    threads.remove(thread);
                    return;
                }
            }
            System.out.println("Thread " + threadId + " not found.");
        }

        private void stopAllThreads() {
            for (PrintThread thread : threads) {
                thread.stopThread();
            }
            threads.clear();
        }
    }

    static class PrintThread extends Thread {
        private static int nextThreadId = 1;
        private int threadId;
        private volatile boolean isRunning = true;
        private LocalTime startTime;
        private DateTimeFormatter formatter;

        public PrintThread(LocalTime startTime, DateTimeFormatter formatter) {
            this.threadId = nextThreadId++;
            this.startTime = startTime;
            this.formatter = formatter;
        }

        @Override
        public void run() {
            while (isRunning) {
                LocalTime currentTime = LocalTime.now();
                String formattedTime = currentTime.format(formatter);
                System.out.println("Hello World! I'm thread " + threadId + ". The time is " + formattedTime);

                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        }

        public void stopThread() {
            isRunning = false;
        }

        public int getThreadId() {
            return threadId;
        }
    }
}
