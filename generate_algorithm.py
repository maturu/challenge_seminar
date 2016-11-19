import sys
import numpy as np
import numpy.linalg as la

class Generate:
    # Constructor
    def __init__(self):
        # target
        self.target = np.eye(2)
        # result
        self.result = np.eye(2)
        # Define Seeds
        self.SIGMA = np.array([[1, 1], [0, 1]])
        self.OMEGA = np.array([[0, 1], [-1, 0]])
        # Inverse element
        self.sigma_inv_element = []
        self.omega_inv_element = []

    # Method

    # Getter
    def get_target(self):
        return self.target
    # Setter
    def set_target(self, target):
        self.target = target
    # Search
    def proof(self):
        if self.target[0, 0] == 0:
            POW = 1
            result = la.matrix_power(self.OMEGA, POW).dot(self.target)
            self.omega_inv_element.append(-1 * POW)
        elif self.target[1, 0] == 0:
            result = self.target
        else:
            result = self.search_loop()


    def search_loop(self):
        target_calc = self.target
        while True:
            print(target_calc)
            target_calc = self.search_algorithm(target_calc)
            if target_calc[(1, 0)] == 0:
                return target_calc

    # if Part a * Part c != 0
    def search_algorithm(self, target_calc):
        # if |Part a| < |Part c|
        if np.fabs(target_calc[(0, 0)]) < np.fabs(target_calc[(1, 0)]):
            # ω・target_calc
            target_calc = self.OMEGA.dot(target_calc)

        # Part a // Part c, Part a % Part c
        division = self.euclidean_division(target_calc[0, 0], target_calc[1, 0])

        # ω・σ^(-quotient)・target_calc
        target_calc = self.OMEGA.dot(la.matrix_power(self.SIGMA, -1 * division["quotient"]).dot(target_calc))

        return target_calc

    # calced by euclidean_division
    def euclidean_division(self, dividend, divisor):
        # calc division
        quotient = int(dividend) // int(divisor)
        # calc remainder
        remainder =  dividend - quotient * divisor

        if remainder < 0:
            # calc remainder
            remainder_inc =  dividend - (quotient + 1) * divisor
            remainder_dec =  dividend - (quotient - 1) * divisor

            if remainder_inc >= 0:
                quotient += 1
                remainder = remainder_inc
            else:
                quotient -= 1
                remainder = remainder_dec

        return {"quotient": int(quotient),
                "remainder": int(remainder)}

def main():
    # Define Determinant for ∈ SL(2, Z)
    SL2Z_DET = 1
    # Constract 2 x 2 Identity Matrix
    target = np.eye(2)

    # Input to target
    print("Please set Part a:")
    target[(0, 0)] = float(input())
    print("Please set Part b:")
    target[(0, 1)] = float(input())
    print("Please set Part c:")
    target[(1, 0)] = float(input())
    print("Please set Part d:")
    target[(1, 1)] = float(input())

    # Judge element for SL(2. Z)
    if(int(la.det(target)) == SL2Z_DET):
        print(target)
    else:
        raise ValueError("Input Matrix is not element for SL(2, Z)")

    # Create Instance
    gen = Generate()
    gen.set_target(target)

    # Run Search and Print Result
    gen.proof()
    print(gen.result)

if __name__ == '__main__':
    main()
