# py-task-tools Tests 🧪

This folder contains a comprehensive suite of tests for the py-task-tools Python module. The tests are organized into specific categories to cover various functionalities as outlined in the module's README.md.

## Test Files

1. **task_management_database_tests.py:**
   - Tests for creating tasks with various attributes and ensuring they are stored correctly in the database.
   - Retrieve tasks from the database and validate that the stored information matches the original input.

2. **prioritization_dependency_tests.py:**
   - Tests for prioritizing tasks based on urgency, importance, and dependencies.
   - Verify that tasks with dependencies are completed in the correct order.

3. **visual_progress_tests.py:**
   - Tests for monitoring the completion status of tasks and subtasks.
   - Validate the visual progress tracking feature to ensure it accurately reflects overall progress.

4. **efficiency_organization_prioritizaiton_tests.py:**
   - Integration tests covering the efficient organization of tasks and effective prioritization.
   - Check that tasks are listed and prioritized according to user input.

5. **task_breakdown_customization_tests.py:**
   - Tests for breaking down large tasks into smaller, manageable steps.
   - Verify customization features to ensure the system can be adapted to different workflows and preferences.

6. **integration_tests.py:**
   - End-to-end scenarios involving multiple functionalities to ensure seamless interaction.
   - Covers scenarios where tasks with dependencies are organized, prioritized, and tracked visually.

## Running the Tests

To run the tests, execute the following command in your terminal:

```bash
python -m unittest discover -s tests -p '*_tests.py'
```
