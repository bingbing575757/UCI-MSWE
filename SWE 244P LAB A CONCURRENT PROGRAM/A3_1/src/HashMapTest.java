import java.util.HashMap;
import java.util.Vector;

public class HashMapTest {

    private boolean running = true;
    private HashMap<String, Integer> people = new HashMap<>();

    private synchronized void addPerson() {
        people.put(RandomUtils.randomString(), RandomUtils.randomInteger());
    }

    private synchronized void deletePeople(String pattern) {
        Vector<String> hasPattern = new Vector<>();
        for (String key : people.keySet()) {
            if (key.contains(pattern))
                hasPattern.add(key);
        }
        for (String key : hasPattern)
            people.remove(key);
    }

    private synchronized void printPeople() {
        for (HashMap.Entry<String, Integer> entry : people.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        System.out.println("-----------------------------------------");
    }

    public void run() {
        // Start printer thread
        new Thread(new Runnable() {
            public void run() {
                Thread.currentThread().setName("Printer");
                while (running) {
                    printPeople();
                    try {
                        Thread.sleep(200);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();

        // Start deleter thread
        new Thread(new Runnable() {
            public void run() {
                Thread.currentThread().setName("Deleter");
                while (running) {
                    deletePeople("a");
                    try {
                        Thread.sleep(200);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();

        // This thread adds entries
        for (int i = 0; i < 100; i++) {
            addPerson();
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        running = false;
    }

    public static void main(String[] args) {
        HashMapTest hm = new HashMapTest();
        hm.run();
    }
}