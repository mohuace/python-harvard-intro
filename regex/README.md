Regular expressions are nothing but patterns.
They are used to recognize or validate some type of patterns in your code.


.       --> any character except a new line
*       --> 0 or more repetitions
+       --> 1 or more repetitions
?       --> 0 or 1 repetition
{m}     --> m repetitions
{m,n}   --> m-n repetitions
^       --> matches the start of the string
$       --> matches the end of the string or just before the newline at the end of the string
[]      --> set of characters
[^]     --> Complementing the set (not present in the set)

\d      --> Decimal digit
\D      --> not a decimal digit
\s      --> whitespace characters
\S      --> Not a whitespace character
\w      --> word character as well as numbers and the underscore
\W      --> Not a word character

(...)   --> For grouping together
A|B     --> Either A or B
(?: ...) --> Non capturing version