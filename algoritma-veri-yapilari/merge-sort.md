# merge-sort

Proje 2
--
[16,21,11,8,12,22] -> Merge Sort

- Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
- Big-O gösterimini yazınız.

Aşamalar
--

- Dizi [16,21,11] ve [8,12,22] şeklinde ikiye ayrılır.
- [16], [21,11] ve [8], [12,22] şeklinde tekrar bölme işlemi yapılır.
- [16], [21], [11] ve [8], [12], [22] şeklinde bölme işlemi tamamlanır.
- [16], [11,21] ve [8], [12,22] olarak birleştirme işlemi yapılır.
- [11,16,21] ve [8,12,22]
- [8,11,12,16,21,22]

Big-O Gösterimi
--

O(nlogn)
