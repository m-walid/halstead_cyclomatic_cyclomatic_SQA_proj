public class Main {
  public static void main(String args[]) {
    int num1 = 10;
    int num2 = 20;
    boolean flag = true;
    int[] arr = new int[10];
    for (int i = 0; i < 10; i++) {
      if (i % 2 == 0) {
        arr[i] = i * num1;
      } else {
        arr[i] = i * num2;
      }
    }
    if (flag == true) {
      num2 = num1 * num2;
    }
  }
}


