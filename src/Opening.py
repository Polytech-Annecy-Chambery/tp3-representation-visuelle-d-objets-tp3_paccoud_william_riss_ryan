# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        position = self.parameters["position"]
        height = self.parameters["height"]
        width = self.parameters["width"]
        thickness = self.parameters["thickness"]
        self.vertices = [ 
                position,
                [position[0],position[1], position[2] + height],
                [position[0] + width, position[1], position[2] + height],
                [position[0] + width, position[1], position[2]],
                
                [position[0], position[1] + thickness, position[2]],
                [position[0], position[1] + thickness, position[2] + height],
                [position[0] + width, position[1] + thickness, position[2] + height],
                [position[0] + width, position[1] + thickness, position[2]]
                ]
        self.faces = [
                #[0, 3, 2, 1],
                #[4, 7, 6, 5],
                [0, 1, 5, 4],

                [2, 3, 7, 6],
                [1, 2, 6, 5],
                [0, 3, 7, 4]
                ]  
        
    # Draws the faces                
    def draw(self):        
        gl.glPushMatrix() 
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen

        for face in self.faces:
            for i in face:
                gl.glVertex3fv(self.vertices[i])
           
        gl.glEnd()
        gl.glPopMatrix()