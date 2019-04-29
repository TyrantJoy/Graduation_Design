from motor import Motor

motor = Motor()

motor.forward(0.003, 512)
motor.backward(0.003, 512)
motor.destroy()
