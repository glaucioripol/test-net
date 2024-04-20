"""It's responsible to run get the speed test and persist in some place"""
from  subprocess import run
from persist_handlers import PersistSpeedTestResult

class SpeedTestRunner:
    """It's responsible to run get the speed test and persist in some place"""
    def __init__(self, persister: PersistSpeedTestResult):
        self._command_parameters = {
            'args': ['speedtest-cli', '--json'],
            'capture_output': True,
            'text': True,
        }

        self.persist_handler = persister

    def run(self):
        """Run the speed test and persist"""
        result = self._get_results()
        self.persist_handler.persist(result)
        print('Finished')


    def _get_results(self) -> str:
        """Run the speed test cli and retrieve the json output"""
        result = run(
            **self._command_parameters,
            check=False # !note: to avoid fail silently
        ).stdout

        return result
