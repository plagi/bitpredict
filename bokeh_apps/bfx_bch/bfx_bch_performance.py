import sys
import os
sys.path.append(os.path.basename(os.path.basename(__file__)))
from app import run_charts_performance

run_charts_performance.run_chart('bfx', 'bch')
