# Flexbox
- 하나의 컨테이너 안에서 다양한 요소들을 보기좋게 배치하면서 레이아웃을 유연하게 조정

# Flex-Direction
- display는 블록, 인라인, 인라인블록과 flex가 있음
- flexbox에는 본측과 교차측이 있음. 본축의 기본방향은 왼쪽에서 오른쪽, 교차축은 위에서 아래
- flex-direction: row; 는 기본값으로 좌-우 방향이고 row-reverse는 본축의 방향이 우-좌로 바뀜
- flex-direction: column; 은 상-하방향, 마찬가지로 column-reverse 는 하-상 방향으로 바뀜
- flexbox를 품고 있는 부모 컨테이너의 크기가 flexbox보다 작으면 그 안에 알맞게 작아짐

# justify-content
- 주축을 기준으로 요소와 컨텐츠를 어떻게 배치할지 결정하는 속성. 
- 디폴트는 flex-start;로 설정되어 있음. (flex-direction이 시작점을 결정함)
- flex-end라면 끝점을 지점으로 함 (가로든 세로든), center면 가운데 정렬하고 space-between 이면 
  요소 사이에 일정 간격을 띄움 (양 쪽 끝의 요소는 마진없이 붙음)
- around; 는 요소 사이, 요소 사이에 동일한 크기의 여백을 줄 수 있음
  이 경우에는 결국 양쪽 끝에 절반씩 여백이 생기니 전체가 다 균등하진 않음
- space-evenly; 는 요소 사이, 요소와 컨테이너 사이에도 동일한 크기의 여백을 줌

# Flex-wrap
- wrap;과 wrap-revers;, 그리고 nowrap;이 있음
- 주축이 수평일 때, 새로운 행을 만들어 요소를 정렬하고 주축이 수직일 때는 새로운 열을 만들어 요소를 정렬

# Align-items
- flex-start;는 교차축의 시작점을 기준으로 함
- 쉽게 말하자면 flex-direction; row인 여러개의 요소가 있다고 가정할 때, justify-content: center;을 적용하면
  컨테이너의 좌우 가운데 정렬이 되고 align-items: center;를 적용하면 상하 가운데 정렬을 할 수 있음
- 만약 요소 안에 텍스트가 있다면 텍스트는 적용되지 않지만, baseline;을 적용하면 각 글자를 잇는 밑줄을 기준으로 정렬

# Align-content & Align=self
- 여러 행, 열이 있을 때만 사용하는 정렬 방법
- 예를 들어 수직을 주축으로 할 때 align-content는 열 사이의 공간을 조정
- align-self는 align-content와 비슷하지만 단일 요소에 사용하거나 플렉스 컨테이너에서 두 개의 요소에 개별로 사용함
- 플렉스 컨테이너 자체에는 쓰지 않는 속성으로 개별 요소에 적용할 때 사용
- 교차 축을 기준으로 배열된 단일 요소의 위치를 바꿈

# Flex-basis, grow & shrink
## Flex-basis
 - 요소가 한 줄로 늘어서 있을 때 flex-basis가 너비의 기준이 됨 (width는 무시됨)
 - width가 있는데 굳이 flex-basis를 쓰는 이유는 flex-basis는 가로인(혹은 세로인) 주축에 걸쳐있기 때문임
 - 즉, flex-basis는 요소가 배치될 때의 최초 크기 (배치에 따라 너비가 되기도 높이가 되기도 함)
## Flex-grow
 - flex-grow는 공간이 있을 때 요소가 그 공간을 얼마나 차지할 지 정함
 - max-width, min-width 등을 지정해서 최소, 최대값을 정할 수 있음
 - flex-grow는 남는 공간이 있을때 분배하는 방식
## Flex-shrink
 - flex-grow가 여백에 분배하는 방식이라면, 반대로 shrink는 남는 공간이 없을때 줄어드는 비율을 통제
 - 따라서 값을 줄 때 px로 주는 것 보다, 1, 2, 3 등등...자연수로 주는 것이 일반적
 - flex-shrink:0; 이면 창이 줄어들어도 해당 요소는 절대 줄어들지 않음

# Flex shorthand
- flex는 세 가지의 값을 한번에 입력 할 수 있음
- 순서는 flex-grow, flex-shrink, flex-basis 임
- 두개만 있으면 flex-grow, flex-shrink, 한개면 flex-grow가 디폴트

# 미디어쿼리(mediaqueries)
- 반응형 웹사이트 스타일을 수정하는 방법. 메뉴를 없애거나 숨길 수 있고, 크기를 바꾸거나 방향을 바꾸는 등 
- 뷰포트 너비나 높이 화면 방향과 같은 속성이 있음
- 모든 미디어쿼리는 @media로 시작하고 괄호 안에 미디어 기능을 다양하게 넣을 수 있음
```css
@media (min-width:360px) {
  div {
    color: red;
  }
}
```
- 창의 크기가 바뀜에 따라 속성에 변화값을 줌
