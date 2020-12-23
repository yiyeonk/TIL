# Github - Git Intermediate

## Branch

### 브랜치 생성하기(`git branch <name>`)

### 브랜치 확인하기(`git branch`)

### 브랜치 옮기기(HEAD 움직이기 `git switch <name>`)

### 브랜치 합치기(`git merge <name>`)

- 항상 master에서 다른 브랜치를 병합

### 브랜치 삭제하기(`git branch -d <name>`)



$ vim <파일명.md> : 터미널에서 사용하는 문서 편집

i : 편집 시작 > esc

dd : 삭제

:w 저장

:q 나오기

:q! 강제종료(저장x)



missing semester kr

shell = cli



commit message 변경(최근 것만 해당)

$ git commit --amend 



$ git branch

$ git switch about : about 으로 이동 (Head가 움직임)

git commit -m 'add home'
git branch about  # about 브랜치 생성
git switch about  # about 브랜치로 이동
git branch  # 현재 브랜치 현황 확인

git switch master : head를 master에 이동

git merge about : master에 병합

git branch -d about # about 삭제



git branch 만들기 + 이동 => git checkout -b <branch name>

 =git switch -c <branch name>





현재는 master에서만 branch하는 것이 문제

협업을 하기 위해서는 remote에 올려서 하는 것이 

switch -h : help

git push origin branch_a : 각자의 브랜치를 푸쉬

ctrl + l : clear

협업 시 pull은 master에서 당김 : switch master

저장소안에 저장소를 만드는 것은 안됨



