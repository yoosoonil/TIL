# ๐ปํ์ด์ฌ(Python)



## โ . ํ์ด์ฌ(Python)์ด๋?

1. ##### Easy to learn

   - ๋ค๋ฅธ ํ๋ก๊ทธ๋๋ฐ ์ธ์ด๋ณด๋ค ๋ฌธ๋ฒ์ด ๊ฐ๋จํ๋ฉด์ ์๊ฒฉํ์ง ์์
   - ๋ฌธ๋ฒ ํํ ๋งค์ฐ ๊ฐ๊ฒฐ

2. ##### Expressive Language

   - ๊ฐ์ ์์์์ C๋ ์๋ฐ๋ณด๋ค ๋ ๊ฐ๊ฒฐํ๊ฒ ์์ฑ ๊ฐ๋ฅ

3. ##### ํฌ๋ก์ค ํ๋ซํผ ์ธ์ด

   - ๋ค์ํ OS์์ ์คํ ๊ฐ๋ฅ

4. ##### ์ธํฐํ๋ฆฌํฐ ์ธ์ด(Interpreter)

   - ์์ค์ฝ๋๋ฅผ ๊ธฐ๊ณ์ด๋ก ๋ณํํ๋ ์ปดํ์ผ ๊ณผ์  ์์ด ๋ฐ๋ก ์คํ ๊ฐ๋ฅ
   - ์ฝ๋๋ฅผ ์์ฑ ํ ๋ฐ๋ก ํ์ธํ  ์ ์์

5. ##### ๊ฐ์ฒด ์งํฅ ํ๋ก๊ทธ๋๋ฐ

   - ํ์ด์ฌ์ ๊ฐ์ฒด์งํฅ ์ธ์ด์ด๋ฉฐ, ๋ชจ๋  ๊ฒ์ด ๊ฐ์ฒด๋ก ๊ตฌํ๋์ด ์์
     - ๊ฐ์ฒด(object) : ์ซ์,๋ฌธ์,ํด๋์ค ๋ฑ ๊ฐ์ ๊ฐ์ง๊ณ  ์๋ ๋ชจ๋  ๊ฒ. ์ฆ, ์ด๋ ํ ๊ฒ(๋ฌผ๊ฑด, ๋์)๋ค.



## โก. ๊ธฐ์ด ๋ฌธ๋ฒ

1. ##### ๋ค์ฌ์ฐ๊ธฐ

   - ๋ฌธ์ฅ์ ๊ตฌ๋ถํ  ๋, ๋ค์ฌ์ฐ๊ธฐ ์ฌ์ฉ
   - 4์นธ(spaceํค 4๋ฒ) ํน์ 1ํญ(Tabํค 1๋ฒ)์ ์๋ ฅ
   - ์์น์ ์ผ๋ก space ์ฌ์ฉํ์ฌ ๋ค์ฌ์ฐ๊ธฐ ๊ถ์ฅ

2. ##### ๋ณ์

   - ์ปดํจํฐ ๋ฉ๋ชจ๋ฆฌ์ ์ ์ฅ๋์ด ์๋ ๊ฐ์ฒด๋ฅผ ์ฐธ์กฐํ๊ธฐ ์ํด ์ฌ์ฉ๋๋ ์ด๋ฆ

     - ๊ฐ์ฒด : ์ซ์, ๋ฌธ์, ํด๋์ค ๋ฑ ๊ฐ์ ๊ฐ์ง๋ ๋ชจ๋  ๊ฒ

       > ํ์ด์ฌ์ ๊ฐ์ฒด์งํฅ ์ธ์ด์ด๋ฉฐ, ๋ชจ๋  ๊ฒ์ด ๊ฐ์ฒด๋ก ๊ตฌํ๋์ด ์์

   - ๋์ผ ๋ณ์์ ๋ค๋ฅธ ๊ฐ์ฒด๋ฅผ ํ ๋นํ  ์ ์๊ธฐ ๋๋ฌธ์, '๋ณ์'๋ผ๊ณ  ๋ถ๋ฆผ.

     ```python
     # swap
     x = 10 y= 20
     x, y = y, x
     print(x,y)
     # x์ y์ ๊ฐ์ด ๋ฐ๋์ด์ ์ ์ฅํ์ฌ ์ถ๋ ฅ.
     ```

3. ##### ์๋ณ์

4. ##### ์ฌ์ฉ์ ์๋ ฅ

   ```python
   name = input('์ด๋ฆ์ ์๋ ฅํด์ฃผ์ธ์ : ')
   print(name)
   # ์ด๋ฆ์ ์๋ ฅํด์ฃผ์ธ์ : ํ์ด์ฌ
   type(name)
   # str
   ```

5. ##### ์ฃผ์

   - ์ฝ๋์ ๋ํ ์ค๋ช
   - ๊ฐ๋ฐ์์๊ฒ ์ฃผ์์ ์์ฑํ๋ ์ต๊ด์ ์ค์
   - ์ฌ์ด ์ดํด์ ์ฝ๋์ ๋ถ์ ๋ฐ ์์ ์ด ์ฉ์ด



## โข. ๊ธฐ๋ณธ ์๋ฃํ(Python Datatype) 

1. ์๋ฃํ ๋ถ๋ฅ

   - ๋ถ๋ฆฐํ(Boolean)
     - True / False ๊ฐ์ ๊ฐ์ง ํ์์ bool
   - ์์นํ
     - int(์ ์)
     - float(์ค์)
     - complex(๋ณต์์)

   - ๋ฌธ์์ด
   - None





