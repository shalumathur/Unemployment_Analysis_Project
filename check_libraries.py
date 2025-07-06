# check_libraries.py

try:
    import pandas
    print("✅ pandas is installed.")
except ImportError:
    print("❌ pandas is NOT installed.")

try:
    import matplotlib
    print("✅ matplotlib is installed.")
except ImportError:
    print("❌ matplotlib is NOT installed.")

try:
    import seaborn
    print("✅ seaborn is installed.")
except ImportError:
    print("❌ seaborn is NOT installed.")