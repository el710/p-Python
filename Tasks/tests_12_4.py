import logging
import unittest
import rt_with_exceptions as rwe

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        t_speed = -5
        t_name = "Axe"
        try:
            runner = rwe.Runner(t_name, t_speed)
            self.assertIsNotNone(runner)            
            runner.walk()
            logging.info(f"test walk() succesful: {t_name} - {t_speed} - {runner.distance}")
            self.assertNotEqual(runner.distance, 0)
        except ValueError:
            logging.warning(f"Wrong value: name: {t_name}, speed: {t_speed}", exc_info=True)

    
    def test_run(self):
        t_speed = 7
        t_name = 456        
        try:
            runner = rwe.Runner(t_name, t_speed)
            self.assertIsNotNone(runner)
            runner.run()
            logging.info(f"test run() successful: {t_name} - {t_speed} - {runner.distance}")
            self.assertNotEqual(runner.distance, 0)
        except TypeError:
            logging.warning(f"Wrong data type: name: {t_name}, speed: {t_speed}", exc_info=True)
        


if __name__ == "__main__":
    logging.basicConfig(filename="runner_test.log", filemode="w", format="\n %(asctime)s | %(module)s | %(levelname)s | %(message)s",
                        level=logging.INFO, encoding="utf-8")
    
    unittest.main()
    
