`[+-]?\d+(?:\.\d+)?` - всички цифри    
`[+-]?(\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?` - всички цифри    
`pad[dt]ing` - хваща padding и padting    
`pad(t|d)` - всичко което има padd или padt    
`([A-Z])\w+` - всички думи започващи с главна буква    
`\[.\]` - всички символи оградени в []    
`\’.*\’` - всички символи оградени в ‘’     
`s.*` - от s  до края на реда   
`[hc]at$` - хваща ако последната дума завършва на cat или hat   
`^[hc]at` - хваща ако първата дума започваща с cat или hat    
`ca?t` - хваща ако cat и ct     
`ca*t` - хваща ако cat и ct     
`cat|gat` - хваща ако cat или get     
 .* - целя ред
[^abtc…] - всичко освен abtc
pad{1,} - всичко което има pad, padd или paddd
[.W]\d - ако пред числото има . или W
a(?:bc)* - ако не е abc е само а
a(?<foo>bc) - връща abc и bc
cx="(?<foo>\d*.\d*) - взима стойностите на cx
<.*?> - всичко което е <>
\babc\b - цялата дума abc
\Babc\B - част от дума cabcd
([abc])\1 - част от групата
(?=r)d - ако е преди r селектира d - (?!r)d -обратното
(?<=r)d - ако е след r селектира d
(?<=[а-яa-z])\d{1,3} - ако след някоя буква има цифра
(\w+)\-(\w+) - две думи разделени с тире
^.*third.*$ - ако линия от код съдържа third
.*Eventname 2.*\n - връща цялата линия която съдържа Eventname 2
cx="(?<cx>\d*.\d*)"\s*cy="(?<cy>\d*.\d*)"\s*r="(?<r>\d*.\d*) - SVG
([\+\-]?\d+)\D*([\d,]+)\D*([\+\-]?\d+\.\d+)\D*([\+\-]?\d+)\D*([\d,]+)\D*([\+\-]?\d+\.\d+) - координати
(?<=с\.)([ЁёА-я].*)(?=\,\s[\о\б\щ])
(?<=% of )(.*)(?= at )
(.{2}) (.{2}) (.{2}) (.{2}) (.*)\n(.*)
rgb\((\d+)\,\s*(\d+)\,\s*(\d+)\)


. - matches any character except line breaks. Equivalent to [^\n\r].	
\w - matches any word character (alphanumeric & underscore). Only matches low-ascii characters (no accented or non-roman characters). Equivalent to [A-Za-z0-9_]	
\d - matches any digit character (0-9). Equivalent to [0-9].	
\s - matches any whitespace character (spaces, tabs, line breaks).	
[ABC] - matches any character in the set.	
[^ABC] - matches any character is not in the set.	
[A-Z] - matches a character having a character code between the two specified characters inclusive.

^ - matches the beginning of the string, or the beginning of a line if the multiline flag (m) is enabled. This matches a position, not a character.	
$ - matches the end of the string, or the end of a line if the multiline flag (m) is enabled. This matches a position, not a character.	
\b - matches a word boundary position such as whitespace, punctuation, or the start/end of the string. This matches a position, not a character.	
\B - matches any position that is not a word boundary. This matches a position, not a character.


(ABC) - groups multiple tokens together and creates a capture group for extracting a substring or using a backreference.	
\1 - matches the results of a previous capture group. For example \1 matches the results of the first capture group and \3 matches the third.	
(?:ABC) - groups multiple tokens together without creating a capture group.	
(?=ABC) - matches a group after the main expression without including it in the result.	
(?!ABC) - specifies a group that can not match after the main expression (if it matches, the result is discarded).

+ - matches 1 or more of the preceding token.	
* - matches 0 or more of the preceding token.	
{1,3} - matches the specified quantity of the previous token. {1,3} will match 1 to 3. {3} will match exactly 3. {3,} will match 3 or more.	
? - matches 0 or 1 of the preceding token, effectively making it optional.	
+?, *? and ??, are equal to the preceding quantifiers, but make them lazy causing it to match as few characters as possible. By default, quantifiers are greedy, and will match as many characters as possible.	
| - acts like a boolean OR. Matches the expression before or after the |. It can operate within a group, or on a whole expression. The patterns will be tested in order.	

(?=…) - Positive lookahead	(?=\d{10})\d{5}	01234 in 0123456789
(?<=…) - Positive lookbehind	(?<=\d)cat	cat in 1cat
(?!…) - Negative lookahead	(?!theatre)the\w+	theme
(?<!…) - Negative lookbehind	\w{3}(?<!mon)ster	Munster
