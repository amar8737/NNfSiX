'''
Creates a basic neuron with 3 inputs.

Associated YT NNFS tutorial: https://www.youtube.com/watch?v=Wo5dMEP_BbI
'''

import numpy as np
inputs = [1,2,3,2.5]
weights =[[0.2,0.8,-0.5,1.0],
            [0.5,-0.91,0.26,-0.5],
            [-0.26,-0.27,0.17,0.87]
          ]
bais = [2,3,0.5]
output = np.dot(weights,inputs)+bais
print(output)
