import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

xi_base = 4 / 30000
D_f = 3 - xi_base

def t0_model(theta_a, theta_b, xi):
    delta = theta_a - theta_b
    damping = np.exp(-xi * (delta / np.pi)**2 / D_f)
    return -np.cos(delta) * damping

chsh_angles = np.array([[0, np.pi/4], [0, 3*np.pi/4], [np.pi/2, np.pi/4], [np.pi/2, 3*np.pi/4]])
chsh_qm = 2 * np.sqrt(2)

class BellQFTNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return torch.tanh(self.fc3(x))

def generate_qm_data(n_samples=1000):
    theta_a = np.random.uniform(0, 2*np.pi, n_samples)
    theta_b = np.random.uniform(0, 2*np.pi, n_samples)
    return theta_a, theta_b, -np.cos(theta_a - theta_b)

def compute_chsh_nn(model, xi):
    chsh_vals = [model(torch.tensor([[ta, tb, xi]], dtype=torch.float32)).item() for ta, tb in chsh_angles]
    return chsh_vals[0] + chsh_vals[1] + chsh_vals[2] - chsh_vals[3]

def train_nn(xi_var, epochs=50):
    theta_a, theta_b, y = generate_qm_data()
    xi_arr = np.full(len(y), xi_var)
    X = torch.tensor(np.column_stack([theta_a, theta_b, xi_arr]), dtype=torch.float32)
    y_t = torch.tensor(y.reshape(-1,1), dtype=torch.float32)
    model = BellQFTNN()
    opt = optim.Adam(model.parameters(), lr=0.01)
    crit = nn.MSELoss()
    for _ in range(epochs):
        opt.zero_grad()
        out = model(X)
        loss = crit(out, y_t)
        loss.backward()
        opt.step()
    preds = model(X).detach().numpy().flatten()
    rmse = np.sqrt(np.mean((y - preds)**2)) * 100  # Approx % error
    chsh = compute_chsh_nn(model, xi_var)
    delta_chsh = abs(chsh - chsh_qm) / chsh_qm * 100
    return rmse, delta_chsh

# Beispiel-Run
xi = 1e-4
rmse, delta = train_nn(xi)
print(f'RMSE%: {rmse:.4f}, CHSH Δ%: {delta:.4f}')