깃 허브 사용법 정리

1. git bash 설치

2. 프로젝트 폴더 정하기
- 폴더 경로 이동
pwd: 현재 위치한 폴더
ls: 현재 위치한 폴더 안 내용 
옵션
-a : 숨김파일 확인
-l : 접근권한 확인

cd: 폴더 이동 명령어
사용법
cd ../ : 이전 디렉토리(폴더)로 이동
cd / : 최상위 디렉토리 이동 : gitbash에서는 gitbash가 설치된 폴더로 이동(최상위 디렉토리가 gitbash 설치폴더로 마운트(연결)됨) => 여기서 c드라이브 d드라이브 이동도 가능
cd ~ : 홈 디렉터리 이동(로그인한 사용자 폴더)
cd 폴더이름 : 해당 디렉토리로 이동

explorer .: 현재 위치한 경로 탐색기로 열어보기(확인용)

mkdir 폴더이름: 폴더 만들기

3. 초기 설정
3-1. 해당 폴더 내에서 git init
3-1-1. 그대로 활용(github에 어떠한 파일과 폴더도 없는 경우)
3-1-2. git pull을 통해 내용 받아오기(github에 내용이 이미 있는경우)

4. 사용자 설정(누가, 얼마나 열심히 일했는지 확인을 위함)
git config --global user.name "홍길동"
git config --global user.email "hong@example.com"

현재 설정 확인
git config user.name
git config user.email

해당 디렉토리에서만 적용되는 사용자 설정(git 폴더마다 다르게 설정됨 => 전역설정(--global) 되있는 경우 덮어쓰기)
git config user.name "홍길동"
git config user.email "hong@example.com"

5. 스테이징에 올리기
git add ./ : 현재 디렉토리 내의 변경된 전체 파일들
git reset 변경된파일 : 해당 파일은 추가하지 않음

6. 

자주 하는 실수 & 해결법
README 있는 저장소에 push => "rejected, non-fast-forward"
해결법: 빈 저장소로 다시 만들기

main 아닌 master 브랜치 => src refspec main does not match
해결법: git branch -M main 후 다시 push

인증 실패: remote: Permission denied
해결법: SSH 키 설정 또는 Personal Access Token 사용