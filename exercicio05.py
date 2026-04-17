from sklearn.ensemble import IsolationForest

# Cada sublista representa [uso_cpu%, uso_ram%] de um servidor
servidores = [[20, 30], [25, 35], [22, 32], [99, 95], [21, 31]]

modelo = IsolationForest(random_state=42)
modelo.fit(servidores)
predicoes = modelo.predict(servidores)

print("Predições por servidor:")
for i, (servidor, pred) in enumerate(zip(servidores, predicoes)):
    # -1 = anomalia (servidor com comportamento fora do padrão)
    # +1 = normal
    rotulo = "ANOMALIA" if pred == -1 else "Normal"
    print(f"  Servidor {i+1} [CPU: {servidor[0]}%, RAM: {servidor[1]}%] -> {pred} ({rotulo})")

print()
print("Valor -1 significa: o ponto está isolado na floresta de árvores aleatórias,")
print("ou seja, foi separado rapidamente por poucos cortes -> é uma anomalia.")
