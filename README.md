# Wi-Fi ARP Spoofer  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Scapy](https://img.shields.io/badge/Scapy-2.4.5%2B-orange)](https://scapy.net/)
![Linux](https://img.shields.io/badge/Linux-Compatible-orange)

Инструмент для демонстрации ARP-спуфинга (атаки "человек посередине").  
**Использовать только в образовательных целях и с явного разрешения владельца сети!**

---


## 🛠️ Функции  
- Проведение ARP-спуфинга между целевым устройством и роутером.  
- Симуляция MITM-атаки (Man-in-the-Middle).  
- Поддержка Linux, Windows и macOS (требуется настройка интерфейса).  

---

## ⚠️ Предупреждения  
- **Нелегально** использовать этот инструмент без разрешения владельца сети.  
- ARP-спуфинг может нарушить работу сети.  
- Код предоставляется "как есть", автор не несет ответственности за misuse.  

---
## 🛠️ Установка

### 🖥️ Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/Dimatop228/arp-spoofer.git
cd arp-spoofer
pip3 install -r requirements.txt
python arp-spoofer.py
```
