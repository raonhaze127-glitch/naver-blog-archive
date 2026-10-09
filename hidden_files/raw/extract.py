import re, html, sys, time, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def fetch(logno):
    url = f"https://m.blog.naver.com/tzarddogi/{logno}"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")

def extract_text(page):
    m = re.search(r'<div class="se-main-container"[^>]*>(.*)', page, re.S)
    seg = m.group(1) if m else page
    seg = re.split(r'<div class="se-footer', seg)[0]
    seg = re.sub(r'<script.*?</script>', '', seg, flags=re.S)
    seg = re.sub(r'<style.*?</style>', '', seg, flags=re.S)
    seg = re.sub(r'<[^>]+>', '\n', seg)
    seg = html.unescape(seg)
    lines = [l.strip() for l in seg.split('\n') if l.strip()]
    # 본문 시작(제목 이후)부터: '본문 기타 기능' 이후를 본문으로 간주
    try:
        i = lines.index('본문 기타 기능')
        lines = lines[i+1:]
    except ValueError:
        pass
    return '\n'.join(lines)

posts = sys.argv[1].split(',')
for logno in posts:
    try:
        page = fetch(logno.strip())
        text = extract_text(page)
        open(f"{logno.strip()}.txt", "w").write(text)
        print(logno.strip(), 'OK', len(text), 'chars')
    except Exception as e:
        print(logno.strip(), 'FAIL', e)
    time.sleep(1)
