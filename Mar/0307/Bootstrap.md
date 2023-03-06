# Web - Fundamentals of Bootstrap

## 개요
- 프론트엔드 라이브러리(Toolkit)
- 반응형 웹 디자인 & CSS 및 JS 기반의 컴포넌트와 스타일 제공
- 부트스트랩의 CDN이 포함된 코드 2줄을 넣고 시작하면 간단히 시행 가능함

1. Bootstrap 클래스명 맛보기
```html
<p class="mt-5">Hello, world!</p>
```
- mt-5 
- {property}{sides} - {size}

- 이미 스타일이 작성되어 있고 독특한 규칙이 있는 클래스 이름까지 있으니 설명서를 보며
  bootstrap이라는 도구상자를 어떻게 사용할 지 학습할 것

2. Typography
```html
<p class="h1">h1. Bootstrap heading</p>
<p class="h2">h2. Bootstrap heading</p>
<p class="h3">h3. Bootstrap heading</p>
<p class="h4">h4. Bootstrap heading</p>
<p class="h5">h5. Bootstrap heading</p>
<p class="h6">h6. Bootstrap heading</p>
```
- 기존의 h1 태그를 구조적으로 쓸 수 없을때 쓸 수 있으며 디자인적으로는 차이가 없다

```html
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
<h1 class="display-4">Display 4</h1>
<h1 class="display-5">Display 5</h1>
<h1 class="display-6">Display 6</h1>
```
- display heading은 조금 더 강조하고 싶을 때, 크기도 더 크고 디자인도 조금 다르다

3. Bootstrap Component
- Bootstrap에서 제공하는 UI 관련 요소
- 일관된 디자인, 쉬운 프로토 타입 제작 및 사용자 경험을 위해 사용한다
