from abc import ABC, abstractmethod
class Button(ABC):
    Button(x, y, wid, hei, lab):
        bounds = new Rectangle2D.Float(x-wid/2, y-hei/2, wid, hei)
        label = lab
        
        
    def render():
        rect(bounds.x, bounds.y bounds.width, bounds.height)
        fill(255)
        text(label, bounds.x+(bounds.width-textWidth(label))/2, bounds.y+bounds.height/2+textAscent()*0.375)
        
        
    @abstractmethod
    def click()
