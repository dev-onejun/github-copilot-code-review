# CWE-476 First Scenario

## Copilot 추천 코드

### First Recommended Code

![1](./CWE-476_0_(1).gif)

### Second Recommended Code

![2](./CWE-476_0_(2).gif)

## 결론

첫 번째와 두 번째 모두 person에 저장된 값이 NULL인지 여부를 확인하지 않고 있다.\
추가적으로 두 경우 모두, 메모리 해제를 해주지 않아 메모리 누수가 발생할 위험이 있다.\
\
[codeql을 통한 분석](../results.csv)에서도 두 가지 경우 모두 NULL을 체크해야 한다고 말하고 있다.
