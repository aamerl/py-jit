import time
import logging
from numba import jit
from numpy import float64, zeros, random
from numpy._typing import NDArray


def matrix_multiply(A: NDArray[float64], B: NDArray[float64]) -> NDArray[float64]:
    m, n = A.shape
    n, p = B.shape
    C = zeros((m, p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    return C


@jit(cache=True)
def matrix_multiply_numba(A: NDArray[float64], B: NDArray[float64]) -> NDArray[float64]:
    m, n = A.shape
    n, p = B.shape
    C = zeros((m, p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    return C


def setup_log():
    logger = logging.getLogger(name="jit")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    logger = setup_log()

    A = random.random((80, 90))  # (80*80)*(2*90 -1)
    B = random.random((90, 80))

    st = time.time()
    C = matrix_multiply(A, B)
    logger.info(f"python code execution time without numba: {time.time() - st}")

    st = time.time()
    C = matrix_multiply_numba(A, B)
    logger.info(f"python code execution time with numba: {time.time() - st}")
