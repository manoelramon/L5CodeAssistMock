class DAGExecutor:
    def __init__(self, tasks, dependencies):
        self.tasks = tasks  # list of task IDs (strings)
        self.dependencies = dependencies  # dict of task_id -> list of dependency task_ids
        self.completed = set()

    def execute(self, task_funcs):
        '''
        Currently runs sequentially.
        Candidate task: Upgrade this to run concurrently using a thread pool or multiprocessing pool.
        '''
        # Naive sequential execution for the starter code
        for task in self.tasks:
            # We are ignoring dependencies in this naive starter implementation.
            task_funcs[task]()
            self.completed.add(task)
