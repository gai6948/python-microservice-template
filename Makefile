setup: initialize_git install

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache

run:
	PYTHONPATH=$(pwd) python webapi/main.py

unit-test:
	PYTHONPATH=$(pwd) python -m xmlrunner discover -t webapi -s webapi/tests
