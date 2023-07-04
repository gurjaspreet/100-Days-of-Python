PA = 1000
ROI = 3
time = 5

CI = PA * (1 + ROI / 100) ** time
print(f'The future value of the investment: {CI:.2f} USD')