# =============================== #
#  Particle Simulator Makefile    #
#  Written by Howard Yuan         #
#                                 #
#  Basically a straight copy of   #
#  Angelo Kyrilov's Web Server    #
#  Makefile                       #
# =============================== #

#compiler
CC = g++

# Compiler flags
CFLAGS = -lglfw -lglut -lGLU -lGL -lGLEW  -Ihpp  -Idb -Idep -w -std=c++11  -lboost_system -lboost_filesystem

#Project File Struct
IDIR = inc
ODIR = obj
BDIR = bin
SDIR = src
TDIR = test

PROGRAM = simulator
TEST = test

H_FILES := $(wildcard $(SDIR)/*.cpp)

SRC_FILES := $(wildcard $(SDIR)/*.cpp)
OBJ := $(patsubst $(SDIR)/%.cpp,$(ODIR)/%.o,$(SRC_FILES))

NEEDED_FILES := $(filter-out $(SDIR)/app.cpp, $(SRC_FILES))
TESTOBJ = $(TDIR)/$(ODIR)/test.o $(patsubst $(SDIR)/%.cpp,$(ODIR)/%.o,$(NEEDED_FILES))

$(PDIR)/$(ODIR)/%.o: $(PDIR)/%.cpp $(H_FILES)
	$(CC) -c -o $@ $< $(CFLAGS)

$(TDIR)/$(ODIR)/%.o: $(TDIR)/%.cpp $(H_FILES)
	$(CC) -c -o $@ $< $(CFLAGS)

$(ODIR)/%.o: $(SDIR)/%.cpp $(H_FILES)
	$(CC) -c -o $@ $< $(CFLAGS)

$(PROGRAM): $(OBJ) 
	$(CC) $^ -o $(BDIR)/$@ $(CFLAGS)

$(TEST): $(TESTOBJ) 
	$(CC) $^ -o $(BDIR)/$@ $(CFLAGS)

clean:
	$(RM) $(BDIR)/*
	$(RM) $(ODIR)/*.o
	$(RM) $(TDIR)/$(ODIR)/*.o
	$(RM) $(PDIR)/$(ODIR)/*.o