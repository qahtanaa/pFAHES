import sys


def find_all_patterns(T):
    # histogram
    hist = {col:T[col].value_counts() for col in T.columns}
    print(hist)
    # for each column in the csv
    for k, v in hist.items():
        col_hist = hist[k]
        # ptrns_vec contains pattern as a directory
        # pttrns_hist contains pattern string : frequency
        ptrns_vec, pttrns_hist = L1_patterns(col_hist)
    # print(T['a'].value_counts().get(1))


def L1_patterns(col_hist):
    # given a column, for each row
    for k, v in col_hist.items():
        pttrn = L1_pattern(k)
        print(pttrn)
    return 1,1

def L1_pattern(k):
    if not isinstance(k, str):
        print("Error reading non string!\n")
        sys.exit(1)
    pttrn = []
    # class and number of previous char
    prev_c = None
    prev_n = None
    for i in range(len(k)):
        ch = get_char_class(k[i])
        if(ch == prev_c):
            if(ch == SPACE):
                continue
            prev_n = prev_n + 1
            pttrn.pop()
            pttrn.append(ch + str(prev_n))
        else:
            pttrn.append(ch)
            prev_n = 1
        prev_c = ch
	remove_enclosing(pttrn)
    return pttrn

def remove_enclosing(pttrn):
	if(check_enclosing(ptrn)):
		for i in range(len(k)):

def get_char_class(ch):
    if (ch.isdigit()):
        return DIGIT
    if (ch.islower()):
        return LOWER
    if (ch.isupper()):
        return UPPER
	# if (Special_Alphabet(ch)):
    #     return SPALPHA
    if ((ch == ':') or (ch == '?')):
        return PUNCT
    if ((ch == ' ') or (ch == '\t')):
        return SPACE
    if ((ch == '(') or (ch == '{') or (ch == '[')):
        return ENCLOSE
    if ((ch == ')') or (ch == '}') or (ch == ']')):
        return ENCLOSE
    if (ch == '-'):
        return DASH
    if (ch == '.'):
        return DOT
    if (ch == ','):
        return COMMA
    if (ch == '&'):
        return AND
    if (ch == '#'):
        return HASH
    if (ch == '@'):
        return AT
    if (ch == '%'):
        return PERCENT
    if (ch == '^'):
        return POWER
    if (ch == '*'):
        return ASTRSK
    if (ch == '!'):
        return NOT
    if (ch == '\''):
        return SQUOTE
    if (ch == '_'):
        return USCR
    if (ch == ';'):
        return PUNCT
    if (ch == '/'):
        return SLASH
    return SYMBOL

def Special_Alphabet(ch):
	cch = ord(ch)
	if ((cch >= 1) and (cch <=8)):
		return true
	if ((cch >= 11) and (cch <=26)):
		return true
	if ((cch >= 192) and (cch <=214)):
		return true
	if ((cch >= 217) and (cch <=246)):
		return true
	if ((cch >= 249) and (cch <=254)):
		return true
	return false

LOWER = 'l'
UPPER =	'u'
DIGIT =	'd'
SPACE =	's'
ALPHA =	'a'
ALNUM =	'x'
DASH =	'h'
DOT =	't'
COMMA =	'c'
SYMBOL=	'y'
PUNCT =	'p'
ENCLOSE='e'
WORDP =	'w'
AND	=	'&'
HASH =	'#'
AT =	'@'
PERCENT='%'
POWER =	'^'
ASTRSK ='*'
NOT	=	'!'
SQUOTE ='q'
USCR =	'_'
SLASH =	'/'
SPALPHA='v'
