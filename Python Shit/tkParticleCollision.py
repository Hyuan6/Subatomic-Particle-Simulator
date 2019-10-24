from tkinter import Tk, Canvas
from math import pi, ceil, cos, sin, floor
from time import time, sleep

frameDimension = (800,600)

circleRadius = 5
velocity = 1

frameRate = 60
delayPerFrame = 1/frameRate

class Segmentation_Fault(Exception):
    pass

class Simulator(Tk):

    particles = []

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.window = Canvas(self, bg = "black", height = frameDimension[1], width = frameDimension[0])
        self.window.master.title("Particle Simulator")
        self.window.pack()

        self.window.bind("<Button-1>", self.drawCircle)
        self.window.bind("<B1-Motion>", self.drawCircle)

        self.window.focus_set()

    def updateParticles(self):
        #TODO:: finish particle particle collision
        nextMoves = []

        #Iterate through each particle an get its next position
        for p in self.particles:
            _step = step(p, p.nextMove())
            
            #Check if next position already in NextMove
            #Can not use if statement with "in" operator b/c need access to object s
            for s in nextMoves:
                #If in nextMove, append to particleQueue
                if s == _step:
                    s.add(p)
                #Else append new step
                else:
                    nextMoves.append(_step)
        
        #while nextMoves contains steps w/ > 1 particles
        multiParticleStep = self.containsMultiple(nextMoves)
        while multiParticleStep != None:
            #Do perfectly elastic colision calculations
            nextMoves.remove(multiParticleStep)
            multiParticleStep.calculateNewParticlePositions(nextMoves)

        #Iterate through next steps, which all contain points with only 1 particle and update canvas
        for s in nextMoves:
            s.updateParticle()

        """
        for p in self.particles:
            try:
                x,y = p.nextMove()
                self.window.move(p.getDrawnObject(),x ,y)
            except:
                self.particles.remove(p)
        """
        
    def containsMultiple(self, steps):
        for s in steps:
            if s.particles > 1:
                return s
        return None           

    def getFidelity(self):
        circum = ceil(2*pi*circleRadius)
        k = 360

        rem = (circum + k) % k
        
        return circum if rem == 0 else circum + k - rem

    def drawCircle(self, event):
        x = event.x
        y = event.y
        
        #add particles to simulation
        particleFidelity = ceil(2*pi*circleRadius) #self.getFidelity()

        for i in range(particleFidelity):
            #must change int iterator to float for higher fidelity
            degree = i/particleFidelity * 360

            
            vX = velocity * cos(degree)
            vY = velocity * sin(degree)
            pX = circleRadius * cos(degree) + x
            pY = circleRadius * sin(degree) + y

            newParticle = particle(pX, pY, self.window, vX, vY)

            self.particles.append(newParticle)

class step:
    particleQueue = []

    def __init__(self, p, pos):
        self.pos = pos
        self.particleQueue.append(p)

    def __hash__(self):
        return hash(self.pos)

    def __eq__(self, other):
        return self.pos == other.getPos()

    def getPos(self):
        return self.pos

    def particles(self):
        return len(self.particleQueue)

    def add(self, p):
        self.particleQueue.append(p)

    def updateParticle(self):
        if len(self.particleQueue) > 1: raise Segmentation_Fault("Something Fucked Up")
        p = self.particleQueue[0]
        x, y = self.pos
        p.move(x,y)


    def calculateNewParticlePositions(self, nextMoves):
        pass

class particle:
    #Time to live in terms of number of iterations
    colorMax = 200
    ttl = colorMax
    drawnObject = None

    def __init__(self, x, y, window, velocityX, velocityY):
        self.window = window
        self.x = x
        self.y = y
        self.velocityX = velocityX
        self.velocityY = velocityY

        self.drawnObject = self.window.create_line(self.x,self.y, self.x + 1, self.y + 1, fill = "#ff0000", width = 1)
    
    def move(self, x, y):
        #Move Particle to colision point
        self.window.move(self.drawnObject,self.velocityX,self.velocityY)

        #Update Particle with post collision velocity(Direction since all velocities are the same)
        self.velocityX = x - self.x
        self.velocityY = y - self.y

        #Update particle ttl and color
        #TODO:: Color will always be 1 iteration behind?

        self.ttl -= 1
        self.setColor()

        if self.ttl == 0: 
            self.window.delete(self.drawnObject)
            return None

    def nextMove(self):
        #If hit left or right
        if self.x >= frameDimension[0] or self.x <= 0:
            #Conserve yV, Flip xV
            self.velocityX = -self.velocityX
        #If hit top or bottom
        if self.y >= frameDimension[1] or self.y <= 0: 
            #Converse xV, Flip yV
            self.velocityY = -self.velocityY

        #Calc next position
        x = self.x + self.velocityX
        y = self.y + self.velocityY

        #return Next position
        return (x, y)

    def setColor(self):
        livedPercentage = self.ttl / self.colorMax
        color255 = livedPercentage * 255
        adjustedColor255 = floor(color255 + (255- color255)/2)
        hexValue = hex(adjustedColor255)[2:]

        #Account for hex returning single values for color255 <= 16
        if len(hexValue) < 2:
            hexValue = "0" + hexValue

        self.window.itemconfig(self.drawnObject, fill = f"#{hexValue}0000")

    def getDrawnObject(self):
        return self.drawnObject

def main():
    sim = Simulator()
    
    while True:
        startTime = time()
        sim.updateParticles()
        sim.update_idletasks()
        sim.update()
        endTime = time()
        elapsedTime = endTime - startTime
        #Cap Frame rate at 60
        if elapsedTime < delayPerFrame:
            sleep(delayPerFrame-elapsedTime)

main()