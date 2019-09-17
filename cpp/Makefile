CXXFLAGS = -O3 -std=c++17
SOURCES  = $(shell find . -type f -name '*.cpp')
TARGETS  = $(basename $(SOURCES))

all: $(TARGETS)

%: %.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

clean:
	$(RM) $(TARGETS)
