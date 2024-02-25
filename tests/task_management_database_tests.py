# Test file for all things task CRUD and database-related.
from src.task_management_database.py import Task, Database

class TaskManagementDatabaseTests(unittest.TestCase):
    def setUp(self):
        # Add a database connection
        self.db = Database(connection_string="test_db_connection_string")

    def tearDown(self):
        # Clean up any resources or database entries after each test - implies clear_database method.
        self.db.clear_database()

    def test_create_task():
        # Test creating a task with various attributes
        task = Task(
            description="Write blog post",
            priority="Urgent/Important",
            estimated_time=120,
            deadline="2024-03-01",
            category="Work",
            tags=["writing", "content creation"],
            context="Requires focus",
        )
        self.db.save_task(task)

        # Retrieve the task from the database
        retrieved_task = self.db.get_task(task.id)

        # Validate that the retrieved task matches the original input
        self.assertEqual(task.to_dict(), retrieved_task.to_dict())

    def test_retrieve_task_list():
        # Test retrieving a list of tasks from the database
        tasks = [
            Task(description="Task 1", priority="High"),
            Task(description="Task 2", priority="Medium"),
            Task(description="Task 3", priority="Low"),
        ]

        # Save tasks to the database
        for task in tasks:
            self.db.save_task(task)

        # Retrieve the list of tasks from the database
        retrieved_tasks = self.db.get_all_tasks()

        # Validate that the retrieved list matches the original input
        self.assertEqual(len(retrieved_tasks), len(tasks))
        self.assertCountEqual([task.to_dict() for task in tasks], [task.to_dict() for task in retrieved_tasks])

    def test_update_task():
        # Test updating a task in the database
        original_task = Task(description="Original Task", priority="Low")
        self.db.save_task(original_task)

        # Update the task
        updated_task = Task(
            id=original_task.id,
            description="Updated Task",
            priority="High",
            estimated_time=60,
        )
        self.db.update_task(updated_task)

        # Retrieve the updated task from the database
        retrieved_task = self.db.get_task(original_task.id)

        # Validate that the retrieved task matches the updated input
        self.assertEqual(updated_task.to_dict(), retrieved_task.to_dict())

    def test_delete_task():
        # Test deleting a task from the database
        task_to_delete = Task(description="Task to Delete", priority="Medium")
        self.db.save_task(task_to_delete)

        # Delete the task
        self.db.delete_task(task_to_delete.id)

        # Try to retrieve the deleted task from the database
        retrieved_task = self.db.get_task(task_to_delete.id)

        # Validate that the retrieved task is None (indicating deletion)
        self.assertIsNone(retrieved_task)

    def test_task_performance():
        # Test the performance of saving and retrieving a large number of tasks
        num_tasks = 1000

        for i in range(num_tasks):
            task = Task(description=f"Task {i}", priority="Medium")
            self.db.save_task(task)

        # Retrieve all tasks and measure performance
        with self.assertMaxTime(2):  # Set a maximum time for the operation
            retrieved_tasks = self.db.get_all_tasks()

        # Validate that the number of retrieved tasks matches the expected count
        self.assertEqual(len(retrieved_tasks), num_tasks)

    def test_integration_with_external_systems():
        pass
