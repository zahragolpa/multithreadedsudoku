# multithreadedsudoku
In this project, three approaches to solve a sudoku puzzle are implemented.

- Solving sudoku using a single thread.
- Solving sudoku using 11 threads; 1 thread for all the rows, 1 thread for all the columns, and 9 threads for 9 sudoku blocks.
- Solving sudoku using 27 threads; 9 thread for 9 rows, 9 thread for 9 columns, and 9 threads for 9 sudoku blocks.

We show that the more threads used, the more the running time will be. This unusual result is a consequence of context switch overhead. In compute-bound operations, unlike I/O-bound operations, multithreading may even increase the latency. The [Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law) also supports this claim.

Figure 1 and 2 shows latency over the number of threads when the given answer is correct and incorrect, respectively.

<img width="600" src="https://imgur.com/MPOXuRW.png"></img>

Figure 1. Latency over the number of threads when the given sudoku is correct.


<img width="600" src="https://imgur.com/SHguFVL.png"></img>

Figure 2. Latency over the number of threads when the given sudoku is not correct.


