import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



contas = pd.read_csv("\Desktop\Tabelas\importacao.csv")

contas.describe()