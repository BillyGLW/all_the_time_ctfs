# Usage of an pwntools, ROPgadget into ret-to-libc execution example.

### pwntools

#### apt-get update
#### apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
#### python3 -m pip install --upgrade pip
#### python3 -m pip install --upgrade git+https://github.com/Gallopsled/pwntools.git@dev3

### ROPgadget

#### pip install ROPGadget


### Makefile

`all:
	gcc exploit.c -o bf -no-pie -ggdb -fno-stack-protector


input:
	(echo `python -c 'print "A"*$(size)'`) > input

.PHONY: clean input

clean:
	rm -rf bf`
