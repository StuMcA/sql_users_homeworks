import pdb
from models.task import Task
import repositories.task_repository as task_repository
from models.user import User
import repositories.user_repository as user_repository

task_repository.delete_all()
user_repository.delete_all()

user_1 = User("Jack", "Jarvis")
user_2 = User("Victor", "McDade")
task_1 = Task("Walk Dog", user_1, 60)
task_2 = Task("Feed Cat", user_2, 5)

user_repository.save(user_1)
user_repository.save(user_2)

task_repository.save(task_1)
task_repository.save(task_2)

task_1.mark_complete()
task_repository.update(task_1)

pdb.set_trace()
