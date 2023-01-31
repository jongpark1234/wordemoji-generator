import detach, translate, draw

for word in input():
    
    draw.process(word=word, filename=translate.process(detach.process(word)), fontsize=48)
