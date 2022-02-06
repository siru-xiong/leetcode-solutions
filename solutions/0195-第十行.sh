# Problem Id:  195
# Problem Name:  Tenth Line, 第十行
# Problem Url:  https://leetcode-cn.com/problems/tenth-line/
# Problem Level:  Easy
# Language:  Bash
 
# Read from the file file.txt and output the tenth line to stdout.
python3 -c '
f = open("file.txt")
for i in range(9):
    f.readline()
print(f.readline(), end = "")
'