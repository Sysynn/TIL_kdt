# World Wide Web
- 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

## Web site
여러 개의 Web page가 모인 것으로 사용자들에게 정보나 서비스를 제공하는 공간


# HTML
- 구조
- HyperText Markup Language

## Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

## Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - HTML, Markdown
- 연산이 불가능하고, 조건 반복문을 사용할 수 없다는 점에서 프로그래밍 언어라고 볼 수 없다

## HTML 문서의 구조
### TEXT Structure
- HTML 의 주요 목적 중 하나는 텍스트의 구조와 의미를 제공하는 것
예를 들어 <h1>은 단순히 텍스트를 크게 하는 것이 아닌 해당 문서의 최상위 제목이라는 의미를 부여

1. 대표적인 HTML Text structure
- Heading % Paragraphs : h1~6, p
- Lists : ol, ul, li
    - Unordered
    - orderd
- Emphasis & Importance : em, strong



```html
- <!DOCTYPE html>
    - 해당 문서가 html로 문서라는 것을 나타냄

- <html></html>
    - 전체 페이지의 콘텐츠를 포함
- <title></title>
    - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- head는 문서의 머리 부분으로 세팅에 가까움. 출력되는 부분이 아니기 때문에 사용자에게 보이지 않음
- 사용자에게 보이는 부분은 전부 body 부분임. 즉 웹 페이지에 출력되는 모든 컨텐츠는 body에 작성됨
```


# CSS
- Cascading Style Sheet 
- 웹 페이지의 디자인과 레이아웃을 구성하는 언어
```css
h1 {
    color: blue;
    font=size: 15px;
}
```

## CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있도록 함

### CSS Selectors 종류
1. 기본 선택자
- 전체(*) 선택자
- 요소(tag) 선택자
- 클래스(class) 선택자
- 아이디(id) 선택자
- 속성(attr) 선택자

2. 결합자(Combinators)
- 자손 결합자(""(space))
- 자식 결합자(>)

### CSS Selectors 특징
- 요소 선택자
    - 지정한 모든 태그를 선택
- 클래스(class) 선택자
    - 주어진 클래스 속성을 가진 모든 요소를 선택
    - 예) .index는 class="index"를 가진 모든 요소를 선택
- 아이디(id) 선택자
    - 주어진 아이디 속성을 가진 요소 선택
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
    - 예) #index는 id="index"를 가진 요소를 선택

느낌표 + Tab 하면 기본 html 구조가 생성됨!!
(아니면 html:5)


## Cascade & Specificity
- 동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 했을 때 어떤 규칙이 이기는지 결정하는 것

1. Cascade (계단식)
- 동일한 우선순위를 같는 규칙이 적용될 때 CSS 에서 마지막에 나오는 규칙이 사용
- 아래 예시에서 h1 태그 내용의 색은 blue가 적용됨
```css
h1 {
    color: red;
}

h1 {
    color: blue;
}
```

2. Specifity (우선순위)
- 선택자 별로 정해진 우선순위 점수에 따라 점수가 높은 규칙이 사용
- 아래 예시에서 h1 태그 내용의 색은 red가 적용됨
```css
.make-red {
    color: red;
}

h1 {
    color: blue;
}
```

html을 검색할 때는 항상 뒤에 "mdn"을 붙이기!