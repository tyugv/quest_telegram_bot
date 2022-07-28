class Task:
    def __init__(self, is_photo: str, text: str, result: str, password: list):
        self.photo = is_photo
        self.text = text
        self.result = result
        self.password = password


class Quest:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.current_task = None
        self.current_task_num = -1
        self.tasks = self.make_tasks()
        self.update_task()
        self.is_done = False

    def make_tasks(self):
        tasks = []
        with open(self.file_path) as f:
            for line in f.readlines():
                line = line.strip().split(';')
                tasks.append(Task(is_photo=line[0], text=line[1], result=line[2], password=line[3:]))
        return tasks

    def update_task(self):
        self.current_task_num += 1
        if self.current_task_num < len(self.tasks):
            self.current_task = self.tasks[self.current_task_num]
        else:
            self.is_done = True

    def print_task(self):
        return self.current_task.text

    def check_password(self, password):
        if password.lower() in self.current_task.password:
            result = self.current_task.result
            self.update_task()
            return True, result

        else:
            return False, f'Answer "{password.lower()}" is wrong'
