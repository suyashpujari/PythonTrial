def tr_time():
    print("\n---Answer 5---")
    train_length=340
    tunnel_length=160
    #Total distance to be travelled by train
    distance=train_length+tunnel_length
    print("Total distance to be travelled by train:",distance,"meter")
    #Conversion of km per hour into m per seconds
    speed=(45*5)/18
    print("Speed=",speed,"m/sec")
    time=distance/speed
    print("Time taken by train to cross the tunnel=",time,"sec")