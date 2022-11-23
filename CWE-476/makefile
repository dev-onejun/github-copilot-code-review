all: CWE-476_0 CWE-476_1 CWE-476_2
CWE-476_0: CWE-476_0_(1) CWE-476_0_(2)
CWE-476_1: CWE-476_1_(1)
CWE-476_2: CWE-476_2_(1) CWE-476_2_(2)
CWE-476_0_(1): ./CWE-476_0/CWE-476_0_(1).c
	gcc -o a ./CWE-476_0/"CWE-476_0_(1).c"
CWE-476_0_(2): ./CWE-476_0/CWE-476_0_(2).c
	gcc -o b ./CWE-476_0/"CWE-476_0_(2).c"
CWE-476_1_(1): ./CWE-476_1/CWE-476_1_(1).c
	gcc -o c ./CWE-476_1/"CWE-476_1_(1).c"
CWE-476_2_(1): ./CWE-476_2/CWE-476_2_(1).c
	gcc -o d ./CWE-476_2/"CWE-476_2_(1).c"
CWE-476_2_(2): ./CWE-476_2/CWE-476_2_(2).c
	gcc -o e ./CWE-476_2/"CWE-476_2_(2).c"
CWE-476_2_(3): ./CWE-476_2/CWE-476_2_(3).c
	gcc -o f ./CWE-476_2/"CWE-476_2_(3).c"
clean:
	rm -f a b c d e f
	