#!/home/adams/xvalad/ML/venv/bin/python
# NumpyUltraQuickTutorial by Google
# https://colab.research.google.com/github/google/eng-edu/blob/master/ml/cc/exercises/numpy_ultraquick_tutorial.ipynb
#
import numpy as np
print(np.version.version)
# Examples
one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print("1D array:\n",one_dimensional_array)
#
two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print("2D array:\n",two_dimensional_array)
#
zeros_array=np.zeros((3,4))
print("Zeros array 3x4:\n",zeros_array)
#
ones_array=np.ones((2,3))
print("Ones array 2x3\n",ones_array)
#
sequence_of_integers = np.arange(5,12)
print("Lower bound sequence from 5 to 12\n",sequence_of_integers)
#
random_integers_between_50_and_100 = np.random.randint(low=50,high= 101,size=(6))
print("Sequence of 6 random numbers between 50 and 100\n",random_integers_between_50_and_100)
#
random_floats_between_0_and_1 = np.random.random_sample([6]) # Updated from np.random.random()
print("Random floats between 0 and 1\n:",random_floats_between_0_and_1)
#
random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)
#
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)
#
# Task 1: Create a linear dataset
#
# Assign a sequence of integers from 6 to 20 (inclusive) to a NumPy array named feature.
#
feature = np.arange(6,21)
print(feature)
#
# Assign 15 values to a NumPy array named label such that;
#   label = (3)(feature) + 4
#
label = 3 * feature + 4
print(label)
#
# Task 2: Add some noise to the Dataset
# Insert a little floating point random noise between -2 and 2 into each element of the label array 
#
noise = (np.random.random_sample([15]) * 4) - 2.0 # Updated from np.random.random()
print(noise)
label = label+noise
print(label)