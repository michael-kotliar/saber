import unittest
from conduit.utils.cwlparser import CwlParser

class TestCwlParser(unittest.TestCase):
    def setUp(self):
        pass
    def test_resolve_tools(self):
        # Test cases:
        # 1. Single tool
        # 2. Multiple tools
        # 3. Workflow CWL not in current directory
        pass
    def test_generate_volume_list(self):
        # Test cases:
        # 1. Test no outputs
        # 2. Single output
        # 3. Multiple output
        # 4. Empty local path
        pass
    def test_create_job_definitions(self):
        # Test cases:
        # 1. Single tool
        # 2. Multiple tools
        # 3. Workflow CWL not in current directory
        pass
    def test_build_docker_images(self):
        # Test cases:
        # 1. Single tool
        # 2. Multiple tools
        # 3. Multiple tools using same image
        pass
    def test_create_subdag(self):
        # Test cases:
        # 1. Single tool
        # 2. Multiple tools
        # 3. No iterations
        # 4. Multiple iterations
        # 5. Empty update dict

        pass

    def test_generate_dag(self):
        # Test cases:
        # 1. Single tool
        # 2. Multiple tools
        # 3. No iterations
        # 4. Multiple iterations
        # 5. Empty update dict
        # 6. Subdag = False
        pass
    def test_resolve_args(self):
        # Test cases:
        # 1. Single tool
        # 2. Multiple tools
        # 3. No iterations
        # 4. Multiple iterations
        # 5. Empty update dict
        pass
    def test_resolve_dependencies(self):
        # Test cases:
        # 1. Single tool
        # 2. Multiple tools
        # 3. Single tool, no outputs
        # 4. Multiple iterations
        # 5. Empty update dict
        pass
    def test_resolve_glob(self):
        # Test cases:
        # 1. Undefined tool
        # 2. Non-parseable glob
        # 3. Parseable but non-input glob
        pass
