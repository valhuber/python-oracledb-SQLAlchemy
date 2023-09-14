import sys
import platform

print("platform.platform:", platform.platform())
print("sys.maxsize > 2**32:", sys.maxsize > 2**32)
print("platform.python_version:", platform.python_version())

import oracledb
print("oracledb.__version__:", oracledb.__version__)