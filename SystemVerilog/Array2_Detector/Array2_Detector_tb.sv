`timescale 1ns / 1ps

module Array2_Detector_tb;

    // 1. Testbench sinyal tanımları (logic türünde)
    logic clk;
    logic rst;
    logic in;
    logic seq_a_detected;
    logic seq_b_detected;

    // 2. Test edilecek modülü (DUT - Device Under Test) bağlama (Instantiation)
    Array2_Detector uut (
        .clk(clk),
        .rst(rst),
        .in(in),
        .seq_a_detected(seq_a_detected),
        .seq_b_detected(seq_b_detected)
    );

    // 3. Saat (Clock) Sinyali Üretimi (Her 5ns'de bir terslenir, Periyot = 10ns -> 100MHz)
    always #5 clk = ~clk;

    // 4. Test Senaryoları (Stimulus)
    initial begin
        // Başlangıç değerleri
        clk = 0;
        rst = 1;
        in  = 0;

        // 20ns sonra reset sinyalini kaldır ve sisteme veri göndermeye başla
        #20;
        rst = 0;
        
        // --- SENARYO 1: Dizi A'yı test et ("1101") ---
        // Zaman: 20ns - 70ns arası 1, 1, 0, 1 dizisini verelim
        #10 in = 1; // 1. adım (SA1)
        #10 in = 1; // 2. adım (SA2)
        #10 in = 0; // 3. adım (SA3)
        #10 in = 1; // 4. adım -> seq_a_detected 1 olmalı!

        #10 in = 0; // Boşluk / Ara verelim
        #10 in = 0;

        // --- SENARYO 2: Dizi B'yi test et ("1011") ---
        // Zaman: 1011 dizisini verelim
        #10 in = 1; // 1. adım (SB1)
        #10 in = 0; // 2. adım (SB2)
        #10 in = 1; // 3. adım (SB3)
        #10 in = 1; // 4. adım -> seq_b_detected 1 olmalı!

        // --- SENARYO 3: Yanıltıcı / Karışık Akış ---
        #10 in = 0;
        #10 in = 1;
        #10 in = 1;
        #10 in = 1;
        #10 in = 0;

        // Simülasyonu sonlandır
        #50;
        $finish;
    end

    // 5. Konsola çıktılabilen anlık takip (Monitor)
    initial begin
        $monitor("Zaman = %0t ns | rst = %b | in = %b || Seq_A_Det = %b | Seq_B_Det = %b", 
                 $time, rst, in, seq_a_detected, seq_b_detected);
    end

endmodule