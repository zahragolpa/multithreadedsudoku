import numpy as np
import threading
import time


# global variable
result = True
threadTime = time.time()


class MatrixSolution:
    def __init__(self, solution_matrix):
        if np.shape(solution_matrix) != (9, 9):
            print('Matrix is not square. Please try again.')
            exit()
        self.number_of_rows = np.shape(solution_matrix)[0]
        self.number_of_columns = np.shape(solution_matrix)[1]
        self.solution_matrix = solution_matrix
        self.rows = self.get_rows()
        self.cols = self.get_cols()
        self.blocks = self.get_blocks()
        self.check_numbers_driver()


    def check_numbers_driver(self):
        t_row = []
        t_col = []
        t_block = []
        # check rows
        for rows in self.rows:
            if not result:
                break
            t_row = threading.Thread(target=self.check_numbers, args=(rows,))
            t_row.start()
            t_row.join()

        # check columns
        for cols in self.cols:
            if not result:
                break
            t_col = threading.Thread(target=self.check_numbers, args=(cols,))
            t_col.start()
            t_col.join()

        # check blocks
        block_line = []
        for blocks in self.blocks:
            block_line.append(np.reshape(blocks, (1, 9))[0])
        for line in block_line:
            if not result:
                break
            t_block.append(threading.Thread(target=self.check_numbers, args=(line,)))
        if result:    
            for i in t_block:
                i.start()
            for i in t_block:
                i.join()

        if result == True:
            print('The provided solution is correct.')
            
        else:
            print('Solution is not valid.')


    def get_rows(self):
        matrix_rows = []
        for rows in self.solution_matrix:
            matrix_rows.append(rows)
        return matrix_rows

    def get_cols(self):
        matrix_cols = []
        for i in range(self.number_of_rows):
            matrix_cols.append([row[i] for row in self.solution_matrix])
        return matrix_cols

    def get_blocks(self):
        matrix_blocks = []
        for i in range(0, 3):
            j = 0
            i *= 3
            for j in range(0, 3):
                j *= 3
                matrix_blocks.append(self.solution_matrix[i:i + 3, j:j + 3])
        return matrix_blocks

    
    def check_numbers(self, row):
        global result
        validator = [False] * len(row)
        for elements in row:
            if not (0 < elements < 10):
                result = False
                return False
            if validator[elements - 1] == True:
                result = False
                return False
            validator[elements - 1] = True
        return True


data_matrix = MatrixSolution(np.array ([[8,3,5,4,1,6,9,2,7],
            [2,9,6,8,5,7,4,3,1],
            [4,1,7,2,9,3,6,5,8],
            [5,6,9,1,3,4,7,8,2],
            [1,2,3,6,7,8,5,4,9],
            [7,4,8,5,2,9,1,6,3],
            [6,5,2,7,8,1,3,9,4],
            [9,8,1,3,4,5,2,7,6],
            [3,7,4,9,6,2,8,1,5]]))

print("time consumed with 11 threads: " + str(time.time() - threadTime))


# valid solution backup       

# data_matrix = MatrixSolution(np.array ([[8,3,5,4,1,6,9,2,7],
#             [2,9,6,8,5,7,4,3,1],
#             [4,1,7,2,9,3,6,5,8],
#             [5,6,9,1,3,4,7,8,2],
#             [1,2,3,6,7,8,5,4,9],
#             [7,4,8,5,2,9,1,6,3],
#             [6,5,2,7,8,1,3,9,4],
#             [9,8,1,3,4,5,2,7,6],
#             [3,7,4,9,6,2,8,1,5]]))


