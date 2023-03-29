# 유용한 CSS 속성들

## 불투명도와 알파 채널
- 알파 채널은 색상이 비치는 정도를 말하며 1은 전혀 투명하지 않다는 말이고 0은 투명한 상태를 말함.
- rgb 값과 결합하여 rgba 로 나타냄.(background-color: rgba(255, 255, 255, 0.7))
- 알파 채널과 불투명도의 가장 큰 차이점은, 불투명도를 사용할 때 버튼이나 다른 콘텐츠가 있으면 해당 콘텐츠도 영향을 받지만,
  RGBA에서는 이 한 요소의 배경색상에만 적용됨. 따라서 다른 요소가 있어도 특정 요소의 배경을 투명하게 하지 않으면 변하지 않음.

## 위치 속성(position)
1. static
 - 기본 위치 특성.
 - 요소의 특성이 static이면, top 등의 효과가 적용되지 않음.

2. relative
 - 문서의 일반적인 흐름에 따라 위치가 정해지지만 
   top, left, right, bottom 등 현 위치와의 상대적 위치로 오프셋을 줄 수 있음
 
3. absolute
 - 문서의 일반적인 흐름에서 요소가 제거되고 공간도 배정되지 않음
 - 위치를 차지하지 않고 부모로부터 상대적인 위치에 배치됨

4. fixed
 - absolute와 약간 비슷하지만 부모요소와 관계없이 초기 컨테이닝 블록의 상대적 위치
 - 스크롤을 내려도 항상 그 자리에 위치함 (nav바 등에 사용함)

5. sticky
 - fixed처럼 초기엔 고정되지 않은 상태로 스크롤을 따라가지만 위쪽에 도달하면 그 위치에 고정됨

## 전환 (transition)
- 한 특성 값에서 다른 값으로 변화할 때 전환으로 애니메이션 효과를 줌
- transition: property name | duration | timing function | delay
 - timing function
  1. linear; 일정한 속도로 변경
  2. ease-in; 천천히 시작됐다가 속도가 점점 빨라짐, ease-out 은 반대로 빠르게 시작 후 천천히 느려짐
  3. steps(6, end); 6단계에 걸쳐서 뚝 뚝 끊기면서 변경
  4. cubic-bezier(.29, 1.01, 1, -0.68); 앞뒤로 움직이는 듯한 변화를 보여줄 때 사용

## 변형 (transform)
1. rotate
 - rotate(90deg) 와 같이 각도를 입력하여 회전시킬 수 있다. (1.2turn) 처럼 회전 회수를 적용하는 것도 가능하지만 보통 각도를 사용
 - transform-origin: center; 혹은 left top, bottom right 등을 적용하여 변환점을 직접 설정할 수 있음
 - rotateX, rotateY 등을 사용하여 축을 기준으로 회전시키는 것도 가능 (카드 회전 등의 효과)
2. scale
 - scale(0.5); 등 비율을 설정하여 크기를 조정할 수 있음. (2, 1)처럼 값을 두개를 설정하면 width, height를 따로 적용 가능

3. tanslation(moving)
 - 가로로 움직이려면 translationX, 세로로 움직이려면 translationY 등을 사용하고 그냥 translate만 쓰면 X,Y 둘 다 적용(대각선)
4. skew
 - skew(10deg, 25deg); 등등 각도로 기울이기 (안중요함)

### 활용
- transform: rotate(-20deg), scale(1.3); 등 동시에 여러 속성을 적용
- 부모 뿐만 아니라 자식들에게 어떤 요소든지 모두 적용되기 때문에 매우 강력함

