import random
import matplotlib.pyplot as plt


gun_sayisi = 365


sicakliklar = [random.uniform(-10, 40) for _ in range(gun_sayisi)]


ortalama_sicaklik = sum(sicakliklar) / gun_sayisi


en_sicak_gun = sicakliklar.index(max(sicakliklar)) + 1  
en_sicak_deger = max(sicakliklar)


en_soguk_gun = sicakliklar.index(min(sicakliklar)) + 1
en_soguk_deger = min(sicakliklar)


print(f"Ortalama sıcaklık: {ortalama_sicaklik:.2f}°C")
print(f"En sıcak gün: {en_sicak_gun}. gün ({en_sicak_deger:.2f}°C)")
print(f"En soğuk gün: {en_soguk_gun}. gün ({en_soguk_deger:.2f}°C)")


plt.figure(figsize=(15, 6))  
plt.plot(range(1, gun_sayisi + 1), sicakliklar, color='green', label='Günlük Sıcaklık')  
plt.axhline(y=ortalama_sicaklik, color='red', linestyle='--', label=f'Ortalama ({ortalama_sicaklik:.2f}°C)')  
plt.scatter([en_sicak_gun], [en_sicak_deger], color='orange', label='En Sıcak Gün')  
plt.scatter([en_soguk_gun], [en_soguk_deger], color='blue', label='En Soğuk Gün')  
plt.title("Bir Yıllık Günlük Sıcaklık Değişimi")  
plt.xlabel("Gün")  
plt.ylabel("Sıcaklık (°C)")  
plt.legend()  
plt.grid(True)  
plt.tight_layout()  
plt.show()  
