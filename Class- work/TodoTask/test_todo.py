import unittest

import todo


class MyTestCase(unittest.TestCase):
    def test_tasks_can_be_added(self):
        todo.tasks = []  # Reset tasks before each test
        self.assertEqual(todo.add_task("will go and playfootball"), "tasks added successfully")
        self.assertEqual(todo.add_task("buy foodstuff"), "tasks added successfully")






if __name__ == '__main__':
    unittest.main()
