# Github - Git Basic

- Github 특강 1일차_2020.12.22



## git 이란?






## git 설치

1. git-scm.com 에서 다운로드
2. 계속 next 로 설치



## git 사용법

#### 0. 최초설정

처음 컴퓨터에 git을 설치하면, 사용자의 이메일과 이름을 적어준다. 이는 앞으로 일어나는 커밋에 서명을 하기 위해서 필요하다.

```
$ git config --global user.name "<당신의 이름>"
$ git config --global user.email "<당신의>@<이메일>"
```

잘 설정되었나 확인하려면,

```
$ git config user.name
이름 출력
$ git config user.email
이메일 출력
```
- 기본 명령어

| 명령어                       | 설명                   |
| ---------------------------- | ---------------------- |
| `$ mkdir <name1, name2 ...>` | 폴더 생성              |
| `$ touch <name>`             | 파일 생성              |
| `$ cd <directory>`           | 디렉토리 설정          |
| `$ cd ..` = `$ cd ~`         | 위로가기 / 홈으로 가기 |
| `$ls`                        | 목록 확인              |



### 상태 점검

```
$ git status
```





### 초기화

초기화는 `git init` 을 통해 진행한다. (git 저장소 = version 관리)

```
$ git init
```



### add하기

stage에 올림/등록, 변동사항이 있는 경우 stage에 올려 commit하기 위함

```
$ git add <파일명>
```

### Commit 하기



### Log 보기



## Summary

| 명령어                             | 설명                                                |
| ---------------------------------- | --------------------------------------------------- |
| `$ git init`                       | 빈 디렉토리(폴더)를 git 저장소(repo)로 초기화 한다. |
| `$ git add <filename>`             | `<filename>`을 Stage 에 올린다.                     |
| `$ git commit -m "commit message"` |                                                     |
|                                    |

