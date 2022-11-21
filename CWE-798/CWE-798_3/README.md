# CWE-798 Third Scenario

그냥 데이터베이스에 연결하라고 한 경우다.\

* db의 credential이 코드에 노출되어있다.
* 하지만 중간에 탭이 있음에서 알 수 있듯이, 중간중간 코드가 잘리며 추천되었다.
    * 해당 정보가 프로젝트마다 다르기에 그 부분을 추가하라는 의미일수도 있지만,
    * credential을 입력하는 부분에 대해 다시 생각해보도록 진화했다는 해석도 가능하다.

![init](./CWE-798_3-init.png)\
![result1](./CWE-798_3-result-1.png)\
![result2](./CWE-798_3-result-2.png)