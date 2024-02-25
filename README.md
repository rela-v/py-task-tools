# py-task-tools 🚀
py-task-tools is a Python module designed to help you conquer your tasks and achieve maximum productivity. It provides a comprehensive set of tools for:

- Creating and managing tasks: Define tasks with descriptions, priorities, estimated time, deadlines, categories, tags, contexts, and subtasks.
- Prioritizing effectively: Focus on what matters most by prioritizing tasks based on urgency, importance, and dependencies.
- Tracking progress: Monitor the completion status of both main tasks and subtasks, gaining a clear picture of your overall progress.
- Managing dependencies: Ensure tasks are completed in the correct order by managing dependencies between them.
- Database flexibility: Connect to various database systems through an abstraction layer for easy data storage and retrieval.

## Features 🛠️

py-task-tools empowers you to:

- Organize your tasks efficiently: 📋 Keep track of everything you need to do in one place.
- Prioritize effectively: Focus on the most important tasks first and avoid procrastination.
- Break down complex tasks: Divide large tasks into smaller, manageable steps.
- Track progress visually: Monitor your progress and stay motivated.
- Adapt to your needs: ⚙️ Customize the system to fit your workflow and preferences.

## Installation 💻

```bash
pip install py-task-tools
```
## Usage 🚨
```python
from py-task-tools import Task, Database
import datetime

# Connect to your database
db = Database(connection_string="...")

# Create a new task
task = Task(
    description="Write blog post",
    priority="Urgent/Important",
    estimated_time=120,
    deadline=datetime.datetime(2024, 3, 1),
    category="Work",
    tags=["writing", "content creation"],
    context="Requires focus",
)

# Add subtasks
task.add_subtask("Research topic")
task.add_subtask("Write outline")

# Save the task to the database
db.save_task(task)

# ... (other functionalities)
```
For detailed documentation and examples, please refer to the full documentation available online.

## Contributing 🤝
We welcome contributions from the community! Feel free to fork the repository, make changes, and submit pull requests.

## License 📝
This project is licensed under the MIT License.
