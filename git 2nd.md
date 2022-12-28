# 2일차

* 깃허브 계정 생성 후 repository 만들기
* 해당 저장소를 오리진으로 지정할때는 
생성하면서 지정한 이름을 아래와 같은 명령어로 작성

```$git remote add origin https://github.com/Sysynn/test.git```

확인하고 싶으면

```$git log```
 

```$git push origin main```

로컬에서 생성된 버전을 생성된 원격저장소로 올린다

```$git pull origin main```

원격저장소에 올려져 잇는 버전을 로컬로 받아온다

```$git clone (github url)```

로컬에 저장소가 없으니까 저장소 자체를 최초로 가지고 오는 행위 
원격저장소에서 커밋을 가져오는 pull이랑은 다른 개념

로컬에서 프로젝트 시작 ```$git init```
원격에서 프로젝트 시작 ```$git clone```

```$git remote -v ```
연결되어있는 깃 확인


```.gitignore```

 git으로 관리하고싶지 않은 파일을 위 파일을 생성 후 내용에 추가해놓으면
이후 git으로 push 할 때 제외하고 진행함