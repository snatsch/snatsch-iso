release:
	python setup.py bdist_wheel
	twine upload dist/*

clean_up:
	rm -rf build dist snatsch_iso.egg-info
