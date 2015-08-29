#!/usr/bin/env python
import copy, sys
from PyPDF2 import PdfFileWriter, PdfFileReader

print(sys.argv);
arg = sys.argv #arguments passed
condition = arg[1]
inputFileName = arg[2];
pagesToMerge = arg[3:-1];
outputFile = arg[-1];

# print(inputFileName,outputFile);
print ("starting ... ");
output = PdfFileWriter()
input1 = PdfFileReader(open("LFS-BOOK-7.3.pdf", "rb"));
# print ("document1.pdf has %d pages." + input1.getNumPages());
# print(input1.getNumPages());

for i in pagesToMerge:
	print("merging page no ", i)
	output.addPage(input1.getPage(int(i)));

# outputStream = file("sample.pdf", "wb")
# output.write(outputStream)
print("creating file",outputFile)
with open(outputFile, "wb") as outputStream:
    output.write(outputStream)

print("enjoy your file ")

# to excute
# python pdfcutter.py --make filename 2 3 4 hello.pdf