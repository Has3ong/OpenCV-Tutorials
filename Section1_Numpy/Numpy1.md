## Numpy1

* NumPy is the fundamental package for scientific computing with Python.
* It contains among other things:

    * a powerful N-dimensional array object
    * sophisticated (broadcasting) functions
    * tools for integrating C/C++ and Fortran code
    * useful linear algebra, Fourier transform, and random number capabilities

* Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined.
* This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.
* NumPy is licensed under the BSD license, enabling reuse with few restrictions.

### Examples 
np.arange(0, 10, 2)
```****
[0 2 4 6 8]
```
np.zeros(shape=(10, 5))
```
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
```
print(np.ones((2, 4)))
```
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
```
np.random.seed(101)
np.random.randint(0, 100, 10)
```
[95 11 81 70 63 87 75  9 77 40]
```
matrix = np.arange(0, 100).reshape(10, 10)
```
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49]
 [50 51 52 53 54 55 56 57 58 59]
 [60 61 62 63 64 65 66 67 68 69]
 [70 71 72 73 74 75 76 77 78 79]
 [80 81 82 83 84 85 86 87 88 89]
 [90 91 92 93 94 95 96 97 98 99]]
```
matrix2 = matrix[:,1]. reshape(1, 10)
```
[[ 1 11 21 31 41 51 61 71 81 91]]
```
matrix3 = matrix[0:3, 0:3]
```
[[ 0  1  2]
 [10 11 12]
 [20 21 22]]
```
matrix[0:5, :] = 333
```
[[333 333 333 333 333 333 333 333 333 333]
 [333 333 333 333 333 333 333 333 333 333]
 [333 333 333 333 333 333 333 333 333 333]
 [333 333 333 333 333 333 333 333 333 333]
 [333 333 333 333 333 333 333 333 333 333]
 [ 50  51  52  53  54  55  56  57  58  59]
 [ 60  61  62  63  64  65  66  67  68  69]
 [ 70  71  72  73  74  75  76  77  78  79]
 [ 80  81  82  83  84  85  86  87  88  89]
 [ 90  91  92  93  94  95  96  97  98  99]]
```