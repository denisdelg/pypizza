.PHONY: test

test:
	python3 -m unittest pizza_bot_tests

simple-example:
	python3 pizzabot.py 5x5 \(1,\ 3\) \(4,\ 4\)

full-example:
	python3 pizzabot.py 5x5 \(0,\ 0\) \(1,\ 3\) \(4,\ 4\) \(4,\ 2\) \(4,\ 2\) \(0,\ 1\) \(3,\ 2\) \(2,\ 3\) \(4,\ 1\)

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +