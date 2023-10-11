'''
Initialize all weights and biases to random values

Compute the net incoming value and output value for each neuron in the network and keep going forward.
 
At the last layer, compute the output error (output delta)

Use the output delta to compute delta and weight update of next to last layer, and similarly go backwards and at each step use the delta of the foward layer to update the weights of the backward layer

Repeat the forward and backward passes until you have reached the desired accuracy or have reached the maximum number of steps specified.
'''
