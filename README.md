I am in the process of porting this to python3 from C. This is not complete.

Photosop CC icon resource unpacking program
07/18/2020

This is a command line program:
psccIcon [-e|-p] <idx-file>

Examples:
Unpack: psccIcon -e "D:\Photoshop CC\Resources\IconResources.idx"
Before use, make sure that at least one of PSIconsLowRes.dat and PSIconsHighRes.dat is in the same directory of idx. After the unpacking is successful, a Low or High folder will be created, which contains the disassembled pictures.
Packet: psccIcon -p "D:\Photoshop CC\Resources\IconResources.idx"
Before using it, make sure that there is at least one of Low or High folders in the same directory of idx. The names and number of all png files in it must be the same as the unpacked ones. The length and width of the picture should not change. The file name after the package ends with "_" and is generated in the same directory (if there is a copy with the same name, it will be overwritten).
The
The
Quick usage:

Unpack: When there is no High or Low folder in the same directory, drag idx directly to psccIcon.exe.
Packet: When there is at least one of the Hight or Low folders in the same directory, drag the idx directly to psccIcon.exe.
