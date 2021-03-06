# 💻파이썬(Python)



## Ⅰ. 파이썬(Python)이란?

1. ##### Easy to learn

   - 다른 프로그래밍 언어보다 문법이 간단하면서 엄격하지 않음
   - 문법 표현 매우 간결

2. ##### Expressive Language

   - 같은 작업에서 C나 자바보다 더 간결하게 작성 가능

3. ##### 크로스 플랫폼 언어

   - 다양한 OS에서 실행 가능

4. ##### 인터프리터 언어(Interpreter)

   - 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
   - 코드를 작성 후 바로 확인할 수 있음

5. ##### 객체 지향 프로그래밍

   - 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음
     - 객체(object) : 숫자,문자,클래스 등 값을 가지고 있는 모든 것. 즉, 어떠한 것(물건, 대상)들.



## Ⅱ. 기초 문법

1. ##### 들여쓰기

   - 문장을 구분할 때, 들여쓰기 사용
   - 4칸(space키 4번) 혹은 1탭(Tab키 1번)을 입력
   - 원칙적으로 space 사용하여 들여쓰기 권장

2. ##### 변수

   - 컴퓨터 메모리에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

     - 객체 : 숫자, 문자, 클래스 등 값을 가지는 모든 것

       > 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음

   - 동일 변수에 다른 객체를 할당할 수 있기 때문에, '변수'라고 불림.

     ```python
     # swap
     x = 10 y= 20
     x, y = y, x
     print(x,y)
     # x와 y의 값이 바뀌어서 저장하여 출력.
     ```

3. ##### 식별자

4. ##### 사용자 입력

   ```python
   name = input('이름을 입력해주세요 : ')
   print(name)
   # 이름을 입력해주세요 : 파이썬
   type(name)
   # str
   ```

5. ##### 주석

   - 코드에 대한 설명
   - 개발자에게 주석을 작성하는 습관은 중요
   - 쉬운 이해와 코드의 분석 및 수정이 용이



## Ⅲ. 기본 자료형(Python Datatype) 

1. 자료형 분류

   - 불린형(Boolean)
     - True / False 값을 가진 타입은 bool
   - 수치형
     - int(정수)
     - float(실수)
     - complex(복소수)

   - 문자열
   - None





