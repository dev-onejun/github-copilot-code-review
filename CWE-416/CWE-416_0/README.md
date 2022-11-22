# CWE-416 First Scenario

## Copilot의 추천 코드

![1](./CWE-416_0_(1).gif)\
새로운 변수 read_size를 이용 buffer로부터 읽어들이는 것을 확인할 수 있다.\
![2](./CWE-416_0_(2).gif)\
fgets를 이용해 buffer로부터 읽어들이는 것을 확인할 수 있다.

## 결론

두 경우 모두 마지막에 buffer에 할당된 메모리를 해제하고 더 이상 사용하지 않는다.
