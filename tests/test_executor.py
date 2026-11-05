import time
import pytest
from core.dag_executor import DAGExecutor

def mock_fast_task():
    time.sleep(0.1)

def test_concurrent_execution_speed():
    tasks = ['A', 'B', 'C', 'D']
    # A -> B, C -> D. So B and C can run concurrently after A.
    dependencies = {'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
    
    executor = DAGExecutor(tasks, dependencies)
    task_funcs = {t: mock_fast_task for t in tasks}
    
    start_time = time.time()
    executor.execute(task_funcs)
    duration = time.time() - start_time
    
    # If sequential, it takes 0.4s. If concurrent, it should take ~0.3s.
    assert duration < 0.35, f"Execution took {duration:.2f}s, expected concurrent speedup"

def test_dependency_order():
    execution_order = []
    
    def get_tracker(task_id):
        def tracker():
            execution_order.append(task_id)
        return tracker
        
    tasks = ['A', 'B', 'C']
    dependencies = {'B': ['A'], 'C': ['B']} # A -> B -> C
    
    executor = DAGExecutor(tasks, dependencies)
    task_funcs = {t: get_tracker(t) for t in tasks}
    
    executor.execute(task_funcs)
    assert execution_order == ['A', 'B', 'C']
