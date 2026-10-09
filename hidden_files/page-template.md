# 아카이브 페이지 작성 템플릿

원문 텍스트: /home/hatch/workspace/naver-blog-archive/hidden_files/raw/{logno}.txt
출력 파일: /home/hatch/workspace/naver-blog-archive/posts/{logno}.html

## 템플릿 (그대로 사용, {} 부분만 채우기)

<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{원문 제목 그대로}</title>
<meta name="description" content="{핵심 요약 90~110자. 숫자 포함}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://raonhaze127-glitch.github.io/naver-blog-archive/posts/{logno}.html">
<style>
body {font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;max-width:760px;margin:0 auto;padding:40px 20px;line-height:1.8;color:#222}
h1 {line-height:1.4}
.date {color:#777}
.keywords {color:#555;font-size:.95rem}
.original {display:inline-block;margin-top:20px;padding:12px 18px;border:1px solid #222;border-radius:8px;text-decoration:none;color:#222}
footer {margin-top:50px;border-top:1px solid #ddd;padding-top:20px;color:#777}
</style>
</head>
<body>
<main>
<p><a href="../index.html">← 전체 글</a></p>
<h1>{원문 제목 그대로}</h1>
<p class="date">{YYYY-MM-DD}</p>
<h2>글 소개</h2>
<p>{원문 첫머리 요약 1~2문장}</p>
<h2>핵심 정리</h2>
<p>{단락1: 이 글이 다루는 공고/소식의 개요 — 기관, 대상, 규모(호수/세대수), 핵심 특징}</p>
<p>{단락2: 신청 자격·소득자산 기준·임대조건/분양가 등 핵심 조건}</p>
<ul>
<li>{핵심 일정 1: 접수 기간 등}</li>
<li>{핵심 일정 2: 발표일 등}</li>
<li>{주의사항}</li>
</ul>
<p>{단락3: 어떤 독자에게 유용한지 + 주의할 점 1~2문장}</p>
<p class="keywords"><strong>관련 키워드</strong><br>{키워드 4~6개, 쉼표 구분}</p>
<a class="original" href="https://blog.naver.com/tzarddogi/{logno}" target="_blank" rel="noopener noreferrer">네이버 블로그에서 원문 보기 →</a>
</main>
<footer>네이버 블로그 콘텐츠 아카이브</footer>
</body>
</html>

## 작성 규칙
- 제목은 원문 텍스트 첫 줄의 실제 블로그 제목 사용 (': 네이버 블로그' 접미사 제거)
- 날짜: 원문에서 확인한 발행일 (YYYY-MM-DD)
- 핵심 정리 전체가 300~500자, 페이지 전체 텍스트 1,300자 이상이 되도록 작성
- 원문에 없는 숫자·날짜를 지어내지 말 것. 불확실하면 "~로 안내" 형태로 완화
- HTML 특수문자(&, <, >)는 이스케이프
- 뉴스성 글(정책 뉴스 등)도 같은 구조로 작성 (일정 대신 핵심 내용 bullet)
