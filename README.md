# BasicAssemblyCompiler
A basic assembly compiler converting an XML language to Assembly

# How to read the test file
For each figure, there are 3 corresponding files: c file, asm file, and xml file. C file is created for the readers to understand what the program is doing instead of reading the xml file. XML file is translated from the C file. The xml file is over-written when the program runs the xml file. 

# Supported Figures
## 1. Variable - Argument MicroBenchmark
### Files
* C-file: [micro_benchmark_variable_argument.c](testing/micro_benchmark_variable_argument.c)
* XML-file: [micro_benchmark_variable_argument.xml](testing/micro_benchmark_variable_argument.xml)
* Asm-file: [micro_benchmark_variable_argument.asm](testing/micro_benchmark_variable_argument.asm)

### General Test
There are 10 t-registers and 8 s-regsiters in this compiler. They are listed in [harshTable.py]() file. When the program runs out of the registers, it will raise the error. The current version of the xml file will run fine. To test the error case, uncomment the last variable declaration in the xml file.

### Futher considered improvements:
* Use s-registers when run out of t-registers
* Release unused registers to reuse them

