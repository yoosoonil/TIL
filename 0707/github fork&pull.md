# Git hub fork & pull



## ✨ git 저장소로 버전관리 시작하기

1. 파일의 경로를 통해 **master** 유무를 확인하여 `git init`됐는지 확인.

2. **master**가 없다면 `git init` 한다.

3. 만든 데이터들을 `git add`하고 `git commit -m {작업내용}`한다.

   - 버전을 나눌 때는 각각의 파일을 `add`하고 `commit`한다.
   - commit message는 각 파일, 폴더 설명보다는 이번의 작업에 대한 전반적인 설명을 함축(요약)해야 한다.
     - `git checkout 커밋코드` : 해당 커밋코드로 되돌아 간다.
     - 커밋한 모든 내용은 다시 되돌릴 수 있음. 하지만 커밋하지 않은 모든내용은 다시 되돌릴 수 없음.

4. git hub에 repository를 만들고 local에서 git으로 해당 repo에 연결한다.

   > `git remote {repo url}`

5. `git push origin master`를 통해 만들었던 `commit`을 `git hub`로 `push`한다.

   > github에서 삭제하고 싶다면 로컬에서 삭제 후 커밋, push 한다.
   >
   > Local에서 파일&폴더 생성, 이름 수정 및 이동을 하고 `add, commit, push`하면 된다.



## Ⅰ. clone

1. `git hub`에서 **clone 할 것**을 코드 복사하여 `clone`할 폴더에서 `git bash`하여 `git clone {clone 코드}`로 `clone`한다.

   > clone은 전체저장소를 받아오고, pull은 최근 커밋만 받아오는 것.



## Ⅱ. branch

1. branch의 목적

   > 독립적인 버전을 만들어나가기 위해서, 작업 및 협업하기 위해. 

2. branch merge

   > 각 branch에서 작업을 한 이후 이력을 합치기 위해서는 일반적으로 merge 입력

3. branch 명령어

   > 확인 및 생성
   
   - `git branch` : 현재 레포의 브렌치 목록 확인
   - `git branch --all` : 서버에 있는 모든 브렌치 확인
   - `git branch -v` : 최신 브렌치 확인
   - `git branch 브렌치이름` : 브렌치 생성
   - `git checkout 브렌치이름` : 브렌치 이동
   - `git checkout -b 브렌치이름` : 브렌치 생성 후 해당 브렌치로 이동
   - `git merge 브렌치이름` : root가 되는 곳에서 branch를 병합하는 것
     - master 병합 후 브렌치를 지우면, 커밋(파일)도 지워진다? ->  x 
   
   > 삭제 및 수정
   
   - `git branch -d 브렌치이름` : 해당 브렌치 삭제
   - `git push origin --delete 브렌치이름` : 서버에 있는 브렌치 삭제
   - `git branch --move 브렌치이름 새로운이름` : 브렌치 이름 변경
   - `git push --set-upstream origin 브렌치이름` : 이름 수정한 브렌치를 서버로 업데이트
   
   

## Ⅲ. merge

1. merge

   > 각자의 업무를 병합하는 것. branch와 branch, branch와 root.

2. merge 명령어
   - `git merge 브렌치이름` : 브렌치를 병합
   - `git log --oneline--graph` : 병합한 상태를 그래프적으로 볼  수 있음

3. conflict 났을 때

   > 다시 `add`, `commit`, `merge` 한다.



## Ⅳ. 다른 사람의 github에서 fork & pull

1. 다른 사람의 `github`에서 `fork` 하여 나의 `github`로 가져온다.
2. 나의 `github`에서 `code` 클릭 후 코드 복사하여 나의 로컬에 `clone`한다.
3. `vscode`에서 `branch`생성 후 그곳에서 파일 및 폴더를 수정한다. 그리고 수정한것에 대하여 `ctrl + s`하여 저장한다.
4. `add`하고 `commit`후 `push origin 브렌치이름`한다.
5. 나의 `github`에서 **생성한 브렌치**로 이동하여 `contribute`에서 `open pull request`눌러 **pull request**한다.
6. `merge`될 때까지 기다린다. 



## 🪄기타 숙지사항

1.  add 잘못했을 때

- `git restore --staged [파일]` : [파일]을 unstaged로 돌려놓음.
- `git restore [파일]` : 변경 사항으로 돌아가는 것

2. shared reposibility 와 fork&pull의 차이

   > 권한 유무의 차이

