# ☘ Project Damoa

## 📄 프로젝트 소개
프로젝트 다모아는 인가된 인원에 대해 자유롭게 커뮤니티를 형성할 수 있는 사이트입니다. 기업, 커뮤니티, 작게는 개인까지 소통을 이어나갈 수 있으며 운동, IT, 음식 등 다양한 주제로 소통방을 만들 수 있습니다. 글 또한 고민, 질문, 자랑 등 자유로운 얘기를 할 수 있습니다.    

### ⏲ 개발 기간 : 2022.7.14 ~ 2022.8.16

### 홈페이지  (현재는 닫힌 상태입니다.)

### 소개 영상  [youtube](https://youtu.be/6c7Q82DfTAU)

### Github  [Front-end](https://github.com/jjy0307/damoa_frontend)

## 🧑 팀 구성 
* 4인 팀 프로젝트  <br>
* 맡은 역할 : AI Engineer

<table>
  <tr>
    <td align="center"><strong>구분</strong></td>
    <td align="center"><strong>Back-end</strong></td>
    <td align="center"><strong>Front-end</strong></td>
    <td align="center"><strong>Designer</strong></td>
    <td align="center"><strong>AI Engineer</strong></td>	  
  </tr>
  <tr>
    <td align="center"><strong>메인페이지</strong></td>
    <td align="center">이승태</td>
    <td align="center">이승태</td>
    <td align="center">이승태</td>
    <td rowspan="5" align="center">전진영</td>
  </tr>
  <tr>
    <td align="center"><strong>마이페이지</strong></td>
    <td align="center">이승태</td>
    <td align="center">이승태</td>
    <td align="center">이승태</td>
  </tr>
  <tr>
    <td align="center"><strong>로그인 페이지</strong></td>
    <td align="center">이승태</td>
    <td align="center">이승태</td>
    <td align="center">이승태</br>전진영</td>
  </tr>
  <tr>
    <td align="center"><strong>회원가입 페이지</strong></td>
    <td align="center">이승태</td>
    <td align="center">이승태</td>
    <td align="center">이승태</br>전진영</td>
  </tr>
  <tr>
    <td align="center"><strong>커뮤니티 페이지</strong></td>
    <td align="center">이승태</br>윤가현</br>김민재</td>
    <td align="center">이승태</br>윤가현</br>김민재</td>
    <td align="center">이승태</br>윤가현</br>김민재</td>
  </tr>
</table>

## ✨ Stack
* Language : Python, Javascript
* Framework : Django, DRF
* Database : MySQL
* Infra : AWS EC2, AWS S3, Docker

## 📖 Stack & Library Version
<img src="https://img.shields.io/badge/python-3.9.12-brightgreen"> <img src="https://img.shields.io/badge/django-4.0.6-brightgreen"> <img src="https://img.shields.io/badge/django_rest_framework-3.13.1-brightgreen"> <img src="https://img.shields.io/badge/django_rest_framework_simple_jwt-5.2.0-brightgreen"> <img src="https://img.shields.io/badge/django_cors_header-3.13.0-brightgreen"> <img src="https://img.shields.io/badge/mysql_client-2.1.1-brightgreen"> <img src="https://img.shields.io/badge/tensorflow-2.9.1-brightgreen"> <img src="https://img.shields.io/badge/konlpy-0.6.0-brightgreen"> <img src="https://img.shields.io/badge/boto3-1.24.40-brightgreen"> <img src="https://img.shields.io/badge/PyJWT-2.4.0-brightgreen"> <img src="https://img.shields.io/badge/urllib3-1.26.11-brightgreen"> <img src="https://img.shields.io/badge/requests-2.28.1-brightgreen">
</br>

## 🕹 주요 기능
### 로그인 / 회원가입
* JWT 토큰 방식으로 구현
* JWT refresh token을 구현하여 로그인 상태 유지하게 끔 설정
* USERNAME_FIELD를 사용하여 유저 아이디를 고유값으로 지정하여 중복 방지 기능 구현

