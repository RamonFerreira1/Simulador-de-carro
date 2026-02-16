---

# 🏎️ AutoDrive - Simulador de Controle de Veículo

Este é um projeto desenvolvido em **Python** que simula o sistema de controle de um veículo automotor da empresa **AutoDrive**. O simulador foca na implementação de regras de segurança e lógica de sincronização entre velocidade e transmissão.

---

## 🛠️ Funcionalidades e Regras de Negócio

O sistema gerencia o estado do veículo através de diversas verificações lógicas:

* **Ignição Inteligente:** O veículo só permite ações de movimento se estiver ligado. Para desligar, é obrigatório estar a **0 km/h** e em **Ponto Morto (0)**.
* **Gestão de Transmissão:** Sistema de 6 marchas com faixas de velocidade específicas:
* **Marcha 1:** 0-20 km/h
* **Marcha 2:** 20-40 km/h
* ...até a **Marcha 6:** 100-120 km/h.


* **Troca Sequencial:** O simulador impede "pular marchas", permitindo apenas a mudança de uma posição por vez (ex: de 2ª para 3ª ou 2ª para 1ª).
* **Segurança em Manobras:** A mudança de direção (esquerda/direita) só é permitida em velocidades de segurança entre **1 e 40 km/h**.
* **Monitoramento de Estado:** Exibição em tempo real de velocidade, marcha e status do motor.

---

## 🧠 Conceitos Aplicados

Como estudante de Ciência da Computação, este projeto me permitiu aplicar:

1. **Variáveis Globais e Escopo:** Gerenciamento de estado compartilhado entre funções.
2. **Estruturas de Controle:** Uso extensivo de `match/case` e condicionais aninhadas para validação.
3. **Tratamento de Entradas:** Validação de tipos para evitar quebras no sistema (ex: `isdigit()`).

---

---

## 💡 Próximos Passos (Roadmap)

* [ ] Implementar consumo de combustível.
* [ ] Adicionar sistema de quilometragem percorrida.
* [ ] Criar uma interface gráfica (GUI) simples.

---

Desenvolvido por [Ramon Ferreira](https://github.com/RamonFerreira1).

---
