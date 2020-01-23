py:
	mkdir -p build/py compiled/py/pravah_protocols
	protoc -I=./protocols/include -I=./protocols --python_out=build/py/ ./protocols/**/*.proto
	find ./build/py/ -name *.py -exec cp '{}' "./compiled/py/pravah_protocols" ";"
	rm -rf build
	cd ./compiled/py/pravah_protocols/ && sed -i '' 's/^\(import.*pb2\)/from . \1/g' *.py
	cp template/__init__.py compiled/py/pravah_protocols/__init__.py
	cp template/Makefile compiled/py/Makefile
	ln -s ../../template/setup.py compiled/py/setup.py

clean-compiled:
	rm -rf compiled

clean:
	rm -rf compiled/py/{build,dist,pravah_protocols/__pycache__,*.egg-info}
