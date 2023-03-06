# Semantic Web
- 조금 더 효율적으로 이해하고 웹데이터를 의미론적으로 표현하고 연결하는 개념
- 이 요소가 시각적으로 어떻게 보여질까? 에서 이 요소가 가진 목적과 역할은 뭘까? 로 생각의 전환

## Semantics in HTML
- H1 태그로 예를 들면, 페이지의 최상위 제목의미를 제공한다. 
- 모든 요소를 최상위 제목"처럼" 보이게 할 수는 있지만 의미론적 가치는 없다
- 즉, 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소를 의미

## 대표적인 semantic elements
- header
- nav
- main
- article
- section
- aside
- footer

## DRY 원칙
- 중복 배제. "Don't Repeat Yourself". 

## BEM
- Block, Element, Modifier
- 블록, 요소, 수정자 세 가지로 구성
- Blcok
  - 문단 전체에 적용된 요소 또는 요소를 담고 있는 컨테이너
  - 재사용 가능한 독립적 블록, 가장 바깥쪽 상위 요소
  - 재사용을 위해 margin 또는 padding 적용하지 않음
- Element
  - block이 포함하고 있는 한 조각
  - 블록을 구성하는 종속적인 하위 요소
- Modifier
  - block 또는 element의 속성

- oocss 에 비해 조금 더 종속적인 성격을 지님

## 의미론적인 마크업의 이점
- 검색 엔진이 해당 웹사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌
- 시각 장애 사용자가 스크린 리더기로 웹 페이지를 사용할 때 추가적 도움

## emmet
> : 자식속성
. : 클래스
https://docs.emmet.io/cheat-sheet/