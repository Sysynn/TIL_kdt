# Web - Positioning for CSS layout
## 개요
- 박스를 움직이기
## CSS Layout
- 각 요소의 위치와 크기를 조정하여 웹페이지의 디자인을 결정하는 것
- Display, Position, Floats, Flexbox ...

## CSS Position
- Normal Flow에서 요소를 끄집어내서 다른 위치로 배치하는 것

## Position 유형
- static 
  - 기본값
  - 요소를 Normal Flow에 따라 배치
- relative 상대 
  - 본인이 static이던 때의 위치가 기준위치
  - 요소를 Normal Flow에 따라 배치
  - 요소가 차지하는 공간은 static일 때와 같음 (static일 때의 특성 유지)
- absolute 
  - static이 아닌 부모를 찾아감
  - 요소를 Normal Flow에서 제거
  - 가장 가까운 relative 부모 요소를 기준으로 이동
  - 문서에서 요소가 차지하는 공간이 없어짐
- fixted 
  - absolute처럼 본인의 집을 버리고 이동
  - 우리가 보는 화면을 기준으로 이동 (viewport)
- sticky 
  - 끈끈이
  - 임계점에 다다르지 않았을 때는 Normal Flow에 따라 배치됨
  - 가장 가까운 block 부모 요소를 기준으로 이동
  - viewport의 특정 임계점에 스크롤 될 때 그 위치에서 고정됨(fixed)
  - 만약 다음 sticky 요소가 있다면 이전 요소의 자리를 대체하게 됨

  ## transform
  - 요소에 회전, 크기 조절, 기울이기, 이동 효괄ㄹ 부여
  