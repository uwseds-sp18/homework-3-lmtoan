import unittest
import homework3

# Define a class in which the tests will run
class HW3Test(unittest.TestCase):
    def test_column_names(self):
        df = homework3.create_dataframe('class.db')
        self.assertTrue(set(df.columns) == set(['video_id', 'category_id', 'language']))
                                       
    def test_min_nrows(self):
        df = homework3.create_dataframe('class.db')
        self.assertTrue(len(df) > 100)
     
    def test_keys(self):
    	df = homework3.create_dataframe('class.db')
    	self.assertTrue(len(df) == df.groupby(['video_id', 'language']))

    def test_invalid_path(self):
    	self.assertRaises(ValueError, homework3.create_dataframe, 'toan.db')

if __name__ == '__main__':
    unittest.main()