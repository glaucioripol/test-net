"""Runner"""
from persist_handlers import PersistOnSqlite
from speed_test_runner import SpeedTestRunner


SpeedTestRunner(PersistOnSqlite()).run()
