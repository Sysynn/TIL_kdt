# CSS란
- 스타일을 정하고 시각적으로 정하는 역할
- HTML로 만들기 때문에 HTML이 꼭 필요함
- 캐스케이딩 스타일 시트

## CSS rule
```html
selector {
    property: value;
}
```
```html
input[type="text"]:nth-of-type(2n){
    border:2px solid red;
}
```
- 아래 박스는 훨씬 복잡하지만 기본적으로 같은 문법임

## STYLE element
- Inline Style로 개별 줄에 적용하면 통일하거나 같은 스타일을 주고 싶을 때 어려울 수 있음
- 따라서 요소의 통일성 또는 한번에 같은 스타일을 적용하기 위해 외부 스타일시트에 스타일을 작성하는 방법이 있음
- 완전히 별개의 다른 문서 .css 확장자를 사용해 따로 관리하는 방법도 있음
```html
<head>
    <title>Forms Demo</title>
    <link rel="stylesheet" href="my_styles.css">
</head>
```
- 위 코드로 외부 css 파일을 링크할 수 있음

# 색 및 배경색 속성
- color: rebeccapurple; 등의 공식으로 색상을 지정할 수 있음
- 색상을 지정하는 방법은 매우 다양하며 스타일시트에 지정하는 것으로 모든 하부 요소에 동일한 효과를 적용함
- background-color같은 경우 사용할 수 있는 모든 공간을 차지함. (h2와 같은 블록요소에 적용할 경우 텍스트에만 적용되는 것이 아니라 화면 끝까지 차지함)
- background 특성은 훨씬 더 많은 것을 할 수 있음. 이미지를 넣는다던가, 그라디에이션을 적용한다던가 etc...

## CSS Colors
- 앞서 언급한 미리 명명된 색상 140가지 외에도 다른 방법으로도 적용할 수 있음
- 대표적으로 RGB 색을 적용하는 것이 있는데 빛의 여러 색을 섞어서 표현하는 컬러 시스템임
  rgb를 입력하고 채널 r,g,b 수치를 차례로 입력하는 방식

# Font Family
- 컴퓨터에 기본적으로 설치되어 있는 폰트라면, 해당 폰트를 그대로 적용할 수 있음
- cssfontstack.com 에서 나뉘어 있는 각각의 stack에서 OS별로 설치되어 있는 정도를 확인할 수 있음
```html
h1 {
    font-family: Segoe UI, Futura, Arial, sans-serif; */
}
```
- 위와 같은 css라면 앞의 폰트부터 순서대로 적용해서, 만약 Segoe UI가 없다면, Futura를, Futura도 없다면 Arial을, 
  Arial도 없다면 sans-serif family 중 설치되어 있는 폰트를 아무거나 적용한다는 의미
- 기본적으로 priority를 지정해주는 작업이라고 볼 수 있다
