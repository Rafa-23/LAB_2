import paho.mqtt.publish as pub
import numpy as np
import os
import time

def generate(median=90, err=10, outlier_err=30, size=1000, outlier_size=10):
    errs = err * np.random.rand(size) * np.random.choice((-1, 1), size)
    data = median + errs

    lower_errs = outlier_err * np.random.rand(outlier_size)
    lower_outliers = median - err - lower_errs

    upper_errs = outlier_err * np.random.rand(outlier_size)
    upper_outliers = median + err + upper_errs

    data = np.concatenate((data, lower_outliers, upper_outliers))
    np.random.shuffle(data)

    return data

if __name__ == '__main__':
    # TODO: retrieve the environment variable values for the mqtt broker and the desired rate for the publisher
    broker = os.environ.get('BROKER')
    rate = os.environ.get('RATE')
    topic = os.environ.get('TOPIC')
    rate = int(rate)
    
    
    # TODO: use the generate function to create a pool of values for the publisher
    data_pool = generate()
    
    
    # TODO: publish a msg with a value randomly sampled from the data array. 
    # make it so that there's a 10% chance the value sent is null to emulate a sensor failure
    # you should filter these null values in Node Red 
    value = np.random.choice(data_pool)

    pub.single(topic,value,hostname=broker)
