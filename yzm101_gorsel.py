import matplotlib.pyplot as plt
import matplotlib.patches as patches

def setup_plot(title):
    fig, ax = plt.subplots(figsize=(12, 7), dpi=120)
    ax.set_facecolor('#ffffff')
    plt.title(title, fontsize=16, fontweight='bold', pad=20, color='#2c3e50')
    plt.axis('off')
    return fig, ax

def generate_all_visuals():
    # --- GÖRSEL 1: Donanım Katmanları ve İşlem Döngüsü ---
    fig1, ax1 = setup_plot("Donanım Katmanları ve Fetch-Decode-Execute Döngüsü")
    
    # CPU Alanı
    cpu_rect = patches.FancyBboxPatch((0.05, 0.4), 0.45, 0.5, boxstyle="round,pad=0.02", facecolor='#f1faff', edgecolor='#007bff', linewidth=2)
    ax1.add_patch(cpu_rect)
    plt.text(0.27, 0.85, 'CPU (İşlemci)', fontsize=14, fontweight='bold', ha='center', color='#007bff')
    
    # ALU ve Registers
    plt.text(0.18, 0.6, 'ALU\n(Aritmetik Mantık)', bbox=dict(boxstyle='round', fc='#e7f3ff', ec='#007bff'), ha='center', fontsize=11)
    plt.text(0.38, 0.6, 'Registers\n(Yazmaçlar)', bbox=dict(boxstyle='round', fc='#e7f3ff', ec='#007bff'), ha='center', fontsize=11)
    
    # RAM Alanı
    ram_rect = patches.FancyBboxPatch((0.65, 0.4), 0.25, 0.5, boxstyle="round,pad=0.02", facecolor='#fff7f2', edgecolor='#fd7e14', linewidth=2)
    ax1.add_patch(ram_rect)
    plt.text(0.77, 0.85, 'RAM (Bellek)', fontsize=14, fontweight='bold', ha='center', color='#fd7e14')
    
    # Akış Oku
    plt.annotate('', xy=(0.64, 0.65), xytext=(0.51, 0.65), arrowprops=dict(arrowstyle='<->', color='#34495e', lw=2.5))
    plt.text(0.57, 0.68, 'Veri Yolu', ha='center', fontsize=10, fontweight='bold')
    
    # Döngü Adımları
    steps = "1. FETCH: Komutu RAM'den getir\n2. DECODE: Komutu işlemci diline çöz\n3. EXECUTE: ALU ile işlemi yürüt\n4. STORE: Sonucu sakla"
    plt.text(0.5, 0.15, steps, ha='center', fontsize=12, bbox=dict(boxstyle='round,pad=1', fc='#f8f9fa', ec='#ced4da'), style='italic')
    plt.savefig('docs/images/01_donanim_mimari.png', bbox_inches='tight')

    # --- GÖRSEL 2: Derleme (Compilation) Süreci ---
    fig2, ax2 = setup_plot("C Programı Derleme Aşamaları (Compilation Flow)")
    
    stages = [
        "Kaynak Kod\n(.c)", "Ön İşleyici\n(Preprocessing)", 
        "Derleyici\n(Compiler)", "Assembler\n(Çevirici)", 
        "Bağlayıcı\n(Linker)", "Çalıştırılabilir Kod\n(.exe / .out)"
    ]
    colors = ['#6c757d', '#007bff', '#007bff', '#007bff', '#007bff', '#28a745']
    
    for i, stage in enumerate(stages):
        x_pos = 0.1 + (i * 0.16)
        plt.text(x_pos, 0.6, stage, ha='center', va='center', fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.8', fc=colors[i], ec='white', alpha=0.9), color='white')
        if i < len(stages) - 1:
            plt.annotate('', xy=(x_pos + 0.13, 0.6), xytext=(x_pos + 0.03, 0.6),
                         arrowprops=dict(arrowstyle='->', color='#adb5bd', lw=2))
    
    plt.text(0.5, 0.35, "Derleme Anı (Compile Time) İşlemleri", ha='center', color='#6c757d', style='italic')
    plt.savefig('docs/images/02_derleme_sureci.png', bbox_inches='tight')



    # --- GÖRSEL 4 Bellek Yerleşimi (Memory Layout) ---
    fig4, ax4 = setup_plot("Değişken Tanımlama ve Bellek (RAM) Adresleme")
    
    # Bellek Hücreleri (Tablo Görünümü)
    plt.text(0.5, 0.85, "int a = 10;  // 4 Byte yer kaplar", fontsize=12, family='monospace', bbox=dict(facecolor='#f8f9fa', alpha=0.5))
    
    for i in range(5):
        y = 0.7 - (i * 0.1)
        color = '#d0ebff' if i == 2 else 'white' # Seçili hücre
        rect = patches.Rectangle((0.3, y), 0.4, 0.08, edgecolor='#495057', facecolor=color)
        ax4.add_patch(rect)
        addr = f"0x004FF{i*4:X}"
        val = "00001010 (10)" if i == 2 else "..."
        plt.text(0.22, y+0.03, addr, family='monospace', fontsize=10)
        plt.text(0.5, y+0.03, val, ha='center', family='monospace', fontweight='bold' if i==2 else 'normal')

    plt.text(0.75, 0.44, "<- Değişken 'a'\n   burada saklanır", color='#1971c2', fontweight='bold')
    plt.savefig('docs/images/04_bellek_yerlesimi.png', bbox_inches='tight')
    
    print("Tüm görseller başarıyla üretildi: \n1. 01_donanim_mimari.png\n2. 02_derleme_sureci.png\n4. 04_bellek_yerlesimi.png")

if __name__ == "__main__":
    generate_all_visuals()
