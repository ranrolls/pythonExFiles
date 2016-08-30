Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # if/elif/else   if/else  if/elif/elif/....  else
>>> t = 0
>>> gc = 1
>>> while gc <= 10:
	g = input('enter grade:\n')
	g = int(g)
	t += g
	gc++
	
SyntaxError: invalid syntax
>>> while gc <= 10:
	g = input('enter grade:\n')
	g = int(g)
	t += g
	gc += 1
	if gc == 9:
		print(t/10)
		break

	
enter grade:
2
enter grade:
4
enter grade:
6
enter grade:
3
enter grade:
6
enter grade:
8
enter grade:
5
enter grade:
2
3.6
>>> for c in range(10):
	print(2+c)

	
2
3
4
5
6
7
8
9
10
11
>>> for n in range(2,101,3):
	# range (init, last, increment)
	print(n)

	
2
5
8
11
14
17
20
23
26
29
32
35
38
41
44
47
50
53
56
59
62
65
68
71
74
77
80
83
86
89
92
95
98
>>> 
