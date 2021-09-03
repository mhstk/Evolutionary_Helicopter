import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):

        # layer_sizes example: [4, 10, 2]
        self.w1 = np.random.normal(0, 1, (layer_sizes[0], layer_sizes[1]))
        self.w2 = np.random.normal(0, 1, (layer_sizes[1], layer_sizes[2]))
        # self.w3 = np.random.normal(0, 0.1, layer_sizes[2])
        self.b1 = np.random.normal(0, 1, 1)
        self.b2 = np.random.normal(0, 1, 1)
        self.hidden_layer = np.zeros(layer_sizes[1])
        self.output_layer = np.zeros(layer_sizes[2])
        

    def activation(self, x):
        #sigmoid
        return 1/(1 + np.exp(-x))

    def forward(self, x):
        
        # x example: np.array([[0.1], [0.2], [0.3]])
        self.hidden_layer = self.activation(np.matmul(np.transpose(x), self.w1) + self.b1) 
        self.output_layer = self.activation(np.matmul(self.hidden_layer, self.w2) + self.b2)
        print("here" , self.output_layer)
        return self.output_layer[0, 0]




layer_sizes = [3, 4, 1]
nn = NeuralNetwork(layer_sizes)
print(nn.forward(np.array([[0.1], [0.2], [0.3]])))
