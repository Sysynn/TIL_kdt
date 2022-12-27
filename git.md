# git 저장소 만들기 연습
## .git 폴더 생성
- git innit 명령어를 통해 .git 폴더를 생성
- .git 폴더가 생성되면 git 저장소(repository)가 생성됨을 의미
- 터미널에서는 (master) 혹은 (main) 표기로 확인한다

## 버전 기록
- 작업 후 add하여 Staging area에 모아 commit으로 버전을 기록한다
- 작업을 한 파일은 working directory에 남겨져 있으며 변경 사항을 저장 후에 add 명령어를 통해 Staging Area로 이동시킨 뒤 Commit 명령어를 통해 버전으로 기록한다.

## 기본 명령어
```$git add <file>```
- working directory 상에서 작업한 파일 (untracked 상태)을 staged로 변경
- modified 상태의 파일을 staged로 변경

```$git commit -m <Commit Message>```
- staged 상태의 파일을 커밋 명령어를 통해 버전으로 기록한다
```$git status```
현재 저장소에 기록되어 있는 커밋을 확인한다
다양한 옵션을 통해 로그를 조회할 수 있다
    - $git log -1
    - $git log --online
    - $git log -2 --online
    
    
```$git status```
- Status로 확인할 수 있는 파일의 상태
    1. Tracked: 이전부터 버전으로 관리되고 있는 파일
        - Unmodified : git status에 나타나지 않음
        - Modified : Changes not staged for commit
        - Staged : Changes to be committe
    2. Untracked : 버전으로 관리된 적 없는 파일 (파일을 새로 만든 경우)

```$git log```
 - 현재까지 기록한 버전들의 로그를 확인한다



