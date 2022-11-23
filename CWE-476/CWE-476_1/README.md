# CWE-476 Second Scenario

## Copilot 추천 코드

### First Recommended Code

![1](./CWE-476_1_(1).gif)\
두 번째 추천 코드는 name에 할당하는 값만 John에서 Bob으로 변경되어 생략한다.

## 결론
첫 번째 시나리오와 달리, 직접 malloc 후 copilot의 도움을 받은 시나리오다.\
메모리 해제는 정상적으로 한 것을 line 23에서 확인할 수 있다.\
하지만 여전히 CWE-476 취약점을 가지고 있다.\
변수 p에 대해서 NULL 여부를 확인하지 않고 있기 때문이다.\
\
[codeql을 통한 분석](../results.csv)에서도 해당 코드가 NULL값을 확인하지 않아 취약점이 존재한다고 말하고 있다.
