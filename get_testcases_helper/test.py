import mock
import os
from unittest import TestCase, expectedFailure

from get_testcases import run, read_file, get_units


def examples_folder_path():
    dirname = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dirname, 'test_examples')


class TestReadFile(TestCase):

    def test_its_called_with_run_first_argument(self):
        argv = ['command_name', 'something', 'someotherthing']
        with mock.patch('get_testcases_helper.get_testcases.read_file') as mock_f_reader:
            mock_f_reader.return_value = None
            run(argv)
        mock_f_reader.assert_called_once_with(argv[1])

    def test_if_file_exists_returns_its_content(self):
        existent_fname = os.path.join(examples_folder_path(), 'test_something.py')
        data = read_file(existent_fname)
        self.assertEqual(data, file(existent_fname).read())

    def test_py_extension_is_appended(self):
        existent_fname = os.path.join(examples_folder_path(), 'test_something')
        data = read_file(existent_fname)
        self.assertEqual(data, file(existent_fname + '.py').read())

    def test_if_file_not_found_returns_None(self):
        existent_fname = os.path.join(examples_folder_path(), 'nothing.py')
        data = read_file(existent_fname)
        self.assertEqual(data, None)


_sample_data = """
from unittest import TestCase
class TestA(TestCase):
    pass
class TestB(TestCase):
    def test_b1(self):
        pass
    def test_b2(self):
        pass
    def test_something_else(self):
        pass
class TestC(TestB):
    def test_a1(self):
        pass
"""


class TestListedCases(TestCase):

    def setUp(self):
        self.sample_data = _sample_data
        self.argv = ['command', 'dummy_filename.py']
        patcher = mock.patch('get_testcases_helper.get_testcases.read_file')
        self.read_patcher = patcher.start()
        self.read_patcher.return_value = _sample_data
        self.addCleanup(patcher.stop)

    def test_classes_listed(self):
        opts = run(self.argv)
        self.assertEqual(set(['TestA', 'TestB', 'TestC']), set(opts))

    def test_units_are_listed(self):
        argv = self.argv[:]
        argv.append('--units=TestB.')
        opts = run(argv)
        self.assertEqual(set(['TestB.test_b1',
                              'TestB.test_b2',
                              'TestB.test_something_else']), set(opts))

    def test_units_are_parcially_listed(self):
        argv = self.argv[:]
        argv.append('--units=TestB.test_b')
        opts = run(argv)
        self.assertEqual(set(['TestB.test_b1',
                              'TestB.test_b2']), set(opts))

    def test_empty_units_are_listed(self):
        argv = self.argv[:]
        argv.append('--units=TestA.')
        opts = run(argv)
        self.assertEqual([], opts)

    @expectedFailure
    def test_inherited_units_are_listed_too(self):
        argv = self.argv[:]
        argv.append('--units=TestC.')
        opts = run(argv)
        self.assertIn('TestC.test_b1', set(opts))
