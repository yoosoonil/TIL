# Git & Git hub

## 1. Git이란?

- **분산버전관리시스템** 또는 **형상관리시스템**이라 한다.

## 2. Git 명령어

- `git init` : 저장소 처음 만들 때
- `git add .` : untracked의 파일을 staging area로 이동
- `git add <파일명>` : 특정 파일을 staging area로 이동
- `git commit -m '버전명'` : 어떤 버전을 지칭하여 커밋
- `git status` : 현재 상태를 확인.
- `git log` : 현재 저장소에 기록된 커밋을 조회
- `git log -1` : 직전 커밋 확인
- `git`에 붙여넣기 할때는 **ctrl + v**가 아니라 **우클릭**
- `git config --global user.name "username"` : github에서 설정한 username으로 설정
- `git config --global user.email "useremail"` : github에서 설정한 useremail으로 설정

## 3. Git Hub에 연결

1.  *vscode*에서 `git commit`을 한 후, *git hub*에 연결해야 한다.
2.  `git remote add origin http://github.com/깃허브아이디/리포지토리이름`라는 명령어를 입력한다.
3.  `git remote -v`를 통해 정상적으로 연결됐는지 확인한다.
4.  `git push origin master`를 입력하여 `git hub`에 `push`한다.
5.  *git hub*에서 `commit`됐는지 확인한다.