### 메인 페이지
* 로그인 유무에 따라 추천 커뮤니티 변경
    * prefetch_related, Q 사용을 통한 로그인 된 사용자의 가입되지 않은 커뮤니티 목록 리턴 기능 구현
    * Table Community Field is_public을 filtering 하여 공개 커뮤니티 리스트를 리턴 받는 기능 구현
* 커뮤니티 별 하루 접속자 수 순위표 제공
    * order_by를 통한 Table Community Field count를 기준으로 정렬된 리스트를 리턴 기능 구현
    * X-Forwarded-For를 받아 ip 주소를 확인하여 Field count를 증가시키는 기능 구현
* 가입되지 않은 커뮤니티에 가입 요청 / 요청 취소 가능
    * is_valid, save를 통해 community, user 객체가 있으면 invitation 객체를 저장하는 기능 구현
    * delete를 통해 community, user 객체가 있으면 invitation 객체를 삭제하는 기능 구현
* 커뮤니티 생성
    * 커뮤니티 생성자는 관리자로 자동 설정
    * transaction.atomic을 사용하여 CommunityModel, TagAndCommunityModel, UserAndCommunityModel을 동시에 저장하는 기능 구현

### 마이 페이지
* 비밀번호 변경 가능
    * check_password를 통해 실제 비밀번호가 맞는지 확인 후 serializer validate로 검증 후 비밀번호 변경하는 기능 구현
* 가입된 커뮤니티 관리
    * delete를 통해 id값에 맞는 community 객체가 있으면 삭제하는 기능 구현
* 작성한 글 삭제
    * delete를 통해 id값에 맞는 article 객체가 있으면 삭제하는 기능 구현 
* 작성한 댓글 삭제
    * delete를 통해 id값에 맞는 comment 객체가 있으면 삭제하는 기능 구현
* 유저->커뮤니티 가입 요청 결과 조회 / 요청 철회 / 요청 삭제
    * is_valid, save를 통해 invitation 객체를 생성, 수정하는 기능 구현
    * delete를 통해 id값에 맞는 invitation 객체가 있으면 삭제하는 기능 구현
* 커뮤니티->유저 가입 요청 승락 / 요청 거절
    * is_valid, save를 통해 invitation 객체를 생성, 수정하는 기능 구현
    * delete를 통해 id값에 맞는 invitation 객체가 있으면 삭제하는 기능 구현
    
### 커뮤니티 페이지
* 게시판 생성
   * 생성자는 게시판 관리자도 자동 설정
* 게시글 작성
   * 이미지, 파일 업로드 가능
   * 게시글 제목, 내용중 하나라도 누락이 있을시 작성 불가능
* 게시글 수정
   * 게시글 제목, 내용중 하나라도 누락이 있을시 작성 불가능
* 댓글 작성
   * 내용이 없으면 작성 불가능

## 사용한 모델
* [게시글 감정분석](https://colab.research.google.com/drive/19Ikjcbwx0sWdgx7x1_ooXF2fU5lgsdTh?usp=sharing)

* [비속어 분류](https://colab.research.google.com/drive/1ATOO7HLKlde4koGZ0KPf36-AhIuWPJPJ?usp=sharing)

* [EasyOCR](https://colab.research.google.com/drive/1q1eziFDLWD0mWkuFAfaEJBcXtU27StfF?usp=sharing)

## 🏚 Architecture
![186589235-d27760f4-2d18-4642-90be-950eca5e2a92](https://user-images.githubusercontent.com/90381057/186792240-d9ec22b6-849c-4743-a5fd-8e01c93194a5.png)


## ⚙ [ERD](https://www.erdcloud.com/d/EL9ztjydoLhqhysPe)
![186103025-070baeb8-083d-4394-9153-207b4751c940](https://user-images.githubusercontent.com/90381057/186792091-80933248-481a-402a-9622-14f12739912b.png)

## 🚀 **[API 설계](https://documenter.getpostman.com/view/16204656/VUqypEbL)**

## 🗺 Layout
![Group 26](https://user-images.githubusercontent.com/90381057/186547234-04a9537b-2f48-4a3d-903b-bed3f7b3ba8d.png)
