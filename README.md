# 나만의 프롬프트 생성기

칸만 채우면 글 · 이미지 · 영상 컷 · 릴스 스토리보드 · 업무 메일 프롬프트를 조합해 주는 생성기예요.
`prompt-generator.html` 한 파일로 동작하고, Streamlit은 이 파일을 웹에 띄우는 역할만 해요.

## 로컬에서 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 참고

- 입력한 내용은 어디로도 보내지 않아요. 브라우저 저장(localStorage)이 막힌 환경에서는 새로고침하면 입력이 지워져요.
- HTML 파일만 더블클릭해서 열어도 똑같이 쓸 수 있어요.
