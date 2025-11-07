# 깃 허브 사용법 정리

## 1. git bash 설치
<br>

## 2. 프로젝트 폴더 정하기
#### 2-1. 폴더 경로 이동에 관련된 명령어<br>
pwd: 현재 위치한 폴더<br>
ls: 현재 위치한 폴더 안 내용 <br>
<br>
옵션<br>
-a : 숨김파일 확인<br>
-l : 접근권한 확인<br>

cd: 폴더 이동 명령어<br>
사용법<br>
cd ../ : 이전 디렉토리(폴더)로 이동<br>
cd / : 최상위 디렉토리 이동 : gitbash에서는 gitbash가 설치된 폴더로 이동(최상위 디렉토리가 gitbash 설치폴더로 마운트(연결)됨) => 여기서 c드라이브 d드라이브 이동도 가능<br>
cd ~ : 홈 디렉터리 이동(로그인한 사용자 폴더)<br>
cd 폴더이름 : 해당 디렉토리로 이동<br>
<br>
explorer .: 현재 위치한 경로 탐색기로 열어보기(확인용)<br>
<br>
mkdir 폴더이름: 폴더 만들기<br>
<br>

## 3. 초기 설정
#### 3-1. 해당 폴더 내에서 git init<br>
#### 3-1-1. 그대로 활용(github에 어떠한 파일과 폴더도 없는 경우)<br>
#### 3-1-2. git pull을 통해 내용 받아오기(github에 내용이 이미 있는경우)<br>
git pull http://.git<br>
<br>

## 4. 사용자 설정(누가, 얼마나 열심히 일했는지 확인을 위함)
git config --global user.name "홍길동"<br>
git config --global user.email "hong@example.com"<br>
<br>

##### 현재 설정 확인<br>
git config user.name<br>
git config user.email<br>
<br>

##### 해당 디렉토리에서만 적용되는 사용자 설정(git 폴더마다 다르게 설정됨 => 전역설정(--global) 되있는 경우 덮어쓰기)<br>
git config user.name "홍길동"<br>
git config user.email "hong@example.com"<br>
<br>

## 5. 스테이징에 올리기
git add 변경된파일 : 현재 디렉토리 내의 해당 파일을 올림<br>
git add ./ : 현재 디렉토리 내의 변경된 전체 파일들을 올림<br>
git restore 변경된파일 : 해당 파일을 다시 내림<br>
git restore ./ : 스테이징 내의 파일들을 다시 내림<br>
<br>

## 6. 로컬 저장소(.git 폴더)에 저장
git commit<br>
#### 6-1. vim에디터<br>
i 버튼(입력버튼) 입력후 내용(간단한 메모) 쓰기 -> esc버튼 -> :wq 입력(저장후 종료)<br>
<br>

#### 6-2. -m 옵션<br>
git commit -m "내용(간단한 메모)"<br>
<br>

## 7. 저장소 이름 설정
git remote add 별명 http://.git<br>
<br>

##### 별명 관례<br>
origin: 기존 저장소(원본)<br>
upstream: 원본 프로젝트(포크했을 때)<br>
<br>

##### 지우기(별명에 설정된 경로가 변경된 경우)<br>
git remote remove 별명<br>
<br>

## 8. 저장소에 밀어넣기(저장시도)
git push origin http://.git<br>
<br>

## 9. 고급 설정
.gitignore 파일: git 추적 대상 제외<br>
협업용, 일반 프로젝트 .gitignore은 보통 공개<br>                  
혼자 쓰는 비공개/보안 프로젝트 git rm --cached .gitignore 후 로컬 유지<br>

git rm --cached .gitignore

##### 옵션주기<br>
git push -u origin http://.git => 이후에는 git push만 해도 됨<br>
<br>



## 자주 하는 실수 & 해결법<br>
README 있는 저장소에 push => "rejected, non-fast-forward"<br>
해결법: 빈 저장소로 다시 만들기<br>
<br>

main 아닌 master 브랜치 => src refspec main does not match<br>
해결법: git branch -M main 후 다시 push<br>
<br>

인증 실패: remote: Permission denied<br>
해결법: SSH 키 설정 또는 Personal Access Token 사용<br>
<br>