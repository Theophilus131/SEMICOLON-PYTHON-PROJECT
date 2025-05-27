import unittest

import to_do_list_manager

class TestStore(unittest.TestCase):

	def test_that_to_do_list_manager_function_exist(self):
		to_do_list_manager.main_menu()

	def test_that_add_task_function_works(self):
		to_do_list_manager.add_a_task_menu()

	def test_that_mark_a_task_function_works(self):
		to_do_list_manager.mark_a_task_as_complete_menu()

	def test_that_delete_a_task_function_works(self):
		to_do_list_manager.delete_a_task_menu() 


		
		
	
	
