import time
import torch

def mock_inference():
    '''
    Simulates a heavy PyTorch model inference.
    Takes ~1 second and uses tensor operations to simulate a real ML workload.
    '''
    # Simulate CPU/GPU bound work
    tensor_a = torch.randn(2000, 2000)
    tensor_b = torch.randn(2000, 2000)
    
    # Matrix multiplication to simulate heavy workload
    result = torch.matmul(tensor_a, tensor_b)
    
    # Sleep to simulate network/IO delay of fetching the model or weights
    time.sleep(1)
    
    return result
