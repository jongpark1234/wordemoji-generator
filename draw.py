import os
from PIL import Image, ImageFont, ImageDraw

def process(word: str, filename: str, fontsize: int=72, indent: int=15) -> None:
    """background에 글자를 적어 results 폴더 내에 저장합니다.
    
    results 폴더가 존재하지 않을 시 경로를 만들어 저장합니다.
    
    기본 설정 폰트는 굴림입니다."""

    background = Image.open('./background.png')

    font = ImageFont.truetype('C:\\Windows\\Fonts\\gulim.ttc', fontsize)

    draw = ImageDraw.Draw(background)
    draw.text((indent, indent), word, (0, 0, 0), font=font)
    draw = ImageDraw.Draw(background)
    
    if not os.path.exists('./results'):
        os.mkdir('./results')

    background.save(f'./results/{filename}.png')
