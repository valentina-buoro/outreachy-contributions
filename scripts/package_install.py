import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('PyTDC')
install('tiledbsoma')
install('ersilia')
install('xgboost')


