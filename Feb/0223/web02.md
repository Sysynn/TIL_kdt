# CSS Box model
- 모든 HTML 요소를 (사각형) 박스로 표현
- 웹사이트는 크고 작은 네모 박스로 구성된다

## Box의 구성
1. Margin : 이 박스와 다른 요소 사이의 공백. 가장 바깥쪽 영역
2. Border : 콘텐츠와 패딩을 감싸는 테두리 영역
3. Content : 콘텐츠가 표시되는 영역
4. Padding : 콘텐츠 주위에 위치하는 공백 영역

## Box 구성의 방향 별 명칭
- 상하 좌우 별로 top, bottom, left, right가 붙는다. 
- 예를 들면 margin-top, border-right, padding-bottom 이런 식...

## width & height 속성
- 요소의 너비와 높이를 지정
- 이 때 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함

### shorthand
```html
<style>
        .box1 {
            border-style : solid;
            border-width: 3px;
            border-color: red;
            border-bottom-color: blue;
            margin-top: 50px;
            margin-left: 30px;
            width: 300px;
            padding-left: 50px;
        }
        
        .box2 {
            width: 300px;
            /* shorthand - 작성순서 무관 */
            border: 1px solid black;
            /* shorthand */
            margin: 25px auto;
        }
    </style>
```

## Box type
- Block & Inline
```html
<style>
.index {
    display: block;
}
</style>
```
```html
<style>
.index {
    display: inline;
}
</style>
```
- Block은 위에서 아래로, Inline은 좌에서 우로 쌓인다.