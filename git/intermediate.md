# Github - Git Intermediate



## Branch란?

- 코드 전체를 복사하고 나서 원래 코드와는 상관없이 독립적으로 개발하는 것
- 브랜치 생성 - 작업 - merge



## Branch 사용법

#### 1. 브랜치 생성

```
$ git branch <name>
```



#### 2. 브랜치 확인

```
$ git branch   # 현황 확인
```



#### 3. 브랜치 이동(head 이동)

- Git이 작업 중인 브랜치를 파악(현재 작업 중이 브랜치를 가리키는 head)

```
$ git switch <name>
ex. $ git switch master  # head를 master에 이동
```

```
$ git checkout -b <branch name>  # git branch 만들기 + 이동
= $ git switch -c <branch name>
```

```
$ git switch -h  # 도움말
```



#### 4. 브랜치 합치기

- 합칠 브랜치에서 합쳐질 브랜치를 merge 하면 됨
- 항상 master에서 다른 브랜치를 병합(master에 병합)

```
$ git switch master   # master 브랜치에서 merge
$ git merge <name>
```



#### 5. 브랜치 삭제하기

```
$ git branch -d <name>
```



## Remote Branch

#### 1. Push

- 리모트 저장소에 전송 : 로컬의 브랜치를 서버로 전송하려면 권한이 있는 리모트 저장소에 push 해야 함.

```
$ git push origin <branch name>
```



#### 2. Pull

- 서버에는 존재하지만, 로컬에는 아직 없는 데이터를 받아와서 저장
- pull은 master branch에서 당겨와야 함

```
$ git pull origin 
```



*master에서만 branch하지 않고, 협업을 하기 위해서는 remote에 저장해서 진행하는 것이 좋음.

*저장소안에 저장소를 만드는 것은 안됨



#### Tip. 

##### 1. 문서편집

| 명령어             | 설명                          |
| ------------------ | ----------------------------- |
| `$vim <파일명.md>` | 터미널에서 사용하는 문서 편집 |
| `i`                | 편집시작 -> ESC               |
| `dd`               | 삭제                          |
| `:w`               | 저장                          |
| `:q`               | 나오기                        |
| `:q!`              | 강제종료(저장X)               |

##### 2. 기타

| 명령어   | 설명  |
| -------- | ----- |
| `ctrl+i` | clear |
|          |       |
|          |       |
|          |       |



## Summary

| 명령어                            | 설명                   |
| --------------------------------- | ---------------------- |
| `$ git branch <name>`             | 브랜치 생성            |
| `$ git branch `                   | 브랜치 현황 확인       |
| `$ git switch <name>`             | 브랜치 이동            |
| `$ git switch -c <branch name>`   | branch 만들기 + 이동   |
| `$ git merge <name>`              | 브랜치 합치기          |
| `$ git push origin <branch name>` | 저장소에 올리기        |
| `$ git pull origin`               | 로컬 저장소로 내려받기 |