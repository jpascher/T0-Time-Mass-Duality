import numpy as np

xi = 4 / 30000
D_f = 3 - xi
Lambda_QCD = 0.2
target_lambda = 1.0002

def beta_standard(lam, t): return lam**2 / (16 * np.pi**2)
def beta_T0(lam, t): 
    beta = beta_standard(lam, t)
    return beta * (1 + xi * lam / (4 * np.pi))
def beta_extended(lam, t):
    beta = beta_T0(lam, t)
    mu = np.exp(t)
    t_prime = np.log(mu / Lambda_QCD)
    damping = np.exp(-xi * t_prime / D_f)
    return beta * damping

def integrate_rge(mu_start, mu_end, lam_start, beta_func):
    num_points = 100
    log_mu = np.linspace(np.log(mu_start), np.log(mu_end), num_points)
    lam = np.zeros(num_points)
    lam[0] = lam_start
    for i in range(1, num_points):
        dt = log_mu[i] - log_mu[i-1]
        beta_val = beta_func(lam[i-1], log_mu[i-1])
        lam[i] = lam[i-1] + beta_val * dt
    return np.exp(log_mu), lam

# Run
mu_start, mu_end, lam_start = 2.0, 100.0, 0.13
mu_std, lam_std = integrate_rge(mu_start, mu_end, lam_start, beta_standard)
# ... (ähnlich für T0 und Extended)
# Delta-Berechnung wie oben