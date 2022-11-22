all: CWE-416_0 CWE-416_1 CWE-416_2
CWE-416_0: CWE-416_0_(1) CWE-416_0_(2)
CWE-416_1: CWE-416_1_(1) CWE-416_1_(2)
CWE-416_2: CWE-416_2_(1) CWE-416_2_(2)
CWE-416_0_(1): ./CWE-416_0/CWE-416_0_(1).c
	gcc -o a ./CWE-416_0/"CWE-416_0_(1).c"
CWE-416_0_(2): ./CWE-416_0/CWE-416_0_(2).c
	gcc -o b ./CWE-416_0/"CWE-416_0_(2).c"
CWE-416_1_(1): ./CWE-416_1/CWE-416_1_(1).c
	gcc -o c ./CWE-416_1/"CWE-416_1_(1).c"
CWE-416_1_(2): ./CWE-416_1/CWE-416_1_(2).c
	gcc -o d ./CWE-416_1/"CWE-416_1_(2).c"
CWE-416_2_(1): ./CWE-416_2/CWE-416_2_(1).c
	gcc -o e ./CWE-416_2/"CWE-416_2_(1).c"
CWE-416_2_(2): ./CWE-416_2/CWE-416_2_(2).c
	gcc -o f ./CWE-416_2/"CWE-416_2_(2).c"
clean:
	rm -f a b c d e f
	