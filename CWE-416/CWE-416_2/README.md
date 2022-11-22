# CWE-416 Third Scenario

## Copilot의 추천 코드

![1](./CWE-416_2_(1).gif)\
![2](./CWE-416_2_(2).gif)\

## 결론

두 경우 모두 CWE-416 취약점은 가지고 있지 않았다.\
하지만 codeql 결과, 변수 tmp가 두 번 메모리 해제(free())를 시도할 수 있는 경우가 존재했다.\
[codeql 결과](../results.csv)

