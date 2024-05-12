class Task:
  def __init__(self, description, priority):
    self.description = description
    self.priority = priority

  def __repr__(self):
    return f"Task(description={self.description}, priority={self.priority})"

class TaskManager:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def remove_task(self, description):
    self.tasks = [task for task in self.tasks if task.description != description]

  def get_tasks_sorted_by_priority(self):
    return sorted(self.tasks, key=lambda x: x.priority)

  def __repr__(self):
    return f"TaskManager(tasks={self.tasks})"
