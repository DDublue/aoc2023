MAIN = day1
SOURCE = $(MAIN).c
OBJECT = $(MAIN).o
COMPILE = gcc -std=c17 -Wall -c
LINK = gcc -std=c17 -Wall -o
REMOVE = rm -f

$(MAIN): $(OBJECT)
	$(LINK) $(MAIN) $(OBJECT)

$(OBJECT): $(SOURCE)
	$(COMPILE) $(SOURCE)

clean:
	$(REMOVE) $(MAIN)
	$(REMOVE) $(OBJECT)
	