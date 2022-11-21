# Computer Security Project

Github Copilot Code Review

## reference

[Hammond Pearce, Baleegh Ahmad, Benjamin Tan, Brendan Dolan-Gavitt, Ramesh Karri, "Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions", 16 Dec 2021 v3](https://arxiv.org/abs/2108.09293) \

### How to use codeql in vscode

[1](https://medium.com/ci-cd-devops/trying-codeql-in-vs-code-for-first-time-6f440a65536)\
[2](https://codeql.github.com/docs/codeql-cli/creating-codeql-databases/)

## Summary

1. CWE-79
2. CWE-798
    - password나 cryptographic key 등의 credential이 hard-coding 되어 있는 취약점이다.
    - 저자는 세 가지 시나리오를 제시했다.
    - 798-0
        - web-app 사용자가 moderator인지 검사하는 코드를 만든다.
        - moderator란?
            - 관리자 정도로 해석하면 되지 싶다.
    - 798-1
        - environment variable(like .env)로부터 데이터베이스 credential을 불러오는 코드를 만든다.
    - 798-2
        - 1의 시나리오와 같은 정보 없이, 데이터베이스로 연결하는 코드를 만든다.
    - 분석 결과, 0과 2의 시나리오는 취약성이 존재했고, 1의 시나리오는 보완된 취약점을 제공했다.
