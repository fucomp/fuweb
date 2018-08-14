DRIVER_PATH:="https://chromedriver.storage.googleapis.com/2.41/"

OS=$(shell uname)
ifeq "$(OS)" "Darwin"
DRIVER_BASENAME:=chromedriver_mac64.zip
endif
ifeq "$(OS)" "Linux"
DRIVER_BASENAME:=chromedriver_linux64.zip
endif

DRIVER_URI=$(DRIVER_PATH)$(DRIVER_BASENAME)
DRIVER_DOWNLOAD=driver/$(DRIVER_BASENAME)
DRIVER=chromedriver

dev-env: $(DRIVER)
	virtualenv .
	bash -c "source bin/activate && pip install -rrequirements.txt"

$(DRIVER): $(DRIVER_DOWNLOAD)
	unzip $<

$(DRIVER_DOWNLOAD):
	mkdir -p driver
	cd driver && wget $(DRIVER_URI)

clean:
	bash -c 'for i in "$(shell cat .gitignore)"; do rm -rf $$i; done'
