from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List
from core.dag_executor import DAGExecutor
from models.inference import mock_inference

router = APIRouter()

class InferenceRequest(BaseModel):
    tasks: List[str]
    dependencies: Dict[str, List[str]]

@router.post("/run-pipeline")
def run_pipeline(request: InferenceRequest):
    # TODO for candidate: Use the AI assistant to upgrade DAGExecutor to run 
    # tasks concurrently rather than sequentially.
    
    executor = DAGExecutor(request.tasks, request.dependencies)
    
    # Map tasks to our mock inference workload
    task_funcs = {task: mock_inference for task in request.tasks}
    
    executor.execute(task_funcs)
    
    return {"status": "success", "executed_tasks": request.tasks}
