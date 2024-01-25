import java.util.concurrent.*;

public class Main3 {

    private static void nap(int millisecs) {
        try {
            Thread.sleep(millisecs);
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    private static void addProc(HighLevelDisplay d, Semaphore s) {

        // Add a sequence of addRow operations with short random naps.
        int i = 0;
        while (true) {
            try {
                s.acquire();
                d.addRow("AAAAAAAAAAAA  " + i);
                d.addRow("BBBBBBBBBBBB  " + i);
            } catch (InterruptedException e) {
                System.err.println(e.getMessage());
            } finally {
                s.release();
            }
            i++;
            nap(1000);
        }
    }

    private static void deleteProc(HighLevelDisplay d, Semaphore s) {

        // Add a sequence of deletions of row 0 with short random naps.
        while (true) {
            try {
                s.acquire();
                d.deleteRow(0);
            } catch (InterruptedException e) {
                System.err.println(e.getMessage());
            } finally {
                s.release();
            }
            nap(2500);
        }
    }

    public static void main(String[] args) {
        final HighLevelDisplay d = new JDisplay2();
        Semaphore s = new Semaphore(1);

        new Thread(() -> {
            try {
                addProc(d, s);
            } finally {
                s.release();
            }
        }).start();

        new Thread(() -> {
            try {
                deleteProc(d, s);
            } finally {
                s.release();
            }
        }).start();
    }
}