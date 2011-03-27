# Default target

TESTS = 
COVERAGE_INCLUDES = --include=apps/*,project/*


.PHONY: all

all: develop


###############
# Development #
###############

.PHONY: develop run tags todo test flake8 syncdb clean

develop: bootstrap.py \
         bin/buildout \
         bin/django \
         var/development.db \
	 var/data/main.spa

shell:
	bin/django shell_plus

crawl:
	bin/scrapy crawl delfi_lt

run:
	bin/django runserver

tags:
	bin/ctags -v

todo:
	@egrep -n 'FIXME|TODO' $$(find apps -iname '*.py' ; \
	                          find project -iname '*.py')

test:
	bin/django test $(TESTS)

coverage:
	bin/coverage run $(COVERAGE_INCLUDES) bin/django test $(TESTS)
	bin/coverage html -d var/htmlcov/ $(COVERAGE_INCLUDES)
	bin/coverage report $(COVERAGE_INCLUDES)
	@echo "Also try xdg-open var/htmlcov/index.html"

flake8:
	@bin/flake8 \
	    project/

syncdb:
	test ! -f bin/django.wsgi
	if [ -f var/development.db ] ; then rm var/development.db ; fi
	bin/django syncdb --all --noinput
	bin/django migrate --fake
	bin/django loaddata initial_data.json

createdb:
	mysql -uroot -e 'CREATE DATABASE 369lt CHARACTER SET utf8 COLLATE utf8_unicode_ci;'

# circo dot fdp neato nop nop1 nop2 twopi
graph:
	bin/django graph_models \
	    --group-models \
	    --all-applications \
	    -o var/graph.png
	if [ "$$(uname)" = "Darwin" ]; then \
	    open var/graph.png; \
	else \
	    xdg-open var/graph.png; \
	fi

bin/django: bin/buildout buildout.cfg development.cfg
	test ! -f bin/django.wsgi
	bin/buildout -c development.cfg -N
	touch -c $@

var/development.db:
	test ! -f bin/django.wsgi
	bin/django syncdb --all --noinput
	bin/django migrate --fake
	bin/django loaddata initial_data.json

clean:

realclean: clean
	hg purge --all


##############
# Deployment #
##############

.PHONY: deploy

deploy: bootstrap.py \
	bin/buildout \
	bin/django.wsgi \
	project/production.py \
	var/production.db \
	var/htdocs/static \
 	var/data/main.spa

bin/django.wsgi: bin/buildout buildout.cfg etc/*.in
	test ! -f var/development.db
	bin/buildout -N
	touch -c $@

project/production.py:
	@echo
	@echo "project/production.py settings file is missing."
	@echo "Create this file and run make deploy again."
	@echo
	@echo "Here is example, how to prepare MySQL database:"
	@echo
	@echo "    CREATE USER '<user>'@'localhost' IDENTIFIED BY '<password>';"
	@echo "    GRANT ALL ON *.* TO '<user>'@'localhost';"
	@echo "    CREATE DATABASE <dbname> CHARACTER SET utf8;"
	@echo
	@echo "Use generated sample file: etc/my.cnf and specify "
	@echo "database connection credentials. You can use this file,"
	@echo "to connect to database:"
	@echo
	@echo "    mysql --defaults-extra-file=etc/my.cnf"
	@echo
	@echo "Use generated sample file: etc/production.py and "
	@echo "adjust your production server settings:"
	@echo
	@echo "    cp etc/production.py project/production.py"
	@echo "    vi project/production.py"
	@echo
	@exit 1

var/production.db:
	test ! -f var/development.db
	bin/django syncdb --all --noinput
	bin/django migrate --fake
	bin/django loaddata initial_data.json
	touch -c $@


###########
# General #
###########

bootstrap.py:
	mkdir -p eggs downloads
	wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

bin/buildout:
	if which buildout > /dev/null ; then \
	    $$(which buildout) init ; \
	else \
	    python bootstrap.py --distribute ; \
	fi

var/htdocs/static:
	bin/django collectstatic --noinput

var/data/main.spa:
	parts/sphinx/bin/indexer main
