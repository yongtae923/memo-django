.PHONY: check
check:
	isort -c .
	black -S -l 120 --check --exclude="idl" .

.PHONY: format
format:
	isort .
	black -S -l 120 --exclude="idl" .
