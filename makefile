.PHONY: Diplomacy.log

FILES :=								\
	Diplomacy.html						\
	Diplomacy.log						\
	Diplomacy.py						\
	RunDiplomacy1.in					\
	RunDiplomacy2.in					\
	RunDiplomacy3.in					\
	RunDiplomacy4.in					\
	RunDiplomacy5.in					\
	RunDiplomacy1.out					\
	RunDiplomacy2.out					\
	RunDiplomacy3.out					\
	RunDiplomacy4.out					\
	RunDiplomacy5.out					\
	RunDiplomacy.py						\
	TestDiplomacy.out					\
	TestDiplomacy.py					\
	# cs330e-collatz-tests/nhardham-RunCollatz.in	\
	# cs330e-collatz-tests/nhardham-RunCollatz.out	\
	#cs330e-collatz-tests/nhardham-TestCollatz.out	\
	#cs330e-collatz-tests/nhardham-TestCollatz.py	\

ifeq ($(shell uname), Darwin)		  # Apple
	PYTHON   := python3
	PIP	  := pip3
	PYLINT   := pylint
	COVERAGE := coverage
	PYDOC	:= pydoc3
	AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Windows
	PYTHON   := python				 # on my machine it's python
	PIP	  := pip3
	PYLINT   := pylint
	COVERAGE := coverage
	PYDOC	:= python -m pydoc		# on my machine it's pydoc
	AUTOPEP8 := autopep8
else								   # UTCS
	PYTHON   := python3
	PIP	  := pip3
	PYLINT   := pylint3
	COVERAGE := coverage
	PYDOC	:= pydoc3
	AUTOPEP8 := autopep8
endif


Diplomacy-tests:
	git clone https://gitlab.com/fareszf/cs330e-diplomacy-tests.git

Diplomacy.html: Diplomacy.py
	$(PYDOC) -w Diplomacy

Diplomacy.log:
	git log > Diplomacy.log

RunDiplomacy.tmp: RunDiplomacy1.in RunDiplomacy1.out RunDiplomacy.py
	$(PYTHON) RunDiplomacy.py < RunDiplomacy1.in > RunDiplomacy.tmp
	diff --strip-trailing-cr RunDiplomacy.tmp RunDiplomacy1.out

TestDiplomacy.tmp: TestDiplomacy.py
	$(COVERAGE) run	--branch TestDiplomacy.py >  TestDiplomacy.tmp 2>&1
	$(COVERAGE) report -m					  >> TestDiplomacy.tmp
	cat TestDiplomacy.tmp


check:
	@not_found=0;								 \
	for i in $(FILES);							\
	do											\
		if [ -e $$i ];							\
		then									  \
			echo "$$i found";					 \
		else									  \
			echo "$$i NOT FOUND";				 \
			not_found=`expr "$$not_found" + "1"`; \
		fi										\
	done;										 \
	if [ $$not_found -ne 0 ];					 \
	then										  \
		echo "$$not_found failures";			  \
		exit 1;								   \
	fi;										   \
	echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  RunDiplomacy.tmp
	rm -f  TestDiplomacy.tmp
	rm -rf __pycache__
	rm -rf cs330e-diplomacy-tests

config:
	git config -l

format:
	$(AUTOPEP8) -i Diplomacy.py
	$(AUTOPEP8) -i RunDiplomacy.py
	$(AUTOPEP8) -i TestDiplomacy.py

scrub:
	make clean
	rm -f  Diplomacy.html
	rm -f  Diplomacy.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

versions:
	which	   $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	which	   $(COVERAGE)
	$(COVERAGE) --version
	@echo
	which	   git
	git		 --version
	@echo
	which	   make
	make		--version
	@echo
	which	   $(PIP)
	$(PIP)	  --version
	@echo
	which	   $(PYLINT)
	$(PYLINT)   --version
	@echo
	which		$(PYTHON)
	$(PYTHON)	--version

test: Diplomacy.html Diplomacy.log RunDiplomacy.tmp TestDiplomacy.tmp Diplomacy-tests check
