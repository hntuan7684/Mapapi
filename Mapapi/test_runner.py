import coverage
from django.test.runner import DiscoverRunner

class CoverageRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.coverage = coverage.Coverage(
            source=['Mapapi'],  # adjust this to include all your app directories
            omit=['*/tests/*', '*/migrations/*'],
            data_file='/app/coverage/.coverage',
        )

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        self.coverage.start()
        result = super().run_tests(test_labels, extra_tests, **kwargs)
        self.coverage.stop()
        self.coverage.save()
        self.coverage.xml_report(outfile='/app/coverage/coverage.xml')
        return result

CoverageRunner  