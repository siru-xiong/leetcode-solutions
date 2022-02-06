# Problem Id:  193
# Problem Name:  Valid Phone Numbers, 有效电话号码
# Problem Url:  https://leetcode-cn.com/problems/valid-phone-numbers/
# Problem Level:  Easy
# Language:  Bash
 
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt