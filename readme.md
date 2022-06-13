# Halstead complexity & Cyclomatic complexity Calculator for Java code

calculates Halstead and cyclomatix complexity of Java code.

## Prerequisites

You have to do the following before running the script:
* Install Python 3
* download main.py, requirements.txt and sample.java
* Install Dependencies

    ```bash
    python -m venv venv
    venv/Scripts/pip install install -r requirements.txt
    ```

## Usage

1. run
    ```bash
    venv/Scripts/python main.py
    ```
2. Enter the Java file path for example: (relative or absolute path)

## Java input file example

```java
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
```

## Output example
```
Operators:

 public  |  2
 class   |  1
 {       |  6
 static  |  1
 void    |  1
 (       |  4
 [       |  5
 ]       |  5
 )       |  4
 int     |  5
 =       |  8
 ;       |  9
 boolean |  1
 new     |  1
 for     |  1
 <       |  1
 ++      |  1
 if      |  2
 %       |  1
 ==      |  2
 *       |  3
 }       |  6
 else    |  1

--------------------


Operands:

 Main   |  1
 main   |  1
 String |  1
 args   |  1
 num1   |  3
 10     |  3
 num2   |  4
 20     |  1
 flag   |  2
 true   |  2
 arr    |  3
 i      |  8
 0      |  2
 2      |  1

--------------------

Operators n1:  23
Operators N1:  71
Operands n2:  14
Operands N2:  33

--------------------

Halstead complexity:

 Program length           |  104
 Program vocabulary       |  37
 Estimated length         |  157.345
 Purity ratio             |  1.513
 Volume                   |  819.681
 Difficulty               |  27.107
 Program effort           |  22219.207
 Time required to program |  1234.4
 Number of delivered bugs |  0.273

--------------------

Cyclomatic complexity:  4

--------------------
