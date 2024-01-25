public class TrafficController {
    private Integer onBright = 0;


    public void enterLeft() {
        synchronized (this) {
            while (onBright != 0) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            onBright++;
            notifyAll();

        }

    }

    public void enterRight() {
        synchronized (this) {
            while (onBright != 0) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            onBright++;
            notifyAll();

        }
    }

    public void leaveLeft() {
        synchronized (this) {
            onBright--;
            notifyAll();
        }
    }

    public void leaveRight() {
        synchronized (this) {
            onBright--;
            notifyAll();
        }

    }

}
