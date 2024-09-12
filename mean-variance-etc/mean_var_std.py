import numpy as np

def calculate(numbers_list: list) -> dict:
    """
    Perform calculations on a 3x3 matrix, including mean, variance, standard deviation,
    max, min, and sum for rows, columns, and elements.

    Args:
        matrix (list): A 3x3 matrix represented as a list of lists.

    Returns:
        dict: A dictionary containing the mean, variance, standard deviation, 
              max, min, and sum for rows, columns, and elements.
    """
    if len(numbers_list) != 9:
        raise ValueError('List must contain nine numbers.')

    matrix = np.array(numbers_list).reshape(3, 3)  # convert list to array
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }
    
    return calculations