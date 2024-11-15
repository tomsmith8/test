# test_todo.py

import unittest
from todo import Todo

class TestTodo(unittest.TestCase):

    def setUp(self):
        self.todo = Todo()

    def test_add_task(self):
        # Test adding a valid task
        result = self.todo.add_task("Buy milk")
        self.assertIn("Task 'Buy milk' added.", result)
        self.assertIn("Buy milk", self.todo.get_tasks())

    def test_add_empty_task(self):
        # Test adding an empty task, should raise ValueError
        with self.assertRaises(ValueError):
            self.todo.add_task("")

if __name__ == "__main__":
    unittest.main()
