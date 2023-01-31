initialMatch = {
    'ㄱ': 'g',
    'ㄲ': 'gg',
    'ㄴ': 'n',
    'ㄷ': 'd',
    'ㄸ': 'dd',
    'ㄹ': 'r',
    'ㅁ': 'm',
    'ㅂ': 'b',
    'ㅃ': 'bb',
    'ㅅ': 's',
    'ㅆ': 'ss',
    'ㅇ': '',
    'ㅈ': 'j',
    'ㅉ': 'jj',
    'ㅊ': 'ch',
    'ㅋ': 'k',
    'ㅌ': 't',
    'ㅍ': 'p',
    'ㅎ': 'h'
}
neutralMatch = {
    'ㅏ': 'a',
    'ㅐ': 'ae',
    'ㅑ': 'ya',
    'ㅒ': 'yae',
    'ㅓ': 'eo',
    'ㅔ': 'e',
    'ㅕ': 'yeo',
    'ㅖ': 'ye',
    'ㅗ': 'o',
    'ㅘ': 'wa',
    'ㅙ': 'wae',
    'ㅚ': 'oe',
    'ㅛ': 'yo',
    'ㅜ': 'u',
    'ㅝ': 'wo',
    'ㅞ': 'we',
    'ㅟ': 'wi',
    'ㅠ': 'yu',
    'ㅡ': 'eu',
    'ㅢ': 'ui',
    'ㅣ': 'i'
}
finalMatch = {
    ' ': '',
    'ㄱ': 'g',
    'ㄲ': 'gg',
    'ㄳ': 'gs',
    'ㄴ': 'n',
    'ㄵ': 'nj',
    'ㄶ': 'nh',
    'ㄷ': 'd',
    'ㄹ': 'l',
    'ㄺ': 'lg',
    'ㄻ': 'lm',
    'ㄼ': 'lb',
    'ㄽ': 'ls',
    'ㄾ': 'lt',
    'ㄿ': 'lp',
    'ㅀ': 'lh',
    'ㅁ': 'm',
    'ㅂ': 'b',
    'ㅄ': 'bs',
    'ㅃ': 'bb',
    'ㅅ': 'th',
    'ㅆ': 'tth',
    'ㅇ': 'ng',
    'ㅈ': 'j',
    'ㅉ': 'jj',
    'ㅊ': 'ch',
    'ㅋ': 'k',
    'ㅌ': 't',
    'ㅍ': 'p',
    'ㅎ': 'h'
}

def process(words: list[str]) -> str:
    """로마자 형태의 글자 발음을 반환합니다.
    
    파일명의 중복을 피하기 위해 현재 사용되고 있는 로마자 표기법과 다른 부분이 존재합니다."""

    initial, neutral, final = words
    return initialMatch[initial] + neutralMatch[neutral] + finalMatch[final]
