import numpy.linalg as la

# Judge element for SL(2, Z)
def judge_sl2Z(matrix):
    # Define Determinant for ∈ SL(2, Z)
    SL2Z_DET = 1

    if(int(matrix[0,0] * matrix[1, 1] - matrix[0,1] * matrix[1,0]) == SL2Z_DET):
        return True
    else:
        return False