`timescale 1ns / 1ps

module Lock_Door_tb;

    logic clk;
    logic rst;
    logic in;
    logic unlocked;
    logic [1:0] screen;

    // Test edilecek modül (DUT)
    Lock_Door uut (
        .clk(clk),
        .rst(rst),
        .in(in),
        .unlocked(unlocked),
        .screen(screen)
    );

    // Saat sinyali üretimi (10ns periyot)
    always #5 clk = ~clk;

    initial begin
        // Başlangıç ayarları
        clk = 0;
        rst = 1;
        in  = 0;

        // Girişler saatin düşen kenarında (20, 30, 40 ns) değişir;
        // bitler 25, 35, 45 ns yükselen kenarlarında syc_in = 0, 1, 2 hücrelerine yazılır.
        #20;
        rst = 0;       // Reset kaldırıldı, kasa aktif!
        in  = 1'b1;    // 1. hane (Doğru)
        #10 in = 1'b0; // 2. hane (Doğru)
        #10 in = 1'b1; // 3. hane (Doğru -> 65 ns'de unlocked = 1)

        // Kilit açıldıktan sonraki çerçeve (55-75 ns) değerlendirilmez; 85 ns'den itibaren yeni çerçeve
        #40 in = 1'b0; // Yanlış şifre denemesi ("000")
        #10 in = 1'b0;
        #10 in = 1'b0;

        #60;
        $finish;
    end

    // Anlık takip ekranı
    initial begin
        $monitor("Zaman = %0t ns | rst = %b | in = %b | Ekran Kodu = %b | Kilit Açık = %b", 
                 $time, rst, in, screen, unlocked);
    end

endmodule