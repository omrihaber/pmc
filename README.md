# Makefile
The following line remove or adjust the -13 for the correct g++ alias on your machine
```
CXX          = g++-13 -std=c++03
```

run the following to compile and be able to run pmc.py

```
make clean #optional
make
make libpmc.so 
```