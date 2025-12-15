# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

# Create dataset
samples = 1000
X, y = make_circles(n_samples=samples, noise=0.03, random_state=42)

# Visualize the dataset
plt.figure(figsize=(6,6))
plt.scatter(X[:,0], X[:,1], c=y, cmap='bwr', alpha=0.7)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Binary Classification Dataset: Circles')
plt.show()

# Create a simple Sequential model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='sigmoid', input_shape=(2,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X, y, epochs=50, batch_size=32, verbose=1)

# Improved model with more layers and neurons, using Adam optimizer
model_improved = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model_improved.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history_improved = model_improved.fit(X, y, epochs=100, batch_size=32, verbose=1)

# Function to plot decision boundary
def plot_decision_boundary(model, X, y):
    x_min, x_max = X[:,0].min() - 0.1, X[:,0].max() + 0.1
    y_min, y_max = X[:,1].min() - 0.1, X[:,1].max() + 0.1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = (Z > 0.5).astype(int)
    Z = Z.reshape(xx.shape)
    
    plt.figure(figsize=(6,6))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
    plt.scatter(X[:,0], X[:,1], c=y, cmap='bwr', edgecolors='k')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Decision Boundary')
    plt.show()

# Plot for improved model
plot_decision_boundary(model_improved, X, y)

# Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model on training set
model_final = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model_final.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history_final = model_final.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

# Evaluate on test set
loss, accuracy = model_final.evaluate(X_test, y_test)
print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

# Train set
plot_decision_boundary(model_final, X_train, y_train)

# Test set
plot_decision_boundary(model_final, X_test, y_test)

## Key Takeaways

#- Neural networks can classify data with complex non-linear boundaries.
#- Visualizing data and decision boundaries helps understand model behavior.
#- Adding layers and neurons improves model capacity but requires tuning.
#- Activation functions (ReLU, Sigmoid) significantly impact learning.
#- Using Adam optimizer often converges faster and achieves better performance than SGD.
#

