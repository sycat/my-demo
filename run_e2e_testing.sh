pip install --no-cache-dir -q -r requirements.txt --use-pep517
pytest --html=outputs/test_report.html --self-contained-html --junitxml=outputs/test_report.xml test_1.py || [ $? = 1 ]