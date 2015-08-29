#!/usr/bin/env python
import copy, sys
from PyPDF2 import PdfFileWriter, PdfFileReader

print(sys.stdin);
output = PdfFileWriter()
input1 = PdfFileReader(open("LFS-BOOK-7.3.pdf", "rb"));
# print ("document1.pdf has %d pages." + input1.getNumPages());
print(input1.getNumPages());

output.addPage(input1.getPage(0));
output.addPage(input1.getPage(1));